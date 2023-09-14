from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt, QObject, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QPen, QPalette, QKeyEvent, QColor, QFont, QColorConstants, QPaintEvent, QPainter, QIcon, QBrush, QFocusEvent

from .IconButton import IconButton
from .. import UiController


class SearchLine(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.lineEdit = QLineEdit(self)

        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setFont(QFont(UiController.DefaultFontFamily, 10))
        self.lineEdit.setPlaceholderText("Search...")
        self.lineEdit.setFrame(False)

        self.buttonShown: bool = True

        self.closeButton = IconButton(QIcon("Components/Resources/icons/close.svg"), self)

        self.closeButton.setFixedSize(UiController.DefaultButtonSize)

        pal = self.lineEdit.palette()
        pal.setColor(QPalette.ColorRole.Base, QColorConstants.Transparent)
        self.lineEdit.setPalette(pal)

        lay = QHBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(10, 0, 10, 0)

        lay.addWidget(self.lineEdit)
        lay.addWidget(self.closeButton)

        self.setLayout(lay)

        self.lineEdit.textChanged.connect(self.manageCloseButton)
        self.closeButton.clicked.connect(self.clear)

        self.manageCloseButton()

    @pyqtSlot()
    def manageCloseButton(self):
        if len(self.lineEdit.text()) == 0 and self.buttonShown == True:
            self.closeButton.hide()
            self.buttonShown = False
        elif len(self.lineEdit.text()) != 0 and self.buttonShown == False:
            self.closeButton.show()
            self.buttonShown = True


    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(UiController.HoverBackgroundColor))
        painter.setPen(QPen(QColorConstants.Transparent))

        r = self.height() / 2

        painter.drawRoundedRect(0, 0, self.width(), self.height(), r, r)

    def search(self):
        pass

    @pyqtSlot()
    def clear(self):
        self.lineEdit.clear()
