from PyQt6.QtWidgets import QWidget, QTextEdit, QFrame, QScrollBar
from PyQt6.QtCore import QObject, Qt, pyqtSignal
from PyQt6.QtGui import QColorConstants, QFont, QResizeEvent, QFontMetrics, QKeyEvent, QShortcut, QKeySequence


class ScrollBar(QScrollBar):
    def __init__(self, parent: QObject = None):
        QScrollBar.__init__(self, parent)
        self.setFixedSize(0,0)


class Editor(QTextEdit):
    heightChanged = pyqtSignal(int)
    def __init__(self, parent: QObject = None):
        QTextEdit.__init__(self, parent)

        self.maxHeight = 12
        self.setPlaceholderText("Write a message...")
        self.setFont(QFont("Open Sans", 10))
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

        if self.height() != h:
            self.setMinimumHeight(h)
            self.heightChanged.emit(h)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if (event.key() == Qt.Key.Key_Return  and event.modifiers() == Qt.KeyboardModifier.ShiftModifier) or event.key() == Qt.Key.Key_Enter:
            print("send")
            return

        QTextEdit.keyPressEvent(self, event)