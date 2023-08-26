from PyQt6.QtWidgets import QWidget, QSplitter
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QEvent
from PyQt6.QtGui import QPalette, QColorConstants, QEnterEvent, QMouseEvent

class ButtonBox(QWidget):
    clicked = pyqtSignal()
    def __init__(self, parent: QObject = None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def leaveEvent(self, event: QEvent) -> None:
        self.setCursor(Qt.CursorShape.ArrowCursor)
