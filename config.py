from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    应用程序配置类，通过读取环境变量文件 `.env` 来加载配置项。

    Attributes:
        api_key (str): API接口密钥

    Config:
        env_file (str): 环境变量文件路径，默认为 `.env`。
    """
    api_key: str  # API接口密钥配置项

    class Config:
        env_file = ".env"  # 指定环境变量文件


settings = Settings()
