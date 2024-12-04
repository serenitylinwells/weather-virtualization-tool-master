from pydantic import BaseModel, Field
from typing import Any


class ResponseModel(BaseModel):
    """
    通用响应模型，用于标准化API响应格式。

    Attributes:
    - code (int): 状态码，0 表示成功，1 表示失败，2 表示空数据
    - msg (str): 描述信息，对应状态码的描述。
    - data (Any): 返回结果，包含具体的数据内容。
    """
    code: int = Field(title='状态码', description='状态码, 1:成功, 0:失败, 2:空数据')
    msg: str = Field(title="描述", description='状态码对应描述')
    data: Any = Field(title="返回结果")
