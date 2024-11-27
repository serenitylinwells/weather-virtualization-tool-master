import json
import os

from fastapi import APIRouter

from model import ResponseModel
from model.exception import MyCustomException
from model.user import UserDTO

# 创建注册路由器实例
register_api = APIRouter()


# 用户注册
@register_api.post('/register')
async def register(user: UserDTO):
    """
    用户注册

    检查数据库中是否有相同用户名，有则返回用户已存在，否则返回注册成功

    :param user: 用户
    :return: 状态码，请求消息，是否注册成功
    """
    user_json_path = os.path.join('db', 'users.json')

    with open(user_json_path, 'r+') as f:
        users = json.load(f)
        if user.username in users:
            return ResponseModel(code=1, msg="用户已存在", data={})

        users[user.username] = {'username': user.username, 'password': user.detail}
        f.seek(0)
        json.dump(users, f, indent=4)
        f.truncate()
        return ResponseModel(code=0, msg="注册成功", data={})


# 用户登录
@register_api.get('/login')
async def login(user: UserDTO):
    """
    用户登录

    检查用户名和密码

    :param user: 用户
    :return: 状态码，请求消息，是否登录成功
    """
    user_json_path = os.path.join('db', 'users.json')

    with open(user_json_path, 'r') as f:
        users = json.load(f)
        if user.username not in users or users[user.username]['password'] != user.detail:
            return ResponseModel(code=1, msg="用户不存在或密码错误", data={})

        return ResponseModel(code=0, msg="登录成功", data={})
