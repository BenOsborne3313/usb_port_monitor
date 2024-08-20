# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_tabs = QTabWidget(self.centralwidget)
        self.main_tabs.setObjectName(u"main_tabs")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_tabs.sizePolicy().hasHeightForWidth())
        self.main_tabs.setSizePolicy(sizePolicy)
        self.ports_tab = QWidget()
        self.ports_tab.setObjectName(u"ports_tab")
        self.verticalLayout_2 = QVBoxLayout(self.ports_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.clear_button = QPushButton(self.ports_tab)
        self.clear_button.setObjectName(u"clear_button")

        self.verticalLayout_2.addWidget(self.clear_button)

        self.port_list = QListWidget(self.ports_tab)
        self.port_list.setObjectName(u"port_list")

        self.verticalLayout_2.addWidget(self.port_list)

        self.main_tabs.addTab(self.ports_tab, "")
        self.readme_tab = QWidget()
        self.readme_tab.setObjectName(u"readme_tab")
        self.verticalLayout_3 = QVBoxLayout(self.readme_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit = QTextEdit(self.readme_tab)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_3.addWidget(self.textEdit)

        self.main_tabs.addTab(self.readme_tab, "")

        self.verticalLayout.addWidget(self.main_tabs)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.ports_tab), QCoreApplication.translate("MainWindow", u"Ports", None))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.readme_tab), QCoreApplication.translate("MainWindow", u"Readme", None))
    # retranslateUi

