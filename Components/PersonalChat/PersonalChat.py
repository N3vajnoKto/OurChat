from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QObject, QMargins
from PyQt6.QtGui import QPalette, QColor, QResizeEvent

from .InfoBoard import InfoBoard
from .PageList import PageList
from .Chat.Chat import Chat


class PersonalChat(QWidget):
    def __init__(self, name: str, parent=None):
        QWidget.__init__(self, parent)
        self.setMinimumSize(300, 300)

        self.name = name
        self.infoBoard = InfoBoard(self.name, self)
        self.workSpace = PageList(self)
        self.chat = Chat(self)

        w = QWidget(self)
        w2 = QWidget(self)

        w.setAutoFillBackground(True)
        pal = w.palette()
        pal.setColor(w.backgroundRole(), QColor(0, 0, 255))
        w.setPalette(pal)

        self.workSpace.addWidget(w, "firstWidget")
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
        pal.setColor(QPalette.ColorRole.Window, QColor(245, 245, 245))
        self.setPalette(pal)

    def infoBoardHeight(self) -> int:
        return self.__infoBoardHeight

    def setInfoBoardHeight(self, h: int) -> None:
        self.__infoBoardHeight = h
        self.infoBoard.setFixedHeight(self.infoBoardHeight())

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.infoBoard.move(0, 0)
        self.infoBoard.resize(event.size().width(), self.infoBoardHeight())
