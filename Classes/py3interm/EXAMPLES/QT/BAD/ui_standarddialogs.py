#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jstrick/Documents/curr/pygui/StudentFiles/unix/pygui/EXAMPLES/standarddialogs.ui'
#
# Created: Fri Jun 14 01:34:03 2013
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

class Ui_StandardDialogs(object):
    def setupUi(self, StandardDialogs):
        StandardDialogs.setObjectName(_fromUtf8("StandardDialogs"))
        StandardDialogs.resize(285, 221)
        self.centralwidget = QtGui.QWidget(StandardDialogs)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 3, 279, 165))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btColor = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btColor.setObjectName(_fromUtf8("btColor"))
        self.verticalLayout.addWidget(self.btColor)
        self.btFile = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btFile.setObjectName(_fromUtf8("btFile"))
        self.verticalLayout.addWidget(self.btFile)
        self.btMessage = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btMessage.setObjectName(_fromUtf8("btMessage"))
        self.verticalLayout.addWidget(self.btMessage)
        self.btInput = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btInput.setObjectName(_fromUtf8("btInput"))
        self.verticalLayout.addWidget(self.btInput)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        StandardDialogs.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(StandardDialogs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        StandardDialogs.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(StandardDialogs)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        StandardDialogs.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(StandardDialogs)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(StandardDialogs)
        QtCore.QMetaObject.connectSlotsByName(StandardDialogs)

    def retranslateUi(self, StandardDialogs):
        StandardDialogs.setWindowTitle(_translate("StandardDialogs", "StandardDialogs", None))
        self.btColor.setText(_translate("StandardDialogs", "Select Color", None))
        self.btFile.setText(_translate("StandardDialogs", "Select File", None))
        self.btMessage.setText(_translate("StandardDialogs", "Show Error Message", None))
        self.btInput.setText(_translate("StandardDialogs", "Input Text", None))
        self.label.setText(_translate("StandardDialogs", "Push a button...", None))
        self.menuFile.setTitle(_translate("StandardDialogs", "File", None))
        self.actionQuit.setText(_translate("StandardDialogs", "Quit", None))

