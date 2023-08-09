from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit
from PyQt6.QtCore import Qt, QObject, pyqtSignal
from PyQt6.QtGui import QPen, QKeyEvent, QColor, QFont, QColorConstants, QPaintEvent, QPainter, QBrush


class SearchLine(QLineEdit):
    def __init__(self, parent: QObject = None):
        QLineEdit.__init__(self, parent)

        self.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setFont(QFont("Open Sans", 10))
        self.setPlaceholderText("Search...")
        self.setFrame(False)

        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.Transparent)
        self.setPalette(pal)

        self.setContentsMargins(10, 5, 10, 5)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(245, 245, 245)))
        painter.setPen(QPen(QColorConstants.Transparent))

        r = self.height() / 2

        painter.drawRoundedRect(0, 0, self.width(), self.height(), r, r)

        QLineEdit.paintEvent(self, event)

    def search(self):
        print("searching", self.size())

    def keyPressEvent(self, e: QKeyEvent) -> None:
        if (e.key() == Qt.Key.Key_Return):
            self.search()
        else:
            QLineEdit.keyPressEvent(self, e)


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
        lay.setContentsMargins(10, 5, 10, 5)
        lay.addWidget(self.searchLine)
        self.setLayout(lay)