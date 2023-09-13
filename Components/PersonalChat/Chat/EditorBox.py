from PyQt6.QtWidgets import QWidget, QHBoxLayout
from PyQt6.QtCore import QObject, Qt
from PyQt6.QtGui import QColorConstants, QResizeEvent, QKeyEvent, QShortcut, QKeySequence

from .Editor import Editor

class SendButton(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(36, 36)


class EditorBox(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.setFixedHeight(36)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)

        self.editor = Editor(self)

        lay = QHBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(5, 5, 5, 5)
        lay.addWidget(self.editor)

        self.editor.heightChanged.connect(self.normHeight)

        self.setLayout(lay)

    def normHeight(self, h: int):
        if self.height() != h + 10:
            self.setFixedHeight(h + 10)

