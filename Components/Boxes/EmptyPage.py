from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt6.QtCore import QObject, QMargins, Qt, pyqtBoundSignal, pyqtSignal, QPoint, QEvent
from PyQt6.QtGui import QCursor, QEnterEvent, QMoveEvent, QPalette, QColor, QResizeEvent, QColorConstants, QFont, QMouseEvent, QPaintEvent, QPainter, QColor, QBrush, QPen, QPainterPath

from .. import UiController

class EmptyPage(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), UiController.ThemeColor)
        self.setPalette(pal)

        self.label = QLabel(self)
        self.label.setText("Empty Page")
        self.label.setFont(QFont(UiController.DefaultFontFamily, 30, QFont.Weight.Bold))

        pal = self.label.palette()
        pal.setColor(self.label.foregroundRole(), UiController.DimThemeColor)
        self.label.setPalette(pal)

        lay = QGridLayout(self)
        lay.setContentsMargins(QMargins(0, 0, 0, 0))
        lay.setSpacing(0)
        lay.addWidget(self.label)
        lay.setAlignment(Qt.AlignmentFlag.AlignCenter)