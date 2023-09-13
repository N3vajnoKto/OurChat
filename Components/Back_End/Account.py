from typing import Optional
from random import randint

from PyQt6.QtGui import QImage, QColor

class Account:
    def __init__(self):
        self.__name = "Девушка Рядом С Кириллом"
        self.__nickname = "DaryaGnedko"
        self.__avatar: Optional[QImage] = None
        self.__backgroundColor: QColor = QColor.fromHsv(randint(0, 359), randint(200, 255), randint(220, 240))

    def nickname(self) -> str:
        return self.__nickname

    def name(self) -> str:
        return self.__name

    def hasAvatar(self) -> bool:
        return self.avatar is not None

    def avatar(self) -> QImage:
        return self.__avatar

    def backgroundColor(self) -> QColor:
        return self.__backgroundColor

EmptyAccount = Account()