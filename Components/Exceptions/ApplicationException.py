from enum import Enum

class ApplicationException(Exception):

    class Reason(Enum):
        ApplicationAlreadyExist = 0

    def __init__(self, msg: str, reason):
        self.msg = msg
        self.reason = reason

    def __str__(self) -> str:
        return "ApplicationException: " + self.msg + ". Reason: " + str(self.reason)