#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jstrick/Documents/curr/pygui/StudentFiles/unix/pygui/EXAMPLES/developerinfo.ui'
#
# Created: Fri Jun 14 09:25:32 2013
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

class Ui_DeveloperInfo(object):
    def setupUi(self, DeveloperInfo):
        DeveloperInfo.setObjectName(_fromUtf8("DeveloperInfo"))
        DeveloperInfo.resize(231, 190)
        self.centralwidget = QtGui.QWidget(DeveloperInfo)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btGetInfo = QtGui.QPushButton(self.centralwidget)
        self.btGetInfo.setGeometry(QtCore.QRect(10, 16, 169, 46))
        self.btGetInfo.setObjectName(_fromUtf8("btGetInfo"))
        self.labInfo = QtGui.QLabel(self.centralwidget)
        self.labInfo.setGeometry(QtCore.QRect(18, 75, 182, 57))
        self.labInfo.setText(_fromUtf8(""))
        self.labInfo.setObjectName(_fromUtf8("labInfo"))
        DeveloperInfo.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DeveloperInfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 231, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        DeveloperInfo.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DeveloperInfo)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DeveloperInfo.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(DeveloperInfo)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(DeveloperInfo)
        QtCore.QMetaObject.connectSlotsByName(DeveloperInfo)

    def retranslateUi(self, DeveloperInfo):
        DeveloperInfo.setWindowTitle(_translate("DeveloperInfo", "DeveloperInfo", None))
        self.btGetInfo.setText(_translate("DeveloperInfo", "Get Developer Info", None))
        self.menuFile.setTitle(_translate("DeveloperInfo", "Application", None))
        self.actionQuit.setText(_translate("DeveloperInfo", "Quit", None))

