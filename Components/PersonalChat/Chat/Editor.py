from PyQt6.QtWidgets import QWidget, QTextEdit, QFrame, QScrollBar
from PyQt6.QtCore import QObject, Qt, pyqtSignal
from PyQt6.QtGui import QColorConstants, QFont, QResizeEvent, QFontMetrics, QKeyEvent, QShortcut, QKeySequence

from ... import UiController

class ScrollBar(QScrollBar):
    def __init__(self, parent: QObject | None = None):
        QScrollBar.__init__(self, parent)
        self.setFixedSize(0,0)


class Editor(QTextEdit):
    heightChanged = pyqtSignal(int)
    textSended = pyqtSignal(str)
    def __init__(self, parent: QObject | None = None):
        QTextEdit.__init__(self, parent)

        self.maxHeight = 300
        self.setPlaceholderText("Write a message...")
        self.setFont(QFont(UiController.DefaultFontFamily, 10))
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.textChanged.connect(self.updateSizeAcWidth)

        self.setVerticalScrollBar(ScrollBar())

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setLineWrapMode(QTextEdit.LineWrapMode.FixedPixelWidth)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.updateSizeAcWidth()
        self.setLineWrapColumnOrWidth(self.width())

    def setMaxHeight(self, h: int):
        self.maxHeight = h
    def updateSizeAcWidth(self):
        h = int(self.document().size().height())

        if self.height() != h and h <= self.maxHeight:
            self.setMinimumHeight(h)
            self.heightChanged.emit(h)

    def textIsValid(self):
        text = self.toPlainText()

        if len(text) != 0:
            return True
        else:
            return False

    def send(self):
        if not self.textIsValid():
            return
        self.textSended.emit(self.toPlainText())
        self.clear()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.send()
            return

        QTextEdit.keyPressEvent(self, event)