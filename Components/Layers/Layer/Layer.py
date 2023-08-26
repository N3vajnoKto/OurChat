from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QMouseEvent, QResizeEvent
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QEvent

from ...Settings.SideBar import SideBar


class Layer(QWidget):
    clicked = pyqtSignal()
    def __init__(self, parent: QObject = None):
        self.active: bool = False
        QWidget.__init__(self, parent)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColor(0, 0, 0, 150))
        self.setPalette(pal)


        self.sidebar = SideBar(self)

        self.sidebar.setEnabled(False)
        self.sidebar.hide()

    def isActive(self) -> bool:
        return self.active

    def setActive(self, b: bool):
        self.active = b

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.sidebar.resize(280, event.size().height())

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.clicked.emit()
        self.sidebar.remove()

    # def event(self, event: QEvent) -> bool:
    #     if self.isActive():
    #         if event.type == QEvent.Type.MouseButtonPress:
    #             self.mousePressEvent(event)
    #             return True
    #         else:
    #             return QWidget.event(self, event)
    #     else:
    #         return True

