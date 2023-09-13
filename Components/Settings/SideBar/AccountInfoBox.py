from typing import Optional

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QHBoxLayout
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QEvent
from PyQt6.QtGui import QEnterEvent, QPalette, QColor, QColorConstants, QResizeEvent, QMouseEvent, QIcon, QFont

from ...Boxes.VerticalScrollArea import VerticalScrollArea
from ...Boxes.ButtonBox import ButtonBox
from ...Boxes.VListWidget import VListWidget
from ...Boxes.Avatar import Avatar
from ...Boxes.TextLine import TextLine
from ...Boxes.VWidget import VWidget
from ...Back_End.Account import Account
from ... import UiController
from ...Boxes.VerticalScrollArea import VerticalScrollArea

from ...Back_End import ApplicationController
from ...Boxes.IconWidget import IconWidget

class addNewAccountButton(ButtonBox, VWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        VWidget.__init__(self)
        ButtonBox.__init__(self)
        self.setParent(parent)
        lay = QHBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        iconlay = QGridLayout(self)
        self.icon = IconWidget(QIcon("Components/Resources/Icons/plus-in-circle.svg"), self)

        iconlay.addWidget(self.icon)
        iconlay.setContentsMargins(13, 5, 13, 5)

        self.icon.setFixedSize(UiController.DefaultButtonSize)

        self.label = TextLine("Add new account")
        self.label.setFont(QFont(UiController.DefaultFontFamily, 10, QFont.Weight.Medium))
        lay.addLayout(iconlay)
        lay.addWidget(self.label)

        lay.setSpacing(0)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), UiController.HoverBackgroundColor)
        self.setPalette(pal)

    def leaveEvent(self, event: QEvent) -> None:
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)


class AccountPreview(ButtonBox, VWidget):
    def __init__(self, acc: Optional[Account], parent: Optional[QWidget] = None):
        VWidget.__init__(self)
        ButtonBox.__init__(self)

        self.setAttribute(Qt.WidgetAttribute.WA_Hover)
        self.setParent(parent)
        self.account: Optional[Account] = acc

        self.backColor: QColor = QColorConstants.White

        mainLay = QHBoxLayout(self)

        mainLay.setSpacing(0)
        mainLay.setContentsMargins(0, 0, 0, 0)

        self.avatar = Avatar(acc, self)
        self.avatar.setFixedSize(40, 40)

        lay = QGridLayout()
        lay.setSpacing(0)
        lay.setContentsMargins(5, 0, 5, 0)
        lay.addWidget(self.avatar)
        mainLay.addLayout(lay)

        self.name = TextLine(acc.name(), self)
        self.nickname = TextLine(acc.nickname(), self)

        pal = self.nickname.palette()
        pal.setColor(self.nickname.foregroundRole(), UiController.SecondTextColor)
        self.nickname.setPalette(pal)

        infoLay = QVBoxLayout(self)
        infoLay.setSpacing(0)
        infoLay.setContentsMargins(0, 10, 0, 10)
        infoLay.addWidget(self.name)
        infoLay.addWidget(self.nickname)

        mainLay.addLayout(infoLay)

        self.setLayout(mainLay)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), self.backColor)
        self.setPalette(pal)

    def getAccount(self) -> Account:
        return self.account

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), UiController.HoverBackgroundColor)
        self.setPalette(pal)

    def leaveEvent(self, event: QEvent) -> None:
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)


class AccountList(VListWidget):
    def __init__(self, parent: QObject | None = None):
        VListWidget.__init__(self, parent)
        self.accountList: list[Account] = []
        self.accountPreviews: list[AccountPreview] = []

    def setAccountList(self, lst: list[Account]):
        for preview in self.accountPreviews:
            del preview
        self.accountList = lst
        for acc in lst:
            self.addAccount(acc)

    def addAccount(self, acc: Account):
        self.accountList.append(acc)
        button = AccountPreview(acc, self)
        button.setFixedHeight(54)
        self.accountPreviews.append(button)

        VListWidget.addWidget(self, button)

    def insertAccount(self, index: int, acc: Account):
        self.accountList.insert(index, acc)
        button = AccountPreview(acc, self)
        button.setFixedHeight(54)
        self.accountPreviews.insert(index, button)

        VListWidget.insertWidget(self, index, button)

    def removeAccount(self, acc: Account):
        self.accountList.remove(acc)

        for button in self.accountPreviews:
            if button.getAccount() is acc:
                self.accountPreviews.remove(button)
                break

        self.updateHeight()


class AccountInfoBox(Avatar):
    def __init__(self, parent: QObject | None = None):
        Avatar.__init__(self, ApplicationController.Application.currentAccount(), parent)

        self.setForm(Avatar.AvatarForm.Rectangle)

        self.accountListOpenButton = ButtonBox(self)

        self.name = TextLine(ApplicationController.Application.currentAccount().name(), self.accountListOpenButton)
        self.name.setFont(QFont(UiController.DefaultFontFamily, 11, QFont.Weight.Medium))

        pal = self.name.palette()
        pal.setColor(self.name.foregroundRole(), QColorConstants.White)
        self.name.setPalette(pal)

        self.iconBox = QWidget(self.accountListOpenButton)
        self.icon = IconWidget(QIcon("Components/Resources/Icons/white_up.svg"), self.iconBox)
        self.icon.setFixedSize(UiController.DefaultButtonSize)

        lay = QGridLayout(self.iconBox)
        lay.addWidget(self.icon)

        self.iconBox.setLayout(lay)

        lay = QHBoxLayout(self.accountListOpenButton)
        lay.setSpacing(0)
        lay.setContentsMargins(5, 0, 0, 0)
        lay.addWidget(self.name)
        lay.addWidget(self.iconBox)

        self.accountListOpenButton.setLayout(lay)

        self.accountListOpenButton.setFixedHeight(UiController.DefaultLineHeight)
        self.iconBox.setFixedSize(self.accountListOpenButton.height(), self.accountListOpenButton.height())


    def resizeEvent(self, event: QResizeEvent) -> None:
        self.accountListOpenButton.resize(event.size().width(), self.accountListOpenButton.height())
        self.accountListOpenButton.move(0, self.height() - self.accountListOpenButton.height())
        Avatar.resizeEvent(self, event)

