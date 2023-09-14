from typing import Optional

from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QObject, QMargins
from PyQt6.QtGui import QPalette, QColor, QResizeEvent, QColorConstants

from .InfoBoard import InfoBoard
from .PageList import PageList
from .Chat.ChatWidget import ChatWidget

from ..Back_End.Account import *
from .. import UiController
from ..Boxes.EmptyPage import EmptyPage

from .Chat.MessageInfo import MessageInfo


class PersonalChat(QWidget):
    def __init__(self, acc: Optional[Account] = Account, parent: QObject | None =None):
        QWidget.__init__(self, parent)
        self.setMinimumSize(300, 300)

        self.account: Optional[Account] = acc
        self.infoBoard = InfoBoard(acc, self)
        self.workSpace = PageList(self)
        self.chat = ChatWidget()

        self.workSpace.addWidget(EmptyPage(), "Empty Tab")
        self.workSpace.addWidget(self.chat, "Chat")

        lay = QVBoxLayout(self)
        lay.setContentsMargins(QMargins(0, 0, 0, 0))
        lay.setSpacing(0)
        lay.addWidget(self.infoBoard)
        lay.addWidget(self.workSpace)

        self.__infoBoardHeight = 54
        self.infoBoard.setFixedHeight(self.__infoBoardHeight)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColorConstants.White)
        self.setPalette(pal)

    def setAccount(self, acc: Account):
        self.account = acc
        self.infoBoard.setAccount(acc)

    def infoBoardHeight(self) -> int:
        return self.__infoBoardHeight

    def setInfoBoardHeight(self, h: int) -> None:
        self.__infoBoardHeight = h
        self.infoBoard.setFixedHeight(self.infoBoardHeight())

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.infoBoard.move(0, 0)
        self.infoBoard.resize(event.size().width(), self.infoBoardHeight())
