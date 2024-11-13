import requests
import json
import gzip

from fastapi import APIRouter


from model import ResponseModel
from model.exception.my_exception import MyCustomException

# 创建天气路由器实例
weather_api = APIRouter()


# 请求天气数据
@weather_api.get("/getWeather")
async def get_weather(location: str = "101010100", lang: str = "zh", unit: str = "m"):
    """
    请求天气数据

    向和风天气API发送请求

    :param location: 需要查询地区的LocationID或以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位）
    :param lang: 多语言设置
    :param unit: 数据单位设置，可选值包括unit=m（公制单位，默认）和unit=i（英制单位）
    :return: 状态码，请求消息，响应数据
    """
    headers = {
        "X-QW-Api-Key": "08da0c0c5070482cab7a575133b53745"
    }
    response = requests.get(
        "https://devapi.qweather.com/v7/weather/now",

        headers=headers,

        params={
            "location": location,
            "lang": lang,
            "unit": unit,
        }
    )

    content = gzip.decompress(response.content)
    result_dict = json.loads(content.decode("utf-8"))
    status_code = result_dict["code"]
    if status_code != "200":
        raise MyCustomException("1", "和风天气API请求出错")
    return ResponseModel(code=0, msg="请求天气数据成功", data=result_dict)
