#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jstrick/Documents/curr/pygui/StudentFiles/unix/pygui/EXAMPLES/statusbar.ui'
#
# Created: Thu Jun 13 21:44:55 2013
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

class Ui_StatusBar(object):
    def setupUi(self, StatusBar):
        StatusBar.setObjectName(_fromUtf8("StatusBar"))
        StatusBar.resize(203, 132)
        self.centralwidget = QtGui.QWidget(StatusBar)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.btPushMe = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btPushMe.setObjectName(_fromUtf8("btPushMe"))
        self.verticalLayout.addWidget(self.btPushMe)
        StatusBar.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(StatusBar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 203, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        StatusBar.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(StatusBar)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        StatusBar.setStatusBar(self.statusbar)

        self.retranslateUi(StatusBar)
        QtCore.QMetaObject.connectSlotsByName(StatusBar)

    def retranslateUi(self, StatusBar):
        StatusBar.setWindowTitle(_translate("StatusBar", "StatusBar", None))
        self.label.setToolTip(_translate("StatusBar", "I\'m a tooltip!", None))
        self.label.setText(_translate("StatusBar", "Hello PyQt4 World", None))
        self.btPushMe.setText(_translate("StatusBar", "Push Me", None))

