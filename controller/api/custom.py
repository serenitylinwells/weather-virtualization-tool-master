import json
import os

from fastapi import APIRouter

from model import ResponseModel
from model.exception import MyCustomException
from model.user import UserDTO

# 创建个性化界面路由器实例
custom_api = APIRouter()


# 请求用户个性化界面制定记录
@custom_api.get('/getCustom/{username}')
async def custom(username: str):
    """
    请求用户个性化界面制定记录

    在数据库中检查用户制定的个性化界面信息

    :param username: 用户名
    :return: 状态码，请求消息
    """
    custom_json_path = os.path.join('db', 'customs.json')

    with open(custom_json_path, 'r') as f:
        customs = json.load(f)
        if username not in customs:
            return ResponseModel(code=1, msg="用户不存在", data={})

        return ResponseModel(code=0, msg="请求成功", data={"customs": customs[username]})


# 添加个性化界面信息
@custom_api.post('/setCustom')
async def add_custom(user: UserDTO):
    """
    请求添加用户制定的个性化界面信息

    在数据库中添加用户制定的个性化界面信息

    :param user: 用户
    :return: 状态码，请求消息，是否成功添加
    """

    custom_json_path = os.path.join('db', 'customs.json')

    with open(custom_json_path, 'r') as f:
        customs = json.load(f)
        if user.username not in customs:
            customs[user.username] = []
        customs[user.username].append(user.detail)
        # 删除重复的预警信息
        customs[user.username] = list(set(customs[user.username]))

        with open(custom_json_path, 'w') as f:
            json.dump(customs, f)

        return ResponseModel(code=0, msg="添加成功", data={})
