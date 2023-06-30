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
        Form.resize(770, 983)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
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
        self.evaporator_temperature.setFrame(True)
        self.evaporator_temperature.setAlignment(Qt.AlignCenter)

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
        self.desorber_temperature.setAlignment(Qt.AlignCenter)

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
        self.condenser_temperature.setAlignment(Qt.AlignCenter)

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
        self.absorber_temperature.setAlignment(Qt.AlignCenter)

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

        self.mass_flow_rate_coolant = QLineEdit(self.frame_6)
        self.mass_flow_rate_coolant.setObjectName(u"mass_flow_rate_coolant")
        self.mass_flow_rate_coolant.setFont(font1)
        self.mass_flow_rate_coolant.setLayoutDirection(Qt.LeftToRight)
        self.mass_flow_rate_coolant.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.mass_flow_rate_coolant)

        self.variable_unit_15 = QLabel(self.frame_6)
        self.variable_unit_15.setObjectName(u"variable_unit_15")
        self.variable_unit_15.setMinimumSize(QSize(50, 0))
        self.variable_unit_15.setFont(font1)

        self.horizontalLayout_5.addWidget(self.variable_unit_15)


        self.verticalLayout_2.addWidget(self.frame_6)

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

        self.mass_flow_rate_solvent = QLineEdit(self.frame_8)
        self.mass_flow_rate_solvent.setObjectName(u"mass_flow_rate_solvent")
        self.mass_flow_rate_solvent.setFont(font1)
        self.mass_flow_rate_solvent.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.mass_flow_rate_solvent)

        self.variable_unit_17 = QLabel(self.frame_8)
        self.variable_unit_17.setObjectName(u"variable_unit_17")
        self.variable_unit_17.setMinimumSize(QSize(50, 0))
        self.variable_unit_17.setFont(font1)

        self.horizontalLayout_7.addWidget(self.variable_unit_17)


        self.verticalLayout_2.addWidget(self.frame_8)

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
        self.coolant_var.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.coolant_var)

        self.variable_unit_16 = QLabel(self.frame_7)
        self.variable_unit_16.setObjectName(u"variable_unit_16")
        self.variable_unit_16.setMinimumSize(QSize(50, 0))
        self.variable_unit_16.setFont(font1)

        self.horizontalLayout_6.addWidget(self.variable_unit_16)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.simulateButton = QPushButton(Form)
        self.simulateButton.setObjectName(u"simulateButton")

        self.verticalLayout.addWidget(self.simulateButton)

        self.asd = QTabWidget(Form)
        self.asd.setObjectName(u"asd")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.textEditValues = QTextEdit(self.tab_7)
        self.textEditValues.setObjectName(u"textEditValues")
        self.textEditValues.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"MS Gothic"])
        font2.setPointSize(45)
        font2.setBold(True)
        self.textEditValues.setFont(font2)
        self.textEditValues.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.textEditValues)

        self.asd.addTab(self.tab_7, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_5.sizePolicy().hasHeightForWidth())
        self.tab_5.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.LayoutEvaporatorPlot = QVBoxLayout()
        self.LayoutEvaporatorPlot.setObjectName(u"LayoutEvaporatorPlot")

        self.verticalLayout_5.addLayout(self.LayoutEvaporatorPlot)

        self.asd.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_16 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.LayoutCondenserPlot = QVBoxLayout()
        self.LayoutCondenserPlot.setObjectName(u"LayoutCondenserPlot")

        self.horizontalLayout_16.addLayout(self.LayoutCondenserPlot)

        self.asd.addTab(self.tab_6, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_7 = QVBoxLayout(self.tab_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.LayoutDesorberPlot = QVBoxLayout()
        self.LayoutDesorberPlot.setObjectName(u"LayoutDesorberPlot")

        self.verticalLayout_7.addLayout(self.LayoutDesorberPlot)

        self.asd.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_9 = QVBoxLayout(self.tab_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.LayoutAbsorberPlot = QVBoxLayout()
        self.LayoutAbsorberPlot.setObjectName(u"LayoutAbsorberPlot")

        self.verticalLayout_9.addLayout(self.LayoutAbsorberPlot)

        self.asd.addTab(self.tab_9, "")

        self.verticalLayout.addWidget(self.asd)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.asd.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.evaporator_label.setText(QCoreApplication.translate("Form", u"Evaporator", None))
        self.evaporator_temperature.setText(QCoreApplication.translate("Form", u"-40", None))
        self.evaporator_temperature.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.desorber_label.setText(QCoreApplication.translate("Form", u"Desorber", None))
        self.desorber_temperature.setText(QCoreApplication.translate("Form", u" 60", None))
        self.desorber_temperature.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_8.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.condenser_label.setText(QCoreApplication.translate("Form", u"Condenser", None))
        self.condenser_temperature.setText(QCoreApplication.translate("Form", u"10", None))
        self.condenser_temperature.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_12.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.absorber_label.setText(QCoreApplication.translate("Form", u"Absorber", None))
        self.absorber_temperature.setText(QCoreApplication.translate("Form", u"30", None))
        self.absorber_temperature.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_14.setText(QCoreApplication.translate("Form", u"\u00b0C", None))
        self.volumetric_flow_rate_label.setText(QCoreApplication.translate("Form", u"Mass flow rate coolant", None))
        self.mass_flow_rate_coolant.setText(QCoreApplication.translate("Form", u"0.2", None))
        self.mass_flow_rate_coolant.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_15.setText(QCoreApplication.translate("Form", u"kg/s", None))
        self.variable_17.setText(QCoreApplication.translate("Form", u"Mass flow rate solvent", None))
        self.mass_flow_rate_solvent.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.mass_flow_rate_solvent.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_17.setText(QCoreApplication.translate("Form", u"kg/s", None))
        self.coolan_label.setText(QCoreApplication.translate("Form", u"Coolant", None))
        self.coolant_var.setText(QCoreApplication.translate("Form", u"NH3", None))
        self.coolant_var.setPlaceholderText(QCoreApplication.translate("Form", u"insert value", None))
        self.variable_unit_16.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Config", None))
        self.simulateButton.setText(QCoreApplication.translate("Form", u"Simulate", None))
        self.textEditValues.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Gothic'; font-size:45pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:20pt; font-weight:400;\">Output</span></p></body></html>", None))
        self.asd.setTabText(self.asd.indexOf(self.tab_7), QCoreApplication.translate("Form", u"Values", None))
        self.asd.setTabText(self.asd.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Evaporator", None))
        self.asd.setTabText(self.asd.indexOf(self.tab_6), QCoreApplication.translate("Form", u"Condenser", None))
        self.asd.setTabText(self.asd.indexOf(self.tab_8), QCoreApplication.translate("Form", u"Desorber", None))
        self.asd.setTabText(self.asd.indexOf(self.tab_9), QCoreApplication.translate("Form", u"Absorber", None))
    # retranslateUi

