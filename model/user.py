from typing import Union
from pydantic import BaseModel


class UserDTO(BaseModel):
    """
    数据传输对象，用于注册登录的请求。

    Attributes:
    - username (str): 用户名
    - password (str): 密码
    """

    username: str
    password: str
