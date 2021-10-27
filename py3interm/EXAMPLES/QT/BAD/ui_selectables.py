#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectables.ui'
#
# Created: Wed Jun 12 13:29:37 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Selectables(object):
    def setupUi(self, Selectables):
        Selectables.setObjectName(_fromUtf8("Selectables"))
        Selectables.resize(149, 215)
        self.centralwidget = QtGui.QWidget(Selectables)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 141, 161))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton_2 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        Selectables.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Selectables)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 149, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Selectables.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Selectables)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Selectables.setStatusBar(self.statusbar)

        self.retranslateUi(Selectables)
        QtCore.QMetaObject.connectSlotsByName(Selectables)

    def retranslateUi(self, Selectables):
        Selectables.setWindowTitle(_translate("Selectables", "Selectable Buttons", None))
        self.radioButton_2.setText(_translate("Selectables", "Milk", None))
        self.radioButton_3.setText(_translate("Selectables", "Half-and-half", None))
        self.radioButton.setText(_translate("Selectables", "Soy Milk", None))
        self.checkBox.setText(_translate("Selectables", "Sugar", None))

