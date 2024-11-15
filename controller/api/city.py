import requests
import json
import gzip

from fastapi import APIRouter

from model import ResponseModel
from model.exception.my_exception import MyCustomException

# 创建城市路由器实例
city_api = APIRouter

locationID = ""


# 请求城市信息
@city_api.get("/getCity/{location}")
async def get_city(location: str):
    """
    请求城市信息

    向和风天气API发送请求.

    :param location: 需要查询地区的名称，支持文字、以英文逗号分隔的经度,纬度坐标（十进制，最多支持小数点后两位）
    :return: 状态码，请求消息，城市信息
    """

    global locationID

    headers = {
        "X-QW-Api-Key": "08da0c0c5070482cab7a575133b53745"
    }
    response = requests.get(
        "https://geoapi.qweather.com/v2/city/lookup",

        params={
            "location": location,
            "range": "cn",
            "lang": "zh"
        },

        headers=headers
    )

    content = gzip.decompress(response.content)
    result_dict = json.loads(content.decode("utf-8"))
    status_code = result_dict["code"]

    locationID = result_dict["location"]["id"]

    if status_code != "200":
        raise MyCustomException("1", "和风天气API请求出错")
    return ResponseModel(code=0, msg="请求城市信息成功", data=result_dict)
