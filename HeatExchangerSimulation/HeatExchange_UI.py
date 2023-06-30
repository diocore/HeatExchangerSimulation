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
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(840, 983)
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
        self.tab.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.evaporator_label = QLabel(self.frame)
        self.evaporator_label.setObjectName(u"evaporator_label")
        self.evaporator_label.setMinimumSize(QSize(200, 0))
        font1 = QFont()
        font1.setBold(False)
        self.evaporator_label.setFont(font1)
        self.evaporator_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.evaporator_label)

        self.evaporator_temperature = QLineEdit(self.frame)
        self.evaporator_temperature.setObjectName(u"evaporator_temperature")
        self.evaporator_temperature.setFont(font1)

        self.horizontalLayout.addWidget(self.evaporator_temperature)

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
        self.desorber_label = QLabel(self.frame_3)
        self.desorber_label.setObjectName(u"desorber_label")
        self.desorber_label.setMinimumSize(QSize(200, 0))
        self.desorber_label.setFont(font1)
        self.desorber_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.desorber_label)

        self.desorber_temperature = QLineEdit(self.frame_3)
        self.desorber_temperature.setObjectName(u"desorber_temperature")
        self.desorber_temperature.setFont(font1)

        self.horizontalLayout_2.addWidget(self.desorber_temperature)

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
        self.condenser_label = QLabel(self.frame_4)
        self.condenser_label.setObjectName(u"condenser_label")
        self.condenser_label.setMinimumSize(QSize(200, 0))
        self.condenser_label.setFont(font1)
        self.condenser_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.condenser_label)

        self.condenser_temperature = QLineEdit(self.frame_4)
        self.condenser_temperature.setObjectName(u"condenser_temperature")
        self.condenser_temperature.setFont(font1)

        self.horizontalLayout_3.addWidget(self.condenser_temperature)

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
        self.absorber_label = QLabel(self.frame_5)
        self.absorber_label.setObjectName(u"absorber_label")
        self.absorber_label.setMinimumSize(QSize(200, 0))
        self.absorber_label.setFont(font1)
        self.absorber_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.absorber_label)

        self.absorber_temperature = QLineEdit(self.frame_5)
        self.absorber_temperature.setObjectName(u"absorber_temperature")
        self.absorber_temperature.setFont(font1)

        self.horizontalLayout_4.addWidget(self.absorber_temperature)

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
        self.volumetric_flow_rate_label = QLabel(self.frame_6)
        self.volumetric_flow_rate_label.setObjectName(u"volumetric_flow_rate_label")
        self.volumetric_flow_rate_label.setMinimumSize(QSize(200, 0))
        self.volumetric_flow_rate_label.setFont(font1)
        self.volumetric_flow_rate_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.volumetric_flow_rate_label)

        self.volumetric_flow_rate = QLineEdit(self.frame_6)
        self.volumetric_flow_rate.setObjectName(u"volumetric_flow_rate")
        self.volumetric_flow_rate.setFont(font1)

        self.horizontalLayout_5.addWidget(self.volumetric_flow_rate)

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
        self.coolan_label = QLabel(self.frame_7)
        self.coolan_label.setObjectName(u"coolan_label")
        self.coolan_label.setMinimumSize(QSize(200, 0))
        self.coolan_label.setFont(font1)
        self.coolan_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.coolan_label)

        self.coolant_var = QLineEdit(self.frame_7)
        self.coolant_var.setObjectName(u"coolant_var")
        self.coolant_var.setFont(font1)

        self.horizontalLayout_6.addWidget(self.coolant_var)

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

        self.simulateButton = QPushButton(Form)
        self.simulateButton.setObjectName(u"simulateButton")

        self.verticalLayout.addWidget(self.simulateButton)

        self.tabWidget_2 = QTabWidget(Form)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_5.sizePolicy().hasHeightForWidth())
        self.tab_5.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.layoutPlot_01 = QVBoxLayout()
        self.layoutPlot_01.setObjectName(u"layoutPlot_01")

        self.verticalLayout_5.addLayout(self.layoutPlot_01)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.tabWidget_2)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.evaporator_label.setText(QCoreApplication.translate("Form", u"Evaporator", None))
        self.evaporator_temperature.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.desorber_label.setText(QCoreApplication.translate("Form", u"Desorber", None))
        self.desorber_temperature.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_8.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.condenser_label.setText(QCoreApplication.translate("Form", u"Condenser", None))
        self.condenser_temperature.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_12.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.absorber_label.setText(QCoreApplication.translate("Form", u"Absorber", None))
        self.absorber_temperature.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_14.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.volumetric_flow_rate_label.setText(QCoreApplication.translate("Form", u"Volumetric flow rate", None))
        self.volumetric_flow_rate.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_15.setText(QCoreApplication.translate("Form", u"m^3/s", None))
        self.coolan_label.setText(QCoreApplication.translate("Form", u"Coolant", None))
        self.coolant_var.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_16.setText("")
        self.variable_17.setText(QCoreApplication.translate("Form", u"Variable", None))
        self.variable_lineEdit_17.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_17.setText(QCoreApplication.translate("Form", u"unit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Config", None))
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
        self.simulateButton.setText(QCoreApplication.translate("Form", u"Simulate", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Tab 1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("Form", u"Tab 2", None))
    # retranslateUi


