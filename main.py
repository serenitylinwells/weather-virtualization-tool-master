import uvicorn
import json

from fastapi import FastAPI

from controller.api.weather import weather_api
from controller.api.city import city_api
from model import ResponseModel

app = FastAPI()
app.include_router(weather_api, prefix="/weatherTool/weather-api/", tags=["天气数据接口"])
app.include_router(city_api, prefix="/weatherTool/city-api/", tags=["城市数据接口"])

if __name__ == '__main__':
    uvicorn.run('main:app', port=8081, reload=True)
