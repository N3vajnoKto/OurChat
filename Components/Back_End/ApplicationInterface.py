from .Account import Account
from .Chat import Chat

class ApplicationInterface:
    def __init__(self):
        pass

    def resetCurrentChat(self):
        pass

    def Accounts(self) -> list[Account]:
        pass

    def Chats(self) -> list[Chat]:
        pass

    def resetCurrentAccount(self):
        pass

    def __getitem__(self, n: int) -> Account:
        pass

    def __iter__(self):
        pass

    def addAccount(self, acc: Account):
        pass

    def removeAccount(self, acc: Account):
        pass

    def addChat(self, acc: Chat):
        pass

    def removeChat(self, acc: Chat):
        pass

    def currentAccount(self) -> Account:
        pass

    def currentIndex(self) -> int:
        pass