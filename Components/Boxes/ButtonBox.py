from PyQt6.QtWidgets import QWidget, QSplitter
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QEvent, QChildEvent
from PyQt6.QtGui import QPalette, QColorConstants, QEnterEvent, QMouseEvent

class ButtonBox(QWidget):
    clicked = pyqtSignal(bool)
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.checked: bool = False

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.checked ^= True
            self.clicked.emit(self.checked)

    def childEvent(self, event: QChildEvent) -> None:
        if event.added() or event.removed():
            try:
                c = QWidget(event.child())
                c.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
            except (TypeError) as e:
                pass