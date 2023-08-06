from PyQt6.QtWidgets import QWidget, QPlainTextEdit, QFrame
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColorConstants, QFont


class Editor(QPlainTextEdit):
    def __init__(self, parent: QObject = None):
        QPlainTextEdit.__init__(self, parent)

        self.setPlaceholderText("Write a message...")
        self.setFont(QFont("Open Sans", 10))
        self.resize(self.width(), self.)
        self.setMaximumHeight(300)
        self.setFrameShape(QFrame.Shape.NoFrame)

