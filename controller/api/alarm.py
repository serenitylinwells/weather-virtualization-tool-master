import json
import os

from fastapi import APIRouter

from model import ResponseModel
from model.exception import MyCustomException
from model.user import UserDTO

# 创建天气预警路由器实例
alarm_api = APIRouter()


# 请求用户预警制定记录
@alarm_api.get('/check-alarm/{username}')
async def alarm(username: str):
    """
    请求用户预警制定记录

    在数据库中检查用户制定的预警信息

    :param username: 用户名
    :return: 状态码，请求消息
    """
    alarm_json_path = os.path.join('db', 'alarms.json')

    with open(alarm_json_path, 'r') as f:
        alarms = json.load(f)
        if username not in alarms:
            return ResponseModel(code=1, msg="用户不存在", data={})

        return ResponseModel(code=0, msg="请求成功", data={"alarms": alarms[username]})


# 添加预警信息
@alarm_api.post('/set-alarm')
async def add_alarm(user: UserDTO):
    """
    请求添加用户制定的预警信息

    在数据库中添加用户制定的预警信息

    :param user: 用户
    :return: 状态码，请求消息，是否成功添加
    """

    alarm_json_path = os.path.join('db', 'alarms.json')

    with open(alarm_json_path, 'r') as f:
        alarms = json.load(f)

        # 在预警信息中检查用户制定的预警是否存在
        if user.username in alarms:
            for user_alarm in alarms[user.username]:
                if user_alarm == user.detail:
                    return ResponseModel(code=1, msg="相关预警已有定义", data={})
            # 如果预警不存在，则添加到预警信息中
            alarms[user.username].append(user.detail)
        else:
            # 如果用户不存在，则添加用户和预警到预警信息中
            alarms[user.username] = [[user.detail]]

    with open(alarm_json_path, 'w') as f:
        json.dump(alarms, f)

    return ResponseModel(code=0, msg="添加成功", data={})
