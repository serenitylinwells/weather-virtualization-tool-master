import requests
import json
import gzip

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

    content = gzip.decompress(response.content)
    result_dict = json.loads(content.decode("utf-8"))
    status_code = result_dict["code"]
    if status_code != "200":
        raise MyCustomException("1", "和风天气API请求出错")
    return ResponseModel(code=0, msg="请求城市信息成功", data=result_dict)


# 请求天气数据（城市名）
@weather_api.get("/getWeather/{location_id}")
async def get_weather(location_id: str):
    """
    请求天气数据

    向和风天气API发送请求

    :param location_id: 需要查询地区的LocationID
    :return: 状态码，请求消息，天气信息
    """

    response = requests.get(
        "https://devapi.qweather.com/v7/weather/now",

        params={
            "location": location_id,
            "lang": "zh",
            "unit": "m"
        },

        headers=header
    )

    content = gzip.decompress(response.content)
    result_dict = json.loads(content.decode("utf-8"))
    status_code = result_dict["code"]
    if status_code != "200":
        raise MyCustomException("1", "和风天气API请求出错")

    weather_data = {
        "time": result_dict["now"]["obsTime"],  # 数据获取时间"2020-06-30T21:40+08:00"
        "temp": result_dict["now"]["temp"],  # 温度"24"（摄氏度）
        "feltTemp": result_dict["now"]["feelsLike"],  # 体感温度"26"（摄氏度）
        "text": result_dict["now"]["text"],  # 天气状况"多云"
        "windDir": result_dict["now"]["windDir"],  # 风向"东南风"
        "windScale": result_dict["now"]["windScale"],  # 风力等级"1"
        "windSpeed": result_dict["now"]["windSpeed"],  # 风速"3"（公里/小时）
        "humidity": result_dict["now"]["humidity"],  # 相对湿度"72"（%）
        "precip": result_dict["now"]["precip"],  # 降水量（毫米，过去一个钟）
        "pressure": result_dict["now"]["pressure"]  # 气压（百帕）
    }
    return ResponseModel(code=0, msg="请求天气数据成功", data=weather_data)


# 请求天气数据（经纬度）
@weather_api.get("/getWeather/{longitude_latitude}")
async def get_weather(longitude_latitude: str):
    """
    请求天气数据

    向和风天气API发送请求

    :param longitude_latitude: 需要查询地区的经纬度
    :return: 状态码，请求消息，天气信息
    """

    response = requests.get(
        "https://devapi.qweather.com/v7/weather/now",

        params={
            "location": longitude_latitude,
            "lang": "zh",
            "unit": "m"
        },

        headers=header
    )

    content = gzip.decompress(response.content)
    result_dict = json.loads(content.decode("utf-8"))
    status_code = result_dict["code"]
    if status_code != "200":
        raise MyCustomException("1", "和风天气API请求出错")

    weather_data = {
        "time": result_dict["now"]["obsTime"],  # 数据获取时间"2020-06-30T21:40+08:00"
        "temp": result_dict["now"]["temp"],  # 温度"24"（摄氏度）
        "feltTemp": result_dict["now"]["feelsLike"],  # 体感温度"26"（摄氏度）
        "text": result_dict["now"]["text"],  # 天气状况"多云"
        "windDir": result_dict["now"]["windDir"],  # 风向"东南风"
        "windScale": result_dict["now"]["windScale"],  # 风力等级"1"
        "windSpeed": result_dict["now"]["windSpeed"],  # 风速"3"（公里/小时）
        "humidity": result_dict["now"]["humidity"],  # 相对湿度"72"（%）
        "precip": result_dict["now"]["precip"],  # 降水量（毫米，过去一个钟）
        "pressure": result_dict["now"]["pressure"]  # 气压（百帕）
    }
    return ResponseModel(code=0, msg="请求天气数据成功", data=weather_data)
