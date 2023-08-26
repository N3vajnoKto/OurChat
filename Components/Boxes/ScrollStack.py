from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QObject, pyqtSignal
from PyQt6.QtGui import QPalette, QWheelEvent, QColor, QColorConstants, QResizeEvent, QPainter, QBrush


class ScrollStack(QWidget):
    def __init__(self, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.box = QWidget(self)
        self.box.setFixedHeight(0)

        lay = QVBoxLayout(self.box)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        self.widgetList = []

        self.max = 0
        self.min = 0

    def addWidget(self, w: QWidget):
        self.widgetList.append(w)
        self.box.layout().addWidget(w)
        self.box.setFixedHeight(self.box.height() + w.height())

        self.max = self.height() - self.box.height()
        self.min = 0

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.box.resize(event.size().width(), self.box.height())
        self.max = self.height() - self.box.height()
        self.min = 0

        y = self.box.y()

        if not self.max <= y <= self.min:
            if abs(y - self.max) < abs(y - self.min):
                self.scrollTo(self.max)
            else:
                self.scrollTo(self.min)

    def wheelEvent(self, event: QWheelEvent) -> None:
        h = event.angleDelta().y()
        h = min(h, 40)
        h = max(h, -40)
        self.box.move(self.box.x(), max(self.max, min(self.min, self.box.y() + h)))

    def scrollTo(self, h: int):
        if not self.max <= h <= self.min:
            return
        self.box.move(self.x(), h)

