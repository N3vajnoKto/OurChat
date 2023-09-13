from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent

from ...PersonalChat.PersonalChat import PersonalChat
from ...Back_End.Account import *

class WorkSpace(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.resize(200, 300)
        self.setMinimumSize(340, 300)

        self.centralWidget:QWidget = PersonalChat(EmptyAccount, self)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColor(240, 240, 240))
        self.setPalette(pal)

    def setCentralWidget(self, w:QWidget):
        self.centralWidget = w
        w.resize(self.size())
        w.move(0, 0)
        w.setParent(self)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        if self.centralWidget != None:
            self.centralWidget.resize(a0.size())
