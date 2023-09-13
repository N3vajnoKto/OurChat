from PyQt6.QtWidgets import QWidget, QStackedLayout, QGridLayout
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent
from PyQt6.QtCore import QObject, Qt, pyqtSignal


class OurChatUi(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)


    def focusMainPage(self):
        pass

    def focusLayer(self):
        pass

    def openSidebar(self):
        pass