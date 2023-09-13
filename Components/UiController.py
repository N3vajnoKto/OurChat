from typing import Optional

from PyQt6.QtGui import QFont, QColorConstants, QColor
from PyQt6.QtCore import QSize

from .OurChatUi import OurChatUi

Chat: Optional[OurChatUi] = None
DefaultFont: QFont = QFont("Open Sans", 10)
DefaultFontFamily: str = "Open Sans"
DefaultTextColor: QColor = QColorConstants.Black
SecondTextColor: QColor = QColor(170, 170, 170)
HoverBackgroundColor: QColor = QColor(240, 240, 240)

DefaultButtonSize: QSize = QSize(25, 25)
DefaultLineHeight: int = 54

