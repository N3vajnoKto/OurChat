from PyQt6.QtWidgets import QWidget, QSplitter
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent
from PyQt6.QtCore import QObject, Qt

from .WorkSpace import WorkSpace
from .HomeSpace import HomeSpace


class OurChat(QWidget):
    def __init__(self, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.resize(1000, 600)
        self.setWindowTitle("OurChat")
        self.setMinimumSize(400, 200)

        self.workSpace = WorkSpace(self)
        self.homeSpace = HomeSpace(self)
        self.splitter = QSplitter(self)
        self.splitter.resize(self.size())
        self.splitter.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.homeSpace)
        self.splitter.addWidget(self.workSpace)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setHandleWidth(0)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColor(255, 0, 0))
        self.setPalette(pal)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.splitter.resize(a0.size())
