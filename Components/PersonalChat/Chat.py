from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette, QColor, QResizeEvent


class Chat(QWidget):
    def __init__(self, name: str, parent=None):
        QWidget.__init__(self, parent)
        self.setMinimumSize(300, 300)

        
