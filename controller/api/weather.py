import requests
import json
import os
from fastapi import APIRouter

from model import ResponseModel
from model.exception import MyCustomException
from config import settings

API_KEY = settings.api_key
# 创建天气路由器实例
weather_api = APIRouter()

# 使用主密钥构造 Header
header = {"X-QW-Api-Key": API_KEY}


# 请求城市信息
@weather_api.get("/getCity/{location}")
async def get_city(location: str):
    """
    请求城市信息

    向和风天气API发送请求

    :param location: 需要查询地区的名称，支持文字、以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位）
    :return: 状态码，请求消息，城市信息
    """

    response = requests.get(
        "https://geoapi.qweather.com/v2/city/lookup",
        params={"location": location, "range": "cn", "lang": "en"},
        headers=header
    )

    result_dict = response.json()
    if result_dict["code"] != "200":
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
        params={"location": location, "lang": "en", "unit": "m"},
        headers=header
    )

    response_7_days = requests.get(
        "https://devapi.qweather.com/v7/weather/7d",
        params={"location": location, "lang": "en", "unit": "m"},
        headers=header
    )

    result_dict_real_time = response_real_time.json()
    result_dict_7_days = response_7_days.json()

    if result_dict_real_time["code"] != "200" or result_dict_7_days["code"] != "200":
        raise MyCustomException("1", "和风天气API请求出错")

    result_dict = {**result_dict_real_time, **result_dict_7_days}

    return ResponseModel(code=0, msg="请求天气数据成功", data=result_dict)