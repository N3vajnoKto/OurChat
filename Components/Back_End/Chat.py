from typing import Optional
from .Account import Account

class Chat:
    def __init__(self, acc: Account):
        self.account = acc

    def lastMessage(self) -> Optional[str]:
        # TO DO
        return "last message"