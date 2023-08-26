from PyQt6.QtWidgets import QWidget, QStackedLayout, QGridLayout
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent
from PyQt6.QtCore import QObject, Qt, pyqtSignal

from .Layers.MainPage.MainPage import MainPage
from .Layers.Layer.Layer import Layer
from .Settings.SideBar import SideBar


class OurChat(QWidget):
    def __init__(self, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.resize(1000, 600)
        self.setWindowTitle("OurChat")
        self.setMinimumSize(400, 400)

        self.mainPage = MainPage()
        # self.layer = Layer()

        lay = QStackedLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setStackingMode(QStackedLayout.StackingMode.StackAll)
        lay.addWidget(self.mainPage)
        # lay.addWidget(self.layer)

        self.stack = lay

        self.setLayout(lay)

        # self.layer.clicked.connect(self.focusMainPage)

        # self.currentPage = self.mainPage
        #
        # self.focusMainPage()
        # print(self.stack.currentWidget())

    # def resizeEvent(self, event: QResizeEvent) -> None:
    #     if self.currentPage is not None:
    #         self.currentPage.resize(event.size())
    #
    #
    # def focusMainPage(self):
    #     self.stack.setCurrentWidget(self.mainPage)
    #
    # def focusLayer(self):
    #     self.stack.setCurrentWidget(self.layer)

