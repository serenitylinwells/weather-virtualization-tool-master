import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller.api import alarm, custom, register, weather
from controller.messageSender import MessageSender

app = FastAPI()
app.include_router(register.register_api, prefix="/weatherTool/register-api", tags=["注册接口"])
app.include_router(weather.weather_api, prefix="/weatherTool/weather-api", tags=["天气数据接口"])
app.include_router(alarm.alarm_api, prefix="/weatherTool/alarm-api", tags=["预警接口"])
app.include_router(custom.custom_api, prefix="/weatherTool/custom-api", tags=["个性化界面接口"])

message_sender = MessageSender()

if __name__ == '__main__':
    uvicorn.run(app="main:app", port=8081, reload=True)

# 配置 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#  venv\Scripts\activate
