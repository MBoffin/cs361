# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

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
        w_MainWindow.setMinimumSize(QSize(640, 480))
        w_MainWindow.setMaximumSize(QSize(640, 480))
        w_MainWindow.setBaseSize(QSize(640, 480))
        w_MainWindow.setWindowTitle(u"Simple Game Library")
        self.centralwidget = QWidget(w_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pnl_pages = QStackedWidget(self.centralwidget)
        self.pnl_pages.setObjectName(u"pnl_pages")
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
        self.lbl_title.setText(u"Simple Game Library")
        self.lbl_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_title)

        self.lbl_subtitle = QLabel(self.intro_page)
        self.lbl_subtitle.setObjectName(u"lbl_subtitle")
        font1 = QFont()
        font1.setPointSize(20)
        self.lbl_subtitle.setFont(font1)
        self.lbl_subtitle.setText(u"Keeping track of your games,\n"
"so you don't have to.")
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
        self.groupBox.setTitle(u"Did you know...")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(32, -1, -1, 16)
        self.lbl_tips = QLabel(self.groupBox)
        self.lbl_tips.setObjectName(u"lbl_tips")
        self.lbl_tips.setText(u"tips text")

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
        self.btn_begin.setText(u"Begin")
        self.btn_begin.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_begin)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pnl_pages.addWidget(self.intro_page)
        self.library_page = QWidget()
        self.library_page.setObjectName(u"library_page")
        self.verticalLayout_3 = QVBoxLayout(self.library_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.library_page)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnHome = QPushButton(self.widget)
        self.btnHome.setObjectName(u"btnHome")
        sizePolicy.setHeightForWidth(self.btnHome.sizePolicy().hasHeightForWidth())
        self.btnHome.setSizePolicy(sizePolicy)
        self.btnHome.setMinimumSize(QSize(72, 72))
        self.btnHome.setMaximumSize(QSize(72, 72))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.btnHome.setFont(font4)
        self.btnHome.setText(u"\ud83c\udfe0\n"
"Home")

        self.horizontalLayout_2.addWidget(self.btnHome)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setPointSize(26)
        font5.setBold(True)
        self.label.setFont(font5)
        self.label.setText(u"Game Library")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QSize(72, 72))
        self.widget_4.setMaximumSize(QSize(72, 72))

        self.horizontalLayout_2.addWidget(self.widget_4)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.library_page)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_add_game = QPushButton(self.widget_2)
        self.btn_add_game.setObjectName(u"btn_add_game")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_add_game.sizePolicy().hasHeightForWidth())
        self.btn_add_game.setSizePolicy(sizePolicy3)
        self.btn_add_game.setFont(font4)
        self.btn_add_game.setStyleSheet(u"QPushButton {\n"
"	padding: 10px;\n"
"}")
        self.btn_add_game.setText(u"\u2795 Add Game")

        self.horizontalLayout_3.addWidget(self.btn_add_game)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.dd_sort_by = QComboBox(self.widget_2)
        self.dd_sort_by.addItem(u"Name")
        self.dd_sort_by.addItem(u"Genre")
        self.dd_sort_by.addItem(u"Year")
        self.dd_sort_by.setObjectName(u"dd_sort_by")
        self.dd_sort_by.setFont(font4)
        self.dd_sort_by.setStyleSheet(u"QComboBox {\n"
"	padding: 10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.dd_sort_by)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.library_page)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sa_games = QScrollArea(self.widget_3)
        self.sa_games.setObjectName(u"sa_games")
        self.sa_games.setWidgetResizable(True)
        self.w_game_grid = QWidget()
        self.w_game_grid.setObjectName(u"w_game_grid")
        self.w_game_grid.setGeometry(QRect(0, 0, 620, 326))
        self.grid_games = QGridLayout(self.w_game_grid)
        self.grid_games.setObjectName(u"grid_games")
        self.sa_games.setWidget(self.w_game_grid)

        self.verticalLayout_4.addWidget(self.sa_games)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.pnl_pages.addWidget(self.library_page)

        self.gridLayout.addWidget(self.pnl_pages, 0, 0, 1, 1)

        w_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(w_MainWindow)

        self.pnl_pages.setCurrentIndex(0)
        self.btn_begin.setDefault(True)


        QMetaObject.connectSlotsByName(w_MainWindow)
    # setupUi

    def retranslateUi(self, w_MainWindow):

        pass
    # retranslateUi

