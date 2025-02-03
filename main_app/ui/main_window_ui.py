# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_w_MainWindow(object):
    def setupUi(self, w_MainWindow):
        if not w_MainWindow.objectName():
            w_MainWindow.setObjectName(u"w_MainWindow")
        w_MainWindow.resize(640, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(w_MainWindow.sizePolicy().hasHeightForWidth())
        w_MainWindow.setSizePolicy(sizePolicy)
        w_MainWindow.setBaseSize(QSize(640, 480))
        self.centralwidget = QWidget(w_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.intro_page = QWidget()
        self.intro_page.setObjectName(u"intro_page")
        self.verticalLayout = QVBoxLayout(self.intro_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_title = QLabel(self.intro_page)
        self.lbl_title.setObjectName(u"lbl_title")
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_title)

        self.lbl_subtitle = QLabel(self.intro_page)
        self.lbl_subtitle.setObjectName(u"lbl_subtitle")
        font1 = QFont()
        font1.setPointSize(20)
        self.lbl_subtitle.setFont(font1)
        self.lbl_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_subtitle)

        self.groupBox = QGroupBox(self.intro_page)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.groupBox.setFont(font2)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(32, -1, -1, 16)
        self.lbl_tips = QLabel(self.groupBox)
        self.lbl_tips.setObjectName(u"lbl_tips")

        self.verticalLayout_2.addWidget(self.lbl_tips)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_begin = QPushButton(self.intro_page)
        self.btn_begin.setObjectName(u"btn_begin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_begin.sizePolicy().hasHeightForWidth())
        self.btn_begin.setSizePolicy(sizePolicy2)
        self.btn_begin.setMinimumSize(QSize(200, 0))
        self.btn_begin.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.btn_begin.setFont(font3)
        self.btn_begin.setAutoFillBackground(False)
        self.btn_begin.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_begin)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.intro_page)
        self.library_page = QWidget()
        self.library_page.setObjectName(u"library_page")
        self.stackedWidget.addWidget(self.library_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        w_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(w_MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.btn_begin.setDefault(True)


        QMetaObject.connectSlotsByName(w_MainWindow)
    # setupUi

    def retranslateUi(self, w_MainWindow):
        w_MainWindow.setWindowTitle(QCoreApplication.translate("w_MainWindow", u"Simple Game Library", None))
        self.lbl_title.setText(QCoreApplication.translate("w_MainWindow", u"Simple Game Library", None))
        self.lbl_subtitle.setText(QCoreApplication.translate("w_MainWindow", u"Keeping track of your games\n"
"so you don't have to.", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_MainWindow", u"Did you know...", None))
        self.lbl_tips.setText(QCoreApplication.translate("w_MainWindow", u"tips text", None))
        self.btn_begin.setText(QCoreApplication.translate("w_MainWindow", u"Begin", None))
    # retranslateUi

