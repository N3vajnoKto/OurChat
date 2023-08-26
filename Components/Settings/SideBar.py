from PyQt6.QtWidgets import QWidget, QStackedLayout
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent, QMouseEvent
from PyQt6.QtCore import QObject, Qt, pyqtSignal


class SideBar(QWidget):
    def __init__(self, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        pass

    def open(self):
        self.setEnabled(True)
        self.show()

    def remove(self):
        self.setEnabled(False)
        self.hide()