from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt, QObject, pyqtSignal
from PyQt6.QtGui import QPen, QPalette, QKeyEvent, QColor, QFont, QColorConstants, QPaintEvent, QPainter, QIcon, QBrush, QResizeEvent

from ...Boxes.SearchLine import SearchLine
from ...Boxes.IconButton import IconButton
from ... import UiController

class SearchBox(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.setFixedHeight(54)

        self.setAutoFillBackground(True)
        self.menuButton = IconButton(QIcon("Components/Resources/Icons/settings.svg"))
        self.menuButton.setFixedSize(UiController.DefaultButtonSize)

        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)

        self.searchLine = SearchLine(self)

        lay = QHBoxLayout(self)
        lay.setSpacing(10)
        lay.setContentsMargins(10, 8, 10, 8)
        lay.addWidget(self.menuButton)
        lay.addWidget(self.searchLine)
        self.setLayout(lay)