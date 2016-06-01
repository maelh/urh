# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogOptions(object):
    def setupUi(self, DialogOptions):
        DialogOptions.setObjectName("DialogOptions")
        DialogOptions.resize(746, 486)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DialogOptions)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(DialogOptions)
        self.tabWidget.setObjectName("tabWidget")
        self.tabInterpretation = QtWidgets.QWidget()
        self.tabInterpretation.setObjectName("tabInterpretation")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabInterpretation)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tabInterpretation)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBoxSymbolTreshold = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxSymbolTreshold.sizePolicy().hasHeightForWidth())
        self.spinBoxSymbolTreshold.setSizePolicy(sizePolicy)
        self.spinBoxSymbolTreshold.setMaximum(50)
        self.spinBoxSymbolTreshold.setObjectName("spinBoxSymbolTreshold")
        self.gridLayout.addWidget(self.spinBoxSymbolTreshold, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lSymbolLength = QtWidgets.QLabel(self.groupBox)
        self.lSymbolLength.setObjectName("lSymbolLength")
        self.gridLayout.addWidget(self.lSymbolLength, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.chkBoxEnableSymbols = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxEnableSymbols.setObjectName("chkBoxEnableSymbols")
        self.gridLayout.addWidget(self.chkBoxEnableSymbols, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.lExplanation = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lExplanation.setFont(font)
        self.lExplanation.setWordWrap(True)
        self.lExplanation.setObjectName("lExplanation")
        self.verticalLayout.addWidget(self.lExplanation)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tabInterpretation, "")
        self.tabView = QtWidgets.QWidget()
        self.tabView.setObjectName("tabView")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabView)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.tabView)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.comboBoxDefaultView = QtWidgets.QComboBox(self.tabView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDefaultView.sizePolicy().hasHeightForWidth())
        self.comboBoxDefaultView.setSizePolicy(sizePolicy)
        self.comboBoxDefaultView.setObjectName("comboBoxDefaultView")
        self.comboBoxDefaultView.addItem("")
        self.comboBoxDefaultView.addItem("")
        self.comboBoxDefaultView.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxDefaultView)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.checkBoxPauseTime = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxPauseTime.setObjectName("checkBoxPauseTime")
        self.verticalLayout_4.addWidget(self.checkBoxPauseTime)
        self.checkBoxFallBackTheme = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxFallBackTheme.setObjectName("checkBoxFallBackTheme")
        self.verticalLayout_4.addWidget(self.checkBoxFallBackTheme)
        spacerItem2 = QtWidgets.QSpacerItem(20, 383, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.tabWidget.addTab(self.tabView, "")
        self.tab_plugins = QtWidgets.QWidget()
        self.tab_plugins.setObjectName("tab_plugins")
        self.tabWidget.addTab(self.tab_plugins, "")
        self.tabDevices = QtWidgets.QWidget()
        self.tabDevices.setObjectName("tabDevices")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabDevices)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidgetDevices = QtWidgets.QListWidget(self.tabDevices)
        self.listWidgetDevices.setObjectName("listWidgetDevices")
        self.gridLayout_3.addWidget(self.listWidgetDevices, 0, 0, 3, 2)
        self.chkBoxDeviceEnabled = QtWidgets.QCheckBox(self.tabDevices)
        self.chkBoxDeviceEnabled.setObjectName("chkBoxDeviceEnabled")
        self.gridLayout_3.addWidget(self.chkBoxDeviceEnabled, 0, 2, 1, 1)
        self.rbNativeBackend = QtWidgets.QRadioButton(self.tabDevices)
        self.rbNativeBackend.setObjectName("rbNativeBackend")
        self.gridLayout_3.addWidget(self.rbNativeBackend, 1, 2, 1, 1)
        self.rbGnuradioBackend = QtWidgets.QRadioButton(self.tabDevices)
        self.rbGnuradioBackend.setObjectName("rbGnuradioBackend")
        self.gridLayout_3.addWidget(self.rbGnuradioBackend, 2, 2, 1, 1)
        self.lSupport = QtWidgets.QLabel(self.tabDevices)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSupport.sizePolicy().hasHeightForWidth())
        self.lSupport.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lSupport.setFont(font)
        self.lSupport.setStyleSheet("color: green")
        self.lSupport.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lSupport.setObjectName("lSupport")
        self.gridLayout_3.addWidget(self.lSupport, 3, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.tabDevices)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 4, 0, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.tabDevices)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)
        self.spinBoxNumSendingRepeats = QtWidgets.QSpinBox(self.tabDevices)
        self.spinBoxNumSendingRepeats.setProperty("showGroupSeparator", False)
        self.spinBoxNumSendingRepeats.setMaximum(999999999)
        self.spinBoxNumSendingRepeats.setDisplayIntegerBase(10)
        self.spinBoxNumSendingRepeats.setObjectName("spinBoxNumSendingRepeats")
        self.gridLayout_3.addWidget(self.spinBoxNumSendingRepeats, 5, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tabDevices)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 6, 0, 1, 3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabDevices)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEditPython2Interpreter = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditPython2Interpreter.setObjectName("lineEditPython2Interpreter")
        self.gridLayout_2.addWidget(self.lineEditPython2Interpreter, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 2)
        self.lGnuradioInstalled = QtWidgets.QLabel(self.groupBox_3)
        self.lGnuradioInstalled.setStyleSheet("")
        self.lGnuradioInstalled.setObjectName("lGnuradioInstalled")
        self.gridLayout_2.addWidget(self.lGnuradioInstalled, 2, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox_3, 7, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 8, 1, 1, 1)
        self.tabWidget.addTab(self.tabDevices, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(DialogOptions)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(DialogOptions)

    def retranslateUi(self, DialogOptions):
        _translate = QtCore.QCoreApplication.translate
        DialogOptions.setWindowTitle(_translate("DialogOptions", "Options"))
        self.groupBox.setTitle(_translate("DialogOptions", "Symbols"))
        self.label.setText(_translate("DialogOptions", "Some protocols use different information lengths. This can be part of the protocol logic (e.g. to indicate a SOF). You can set a tolerance window for the selected bit length, outside the window a new symbol will be created."))
        self.label_2.setText(_translate("DialogOptions", "Tolerance window:"))
        self.spinBoxSymbolTreshold.setSuffix(_translate("DialogOptions", "%"))
        self.label_3.setText(_translate("DialogOptions", "of selected bit length"))
        self.label_4.setText(_translate("DialogOptions", "Relative symbol length:"))
        self.lSymbolLength.setText(_translate("DialogOptions", "0%"))
        self.label_6.setText(_translate("DialogOptions", "of selected bit length"))
        self.chkBoxEnableSymbols.setText(_translate("DialogOptions", "Enable symbols"))
        self.lExplanation.setText(_translate("DialogOptions", "No Symbols will be created"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInterpretation), _translate("DialogOptions", "Interpretation"))
        self.label_7.setText(_translate("DialogOptions", "Default View:"))
        self.comboBoxDefaultView.setItemText(0, _translate("DialogOptions", "Bit"))
        self.comboBoxDefaultView.setItemText(1, _translate("DialogOptions", "Hex"))
        self.comboBoxDefaultView.setItemText(2, _translate("DialogOptions", "ASCII"))
        self.checkBoxPauseTime.setText(_translate("DialogOptions", "Show pauses as time"))
        self.checkBoxFallBackTheme.setToolTip(_translate("DialogOptions", "Tick this option if you experience problems with you current Qt theme like no colors in table headers."))
        self.checkBoxFallBackTheme.setText(_translate("DialogOptions", "Use fallback application theme (fusion)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabView), _translate("DialogOptions", "View"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_plugins), _translate("DialogOptions", "Plugins"))
        self.chkBoxDeviceEnabled.setText(_translate("DialogOptions", "Enabled"))
        self.rbNativeBackend.setText(_translate("DialogOptions", "Native backend (recommended)"))
        self.rbGnuradioBackend.setText(_translate("DialogOptions", "Gnuradio backend"))
        self.lSupport.setText(_translate("DialogOptions", "device supports sending and receiving"))
        self.label_8.setText(_translate("DialogOptions", "Default sending repititions:"))
        self.spinBoxNumSendingRepeats.setSpecialValueText(_translate("DialogOptions", "Infinite"))
        self.groupBox_3.setTitle(_translate("DialogOptions", "Gnuradio options"))
        self.label_10.setText(_translate("DialogOptions", "Python2 interpreter:"))
        self.label_11.setText(_translate("DialogOptions", "Needed for Gnuradio backend only"))
        self.lGnuradioInstalled.setText(_translate("DialogOptions", "Gnuradio installation found"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDevices), _translate("DialogOptions", "Device"))

