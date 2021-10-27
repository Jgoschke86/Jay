#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jstrick/Documents/curr/pygui/StudentFiles/unix/pygui/EXAMPLES/hello2.ui'
#
# Created: Wed Jun 12 14:53:14 2013
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

class Ui_Hello2(object):
    def setupUi(self, Hello2):
        Hello2.setObjectName(_fromUtf8("Hello2"))
        Hello2.resize(203, 164)
        self.centralwidget = QtGui.QWidget(Hello2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 141, 21))
        self.label.setObjectName(_fromUtf8("label"))
        Hello2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Hello2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 203, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Hello2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Hello2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Hello2.setStatusBar(self.statusbar)

        self.retranslateUi(Hello2)
        QtCore.QMetaObject.connectSlotsByName(Hello2)

    def retranslateUi(self, Hello2):
        Hello2.setWindowTitle(_translate("Hello2", "Hello2", None))
        self.label.setText(_translate("Hello2", "Hello PyQt4 World", None))

