from typing import Optional
from PyQt6.QtWidgets import QWidget, QStackedLayout, QGridLayout, QLineEdit, QFrame
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QEvent, pyqtSlot
from PyQt6.QtGui import QPalette, QBrush, QColor, QColorConstants, QPen, QPainter, QPaintEvent, QFont

from .. import UiController


class InputLine(QLineEdit):
    def __init__(self, parent: Optional[QWidget] = None):
        QLineEdit.__init__(self, parent)

        self.setContentsMargins(5, 10, 5, 10)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.Transparent)
        self.setPalette(pal)

        self.setFont(QFont(UiController.DefaultFontFamily, 10))

        self.setFrame(False)

        self.__valid: bool = True

    def isValid(self) -> bool:
        return self.__valid

    def setValid(self, b: bool):
        self.__valid = b
        self.update()


    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)


        if not self.isValid():
            painter.setBrush(QBrush(UiController.WA_BackgroundColor))
        else:
            painter.setBrush(QBrush(UiController.Light))
        painter.setPen(QPen(QColorConstants.Transparent, 0))
        painter.drawRect(self.rect())

        painter.setPen(QPen(UiController.Gray, 3))
        painter.drawLine(0, self.rect().height(), self.rect().width(), self.rect().height())

        painter.end()

        QLineEdit.paintEvent(self, event)

