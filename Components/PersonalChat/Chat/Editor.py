from PyQt6.QtWidgets import QWidget, QPlainTextEdit
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColorConstants, QFont


class Editor(QPlainTextEdit):
    def __init__(self, parent: QObject = None):
        QPlainTextEdit.__init__(self, parent)

        self.setPlaceholderText("Write a message...")
        self.setFont(QFont("Open Sans", 10))

        self.setMaximumHeight(300)
