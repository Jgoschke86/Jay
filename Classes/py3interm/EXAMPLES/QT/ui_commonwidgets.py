#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commonwidgets.ui'
#
# Created: Wed Jun 12 13:10:02 2013
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

class Ui_CommonWidgets(object):
    def setupUi(self, CommonWidgets):
        CommonWidgets.setObjectName(_fromUtf8("CommonWidgets"))
        CommonWidgets.resize(336, 196)
        self.centralwidget = QtGui.QWidget(CommonWidgets)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 131))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
#        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btPushMe = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btPushMe.setObjectName(_fromUtf8("btPushMe"))
        self.verticalLayout.addWidget(self.btPushMe)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labName = QtGui.QLabel(self.verticalLayoutWidget)
        self.labName.setObjectName(_fromUtf8("labName"))
        self.horizontalLayout.addWidget(self.labName)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.cbFruits = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cbFruits.setObjectName(_fromUtf8("cbFruits"))
        self.verticalLayout.addWidget(self.cbFruits)
        CommonWidgets.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CommonWidgets)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        CommonWidgets.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CommonWidgets)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CommonWidgets.setStatusBar(self.statusbar)
        self.labName.setBuddy(self.lineEdit)

        self.retranslateUi(CommonWidgets)
        QtCore.QMetaObject.connectSlotsByName(CommonWidgets)

    def retranslateUi(self, CommonWidgets):
        CommonWidgets.setWindowTitle(_translate("CommonWidgets", "Common Widgets", None))
        self.btPushMe.setText(_translate("CommonWidgets", "PushButton", None))
        self.labName.setText(_translate("CommonWidgets", "&Name", None))

