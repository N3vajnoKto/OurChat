from .ApplicationInterface import ApplicationInterface
from . import ApplicationController
from ..Exceptions.ApplicationException import ApplicationException
from .Account import Account

class Application(ApplicationInterface):
    def __init__(self):
        print(ApplicationController.Application)
        ApplicationInterface.__init__(self)
        if ApplicationController.Application is not None:
            raise ApplicationException("Cannot create the Application", ApplicationException.Reason.ApplicationAlreadyExist)

        ApplicationController.Application = self

        self.accountList: list[Account] = []
        self.chatList: list[Account] = []

        self.__currentAccount: Account | None = None
        self.__currentIndex: int = -1

        self.__currentChat: Account | None = None
        self.__currentChatIndex: int = -1

    def resetCurrentChat(self):
        self.__currentChat = None
        self.__currentChatIndex = -1

    def Accounts(self) -> list:
        return self.accountList

    def Chats(self) -> list:
        return self.chatList

    def resetCurrentAccount(self):
        self.__currentAccount = None
        self.__currentIndex = -1

    def __getitem__(self, n: int) -> Account:
        return self.accountList[n]

    def __iter__(self):
        return self.accountList.__iter__()

    def addAccount(self, acc: Account):
        self.accountList.append(acc)

        if len(self.accountList) == 1:
            self.__currentIndex = 0
            self.__currentAccount = acc

    def removeAccount(self, acc: Account):
        self.accountList.remove(acc)
        if self.__currentAccount == acc:
            self.resetCurrentAccount()

    def addChat(self, acc: Account):
        self.chatList.append(acc)

        if len(self.chatList) == 1:
            self.__currentChatIndex = 0
            self.__currentChat = acc

    def removeChat(self, acc: Account):
        self.chatList.remove(acc)

        if self.__currentChat == acc:
            self.resetCurrentChat()

    def currentAccount(self) -> Account:
        return self.__currentAccount

    def currentIndex(self) -> int:
        return self.__currentIndex

    def setCurrentAccount(self, acc: Account):
        for i,account in enumerate(self.accountList):
            if (acc == account):
                self.__currentIndex = i
                self.__currentAccount = acc
                break
        else:
            self.addAccount(acc)
            self.setCurrentAccount(acc)

    def setCurrentIndex(self, i: int):
        self.__currentAccount = self.accountList[i]
        self.__currentIndex = i


