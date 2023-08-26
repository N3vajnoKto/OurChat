from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt, QObject, pyqtSignal
from PyQt6.QtGui import QPen, QPalette, QKeyEvent, QColor, QFont, QColorConstants, QPaintEvent, QPainter, QIcon, QBrush, QResizeEvent

from .IconButton import IconButton


class SearchLine(QWidget):
    def __init__(self, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.lineEdit = QLineEdit(self)

        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setFont(QFont("Open Sans", 10))
        self.lineEdit.setPlaceholderText("Search...")
        self.lineEdit.setFrame(False)

        self.closeButton = IconButton(QIcon("Components/Resources/icons/close.png"), self)

        self.closeButton.setFixedSize(15, 15)

        pal = self.lineEdit.palette()
        pal.setColor(QPalette.ColorRole.Base, QColorConstants.Transparent)
        self.lineEdit.setPalette(pal)

        lay = QHBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(10, 0, 10, 0)

        lay.addWidget(self.lineEdit)
        lay.addWidget(self.closeButton)

        self.setLayout(lay)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(245, 245, 245)))
        painter.setPen(QPen(QColorConstants.Transparent))

        r = self.height() / 2

        painter.drawRoundedRect(0, 0, self.width(), self.height(), r, r)

    def search(self):
        print("searching", self.size())


class SearchBox(QWidget):
    def __init__(self, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.setFixedHeight(54)

        self.setAutoFillBackground(True)

        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)

        self.searchLine = SearchLine(self)

        lay = QGridLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(10, 8, 10, 8)
        lay.addWidget(self.searchLine)
        self.setLayout(lay)