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
HoverBackgroundColor: QColor = QColor(230, 238, 255)
WA_BackgroundColor: QColor = QColor(255, 100, 100)

ThemeColor: QColor = QColor(120, 127, 180)
LightThemColor: QColor = QColor(180, 191, 255)
DimThemeColor: QColor = QColor(96, 102, 144)
DarkThemeColor: QColor = QColor(72, 76, 108)
Light: QColor = QColor(255, 255, 255)
Gray: QColor = QColor(200, 200, 200)
LightGray: QColor = QColor(240, 240, 240)


