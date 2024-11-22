import requests
import json

from fastapi import APIRouter

from model import ResponseModel
from model.exception import MyCustomException
from config import settings

# 创建天气路由器实例
weather_api = APIRouter()

header = {"X-QW-Api-Key": settings.api_key}


# 请求城市信息
@weather_api.get("/getCity/{location}")
async def get_city(location: str):
    """
    请求城市信息

    向和风天气API发送请求.

    :param location: 需要查询地区的名称，支持文字、以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位）
    :return: 状态码，请求消息，城市信息
    """

    response = requests.get(
        "https://geoapi.qweather.com/v2/city/lookup",

        params={
            "location": location,
            "range": "cn",
            "lang": "zh"
        },

        headers=header
    )

    result_dict = response.json()
    status_code = result_dict["code"]
    if status_code != "200":
        raise MyCustomException("1", "和风天气API请求出错")
    return ResponseModel(code=0, msg="请求城市信息成功", data=result_dict)


# 请求天气数据（城市id或经纬度）
@weather_api.get("/getWeather/{location}")
async def get_weather(location: str):
    """
    请求天气数据

    向和风天气API发送请求

    :param location: 需要查询地区的LocationID
    :return: 状态码，请求消息，天气信息
    """

    response_real_time = requests.get(
        "https://devapi.qweather.com/v7/weather/now",

        params={
            "location": location,
            "lang": "zh",
            "unit": "m"
        },

        headers=header
    )

    response_7_days = requests.get(
        "https://devapi.qweather.com/v7/weather/7d",

        params={
            "location": location,
            "lang": "zh",
            "unit": "m"
        },

        headers=header
    )

    result_dict_realTime = response_real_time.json()
    result_dict_7Days = response_7_days.json()

    status_code_realTime = result_dict_realTime["code"]
    status_code_10Days = result_dict_7Days["code"]

    if status_code_realTime != "200" or status_code_10Days != "200":
        raise MyCustomException("1", "和风天气API请求出错")

    result_dict = {**result_dict_realTime, **result_dict_7Days}

    return ResponseModel(code=0, msg="请求天气数据成功", data=result_dict)
