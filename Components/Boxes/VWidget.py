from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PyQt6.QtCore import Qt, QObject, pyqtSignal, QEvent, QPointF
from PyQt6.QtGui import QPalette, QWheelEvent, QColor, QColorConstants, QResizeEvent, QPainter, QBrush, QMouseEvent, \
    QCursor


class VWidget(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

    def resizeWidth(self, w: int):
        self.resize(w, self.height())
