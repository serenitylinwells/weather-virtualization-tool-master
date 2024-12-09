import os
import json
import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv


# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量中获取密钥
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 600
# 创建注册路由器实例
register_api = APIRouter()


# 定义用户数据模型
class UserDTO(BaseModel):
    username: str
    detail: str


# 用户注册接口
@register_api.post("/register")
async def register(user: UserDTO):
    """
    用户注册接口
    检查是否有相同用户名，如果存在返回用户已存在，否则成功注册。
    """
    user_json_path = os.path.join("db", "users.json")
    os.makedirs(os.path.dirname(user_json_path), exist_ok=True)

    # 初始化用户数据文件
    if not os.path.exists(user_json_path):
        with open(user_json_path, "w") as f:
            json.dump({}, f)

    with open(user_json_path, "r+") as f:
        try:
            users = json.load(f)
        except json.JSONDecodeError:
            # 如果文件为空或格式错误，初始化为空字典
            users = {}
            f.seek(0)
            json.dump(users, f)
            f.truncate()

        # 检查用户名是否已存在
        if user.username in users:
            return {"code": 1, "msg": "用户已存在", "data": {}}

        # 添加用户
        users[user.username] = {"username": user.username, "password": user.detail}
        f.seek(0)
        json.dump(users, f, indent=4)
        f.truncate()

    return {"code": 0, "msg": "注册成功", "data": {}}


# 用户登录接口
@register_api.get("/login")
async def login(username: str, detail: str):
    """
    用户登录接口
    检查用户名和密码，验证成功返回 JWT Token。
    """
    user_json_path = os.path.join("db", "users.json")

    # 检查用户文件是否存在
    if not os.path.exists(user_json_path):
        return {"code": 1, "msg": "用户不存在或密码错误", "data": {}}

    with open(user_json_path, "r") as uf:
        users = json.load(uf)

        # 验证用户名和密码
        if username not in users or users[username]["password"] != detail:
            return {"code": 1, "msg": "用户不存在或密码错误", "data": {}}

        # 用户验证成功，生成 JWT Token
        token = create_access_token(data={"username": username})
        return {"code": 0, "msg": "登录成功", "data": {"token": token}}


# 生成 JWT Token
def create_access_token(data: dict):
    """
    创建 JWT Token
    :param data: 包含用户信息的字典
    :return: JWT Token 字符串
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# 验证 JWT Token
def verify_access_token(token: str):
    """
    验证 JWT Token
    :param token: JWT Token
    :return: 解码后的数据
    """
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token 已过期")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="无效的 Token")
