import uvicorn
import json

from fastapi import FastAPI
from controller.api.weather import weather_api

app = FastAPI()
app.include_router(weather_api, prefix="/weathertool/weather-api/", tags=["天气数据接口"])





if __name__ == '__main__':
    uvicorn.run('main:app', port=8081, reload=True)
