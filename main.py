import uvicorn

from fastapi import FastAPI

from controller.api.register import register_api
from controller.api.weather import weather_api
from controller.api.alarm import alarm_api
from controller.api.custom import custom_api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(register_api, prefix="/weatherTool/register-api", tags=["注册接口"])
app.include_router(weather_api, prefix="/weatherTool/weather-api", tags=["天气数据接口"])
app.include_router(alarm_api, prefix="/weatherTool/alarm-api", tags=["预警接口"])
app.include_router(custom_api, prefix="/weatherTool/custom-api", tags=["个性化界面接口"])

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
