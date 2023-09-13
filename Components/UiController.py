from typing import Optional
from enum import Enum

from PyQt6.QtGui import QFont, QColorConstants, QColor
from PyQt6.QtCore import QSize

from .OurChatUi import OurChatUi

Chat: Optional[OurChatUi] = None
DefaultFont: QFont = QFont("Open Sans", 10)
DefaultFontFamily: str = "Open Sans"

DefaultButtonSize: QSize = QSize(25, 25)
DefaultLineHeight: int = 54

MinimumApplicationSize: QSize = QSize(200, 400)

DefaultTextColor: QColor = QColorConstants.Black
SecondTextColor: QColor = QColor(170, 170, 170)
HoverBackgroundColor: QColor = QColor(240, 240, 240)
WA_BackgroundColor: QColor = QColor(255, 100, 100)

Light: QColor = QColor(255, 255, 255)
Gray: QColor = QColor(200, 200, 200)

