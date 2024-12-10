from api import message


class MessageSender:
    """
    短信发送器
    """
    @staticmethod
    def send_message(phone_number: str) -> None:
        """
        发送短信
        """
        message.send_message(phone_number)