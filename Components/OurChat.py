from PyQt6.QtWidgets import QWidget, QStackedLayout, QGridLayout, QApplication
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QEvent
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent, QFocusEvent

from .Layers.MainPage.MainPage import MainPage
from .Layers.Layer.Layer import Layer
from .Settings.SideBar import SideBar
from .OurChatUi import OurChatUi
from . import UiController


class OurChat(OurChatUi):
    def __init__(self, parent: QObject | None = None):
        OurChatUi.__init__(self, parent)
        UiController.Chat = self

        self.resize(1000, 600)
        self.setWindowTitle("OurChat")
        self.setMinimumSize(400, 400)

        self.layer = Layer(self)
        self.mainPage = MainPage(self)

        self.mainPage.setGeometry(0, 0, self.width(), self.height())
        self.layer.setGeometry(0, 0, self.width(), self.height())

        self.layer.clicked.connect(self.focusMainPage)


    def resizeEvent(self, event: QResizeEvent) -> None:
        self.mainPage.resize(event.size())
        self.layer.resize(event.size())

    def focusMainPage(self):
        self.mainPage.raise_()
        if QApplication.focusWidget() is not None:
            QApplication.sendEvent(QApplication.focusWidget(),
                                   QFocusEvent(QEvent.Type.FocusOut, Qt.FocusReason.NoFocusReason))
        self.setFocus(Qt.FocusReason.NoFocusReason)

    def focusLayer(self):
        self.layer.raise_()
        if QApplication.focusWidget() is not None:
            QApplication.sendEvent(QApplication.focusWidget(),
                                   QFocusEvent(QEvent.Type.FocusOut, Qt.FocusReason.NoFocusReason))
        self.setFocus(Qt.FocusReason.NoFocusReason)

    def openSidebar(self):
        self.focusLayer()
        self.layer.openSidebar()
