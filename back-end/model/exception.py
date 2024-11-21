class MyCustomException(Exception):
    """
    自定义异常类

    Attributes:
    - errcode (str): 错误代码
    - message (str): 错误消息
    """
    def __init__(self, errcode: str, message: str):
        """
        初始化自定义异常

        Args:
        - errcode (str): 错误代码
        - message (str): 错误消息
        """
        self.message = message
        self.errcode = errcode
        super().__init__(self.message)
