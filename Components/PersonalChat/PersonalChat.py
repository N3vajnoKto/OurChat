from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette, QColor, QResizeEvent

from .InfoBoard import InfoBoard


class PersonalChat(QWidget):
    def __init__(self, name: str, parent=None):
        QWidget.__init__(self, parent)
        self.setMinimumSize(300, 300)

        self.name = name
        self.infoBoard = InfoBoard(self.name, self)
        self.__infoBoardHeight = 60

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColor(245, 245, 245))
        self.setPalette(pal)

    def infoBoardHeight(self) -> int:
        return self.__infoBoardHeight

    def setInfoBoardHeight(self, h: int) -> None:
        self.__infoBoardHeight = h
        self.infoBoard.resize(self.infoBoard.width(), self.infoBoardHeight())

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.infoBoard.move(0, 0)
        self.infoBoard.resize(event.size().width(), self.infoBoardHeight())
