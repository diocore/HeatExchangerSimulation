# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HeatExchange.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 863)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.variable = QLabel(self.frame)
        self.variable.setObjectName(u"variable")
        self.variable.setMinimumSize(QSize(200, 0))
        font1 = QFont()
        font1.setBold(False)
        self.variable.setFont(font1)
        self.variable.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.variable)

        self.variable_lineEdit = QLineEdit(self.frame)
        self.variable_lineEdit.setObjectName(u"variable_lineEdit")
        self.variable_lineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.variable_lineEdit)

        self.variable_unit = QLabel(self.frame)
        self.variable_unit.setObjectName(u"variable_unit")
        self.variable_unit.setMinimumSize(QSize(50, 0))
        self.variable_unit.setFont(font1)

        self.horizontalLayout.addWidget(self.variable_unit)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.variable_8 = QLabel(self.frame_3)
        self.variable_8.setObjectName(u"variable_8")
        self.variable_8.setMinimumSize(QSize(200, 0))
        self.variable_8.setFont(font1)
        self.variable_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.variable_8)

        self.variable_lineEdit_8 = QLineEdit(self.frame_3)
        self.variable_lineEdit_8.setObjectName(u"variable_lineEdit_8")
        self.variable_lineEdit_8.setFont(font1)

        self.horizontalLayout_2.addWidget(self.variable_lineEdit_8)

        self.variable_unit_8 = QLabel(self.frame_3)
        self.variable_unit_8.setObjectName(u"variable_unit_8")
        self.variable_unit_8.setMinimumSize(QSize(50, 0))
        self.variable_unit_8.setFont(font1)

        self.horizontalLayout_2.addWidget(self.variable_unit_8)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.variable_12 = QLabel(self.frame_4)
        self.variable_12.setObjectName(u"variable_12")
        self.variable_12.setMinimumSize(QSize(200, 0))
        self.variable_12.setFont(font1)
        self.variable_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.variable_12)

        self.variable_lineEdit_12 = QLineEdit(self.frame_4)
        self.variable_lineEdit_12.setObjectName(u"variable_lineEdit_12")
        self.variable_lineEdit_12.setFont(font1)

        self.horizontalLayout_3.addWidget(self.variable_lineEdit_12)

        self.variable_unit_12 = QLabel(self.frame_4)
        self.variable_unit_12.setObjectName(u"variable_unit_12")
        self.variable_unit_12.setMinimumSize(QSize(50, 0))
        self.variable_unit_12.setFont(font1)

        self.horizontalLayout_3.addWidget(self.variable_unit_12)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.variable_14 = QLabel(self.frame_5)
        self.variable_14.setObjectName(u"variable_14")
        self.variable_14.setMinimumSize(QSize(200, 0))
        self.variable_14.setFont(font1)
        self.variable_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.variable_14)

        self.variable_lineEdit_14 = QLineEdit(self.frame_5)
        self.variable_lineEdit_14.setObjectName(u"variable_lineEdit_14")
        self.variable_lineEdit_14.setFont(font1)

        self.horizontalLayout_4.addWidget(self.variable_lineEdit_14)

        self.variable_unit_14 = QLabel(self.frame_5)
        self.variable_unit_14.setObjectName(u"variable_unit_14")
        self.variable_unit_14.setMinimumSize(QSize(50, 0))
        self.variable_unit_14.setFont(font1)

        self.horizontalLayout_4.addWidget(self.variable_unit_14)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.variable_15 = QLabel(self.frame_6)
        self.variable_15.setObjectName(u"variable_15")
        self.variable_15.setMinimumSize(QSize(200, 0))
        self.variable_15.setFont(font1)
        self.variable_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.variable_15)

        self.variable_lineEdit_15 = QLineEdit(self.frame_6)
        self.variable_lineEdit_15.setObjectName(u"variable_lineEdit_15")
        self.variable_lineEdit_15.setFont(font1)

        self.horizontalLayout_5.addWidget(self.variable_lineEdit_15)

        self.variable_unit_15 = QLabel(self.frame_6)
        self.variable_unit_15.setObjectName(u"variable_unit_15")
        self.variable_unit_15.setMinimumSize(QSize(50, 0))
        self.variable_unit_15.setFont(font1)

        self.horizontalLayout_5.addWidget(self.variable_unit_15)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.tab)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.variable_16 = QLabel(self.frame_7)
        self.variable_16.setObjectName(u"variable_16")
        self.variable_16.setMinimumSize(QSize(200, 0))
        self.variable_16.setFont(font1)
        self.variable_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.variable_16)

        self.variable_lineEdit_16 = QLineEdit(self.frame_7)
        self.variable_lineEdit_16.setObjectName(u"variable_lineEdit_16")
        self.variable_lineEdit_16.setFont(font1)

        self.horizontalLayout_6.addWidget(self.variable_lineEdit_16)

        self.variable_unit_16 = QLabel(self.frame_7)
        self.variable_unit_16.setObjectName(u"variable_unit_16")
        self.variable_unit_16.setMinimumSize(QSize(50, 0))
        self.variable_unit_16.setFont(font1)

        self.horizontalLayout_6.addWidget(self.variable_unit_16)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.tab)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 50))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.variable_17 = QLabel(self.frame_8)
        self.variable_17.setObjectName(u"variable_17")
        self.variable_17.setMinimumSize(QSize(200, 0))
        self.variable_17.setFont(font1)
        self.variable_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.variable_17)

        self.variable_lineEdit_17 = QLineEdit(self.frame_8)
        self.variable_lineEdit_17.setObjectName(u"variable_lineEdit_17")
        self.variable_lineEdit_17.setFont(font1)

        self.horizontalLayout_7.addWidget(self.variable_lineEdit_17)

        self.variable_unit_17 = QLabel(self.frame_8)
        self.variable_unit_17.setObjectName(u"variable_unit_17")
        self.variable_unit_17.setMinimumSize(QSize(50, 0))
        self.variable_unit_17.setFont(font1)

        self.horizontalLayout_7.addWidget(self.variable_unit_17)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(self.tab_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setFont(font1)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.variable_18 = QLabel(self.frame_9)
        self.variable_18.setObjectName(u"variable_18")
        self.variable_18.setMinimumSize(QSize(200, 0))
        self.variable_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.variable_18)

        self.variable_lineEdit_18 = QLineEdit(self.frame_9)
        self.variable_lineEdit_18.setObjectName(u"variable_lineEdit_18")

        self.horizontalLayout_8.addWidget(self.variable_lineEdit_18)

        self.variable_unit_18 = QLabel(self.frame_9)
        self.variable_unit_18.setObjectName(u"variable_unit_18")
        self.variable_unit_18.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_8.addWidget(self.variable_unit_18)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.tab_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 50))
        self.frame_10.setFont(font1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.variable_19 = QLabel(self.frame_10)
        self.variable_19.setObjectName(u"variable_19")
        self.variable_19.setMinimumSize(QSize(200, 0))
        self.variable_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.variable_19)

        self.variable_lineEdit_19 = QLineEdit(self.frame_10)
        self.variable_lineEdit_19.setObjectName(u"variable_lineEdit_19")

        self.horizontalLayout_9.addWidget(self.variable_lineEdit_19)

        self.variable_unit_19 = QLabel(self.frame_10)
        self.variable_unit_19.setObjectName(u"variable_unit_19")
        self.variable_unit_19.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_9.addWidget(self.variable_unit_19)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_14 = QFrame(self.tab_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 50))
        self.frame_14.setFont(font1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.variable_23 = QLabel(self.frame_14)
        self.variable_23.setObjectName(u"variable_23")
        self.variable_23.setMinimumSize(QSize(200, 0))
        self.variable_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.variable_23)

        self.variable_lineEdit_23 = QLineEdit(self.frame_14)
        self.variable_lineEdit_23.setObjectName(u"variable_lineEdit_23")

        self.horizontalLayout_13.addWidget(self.variable_lineEdit_23)

        self.variable_unit_23 = QLabel(self.frame_14)
        self.variable_unit_23.setObjectName(u"variable_unit_23")
        self.variable_unit_23.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_13.addWidget(self.variable_unit_23)


        self.verticalLayout_3.addWidget(self.frame_14)

        self.frame_11 = QFrame(self.tab_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 50))
        self.frame_11.setFont(font1)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.variable_20 = QLabel(self.frame_11)
        self.variable_20.setObjectName(u"variable_20")
        self.variable_20.setMinimumSize(QSize(200, 0))
        self.variable_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.variable_20)

        self.variable_lineEdit_20 = QLineEdit(self.frame_11)
        self.variable_lineEdit_20.setObjectName(u"variable_lineEdit_20")

        self.horizontalLayout_10.addWidget(self.variable_lineEdit_20)

        self.variable_unit_20 = QLabel(self.frame_11)
        self.variable_unit_20.setObjectName(u"variable_unit_20")
        self.variable_unit_20.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_10.addWidget(self.variable_unit_20)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.tab_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 50))
        self.frame_13.setFont(font1)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.variable_22 = QLabel(self.frame_13)
        self.variable_22.setObjectName(u"variable_22")
        self.variable_22.setMinimumSize(QSize(200, 0))
        self.variable_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.variable_22)

        self.variable_lineEdit_22 = QLineEdit(self.frame_13)
        self.variable_lineEdit_22.setObjectName(u"variable_lineEdit_22")

        self.horizontalLayout_12.addWidget(self.variable_lineEdit_22)

        self.variable_unit_22 = QLabel(self.frame_13)
        self.variable_unit_22.setObjectName(u"variable_unit_22")
        self.variable_unit_22.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_12.addWidget(self.variable_unit_22)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.tab_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 50))
        self.frame_15.setFont(font1)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.variable_24 = QLabel(self.frame_15)
        self.variable_24.setObjectName(u"variable_24")
        self.variable_24.setMinimumSize(QSize(200, 0))
        self.variable_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.variable_24)

        self.variable_lineEdit_24 = QLineEdit(self.frame_15)
        self.variable_lineEdit_24.setObjectName(u"variable_lineEdit_24")

        self.horizontalLayout_14.addWidget(self.variable_lineEdit_24)

        self.variable_unit_24 = QLabel(self.frame_15)
        self.variable_unit_24.setObjectName(u"variable_unit_24")
        self.variable_unit_24.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_14.addWidget(self.variable_unit_24)


        self.verticalLayout_3.addWidget(self.frame_15)

        self.frame_12 = QFrame(self.tab_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setFont(font1)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.variable_21 = QLabel(self.frame_12)
        self.variable_21.setObjectName(u"variable_21")
        self.variable_21.setMinimumSize(QSize(200, 0))
        self.variable_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.variable_21)

        self.variable_lineEdit_21 = QLineEdit(self.frame_12)
        self.variable_lineEdit_21.setObjectName(u"variable_lineEdit_21")

        self.horizontalLayout_11.addWidget(self.variable_lineEdit_21)

        self.variable_unit_21 = QLabel(self.frame_12)
        self.variable_unit_21.setObjectName(u"variable_unit_21")
        self.variable_unit_21.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_11.addWidget(self.variable_unit_21)


        self.verticalLayout_3.addWidget(self.frame_12)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)

        self.verticalLayout.addWidget(self.textEdit)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.variable.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_8.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_8.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_8.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_12.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_12.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_12.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_14.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_14.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_14.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_15.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_15.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_15.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_16.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_16.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_16.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_17.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_17.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_17.setText(QCoreApplication.translate("Form", u"unit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Absorber", None))
        self.variable_18.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_18.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_18.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_19.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_19.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_19.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_23.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_23.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_23.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_20.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_20.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_20.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_22.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_22.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_22.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_24.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_24.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_24.setText(QCoreApplication.translate("Form", u"unit", None))
        self.variable_21.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_21.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_21.setText(QCoreApplication.translate("Form", u"unit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Desorber", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Condenser", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Evaporator", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Simulate", None))
    # retranslateUi

