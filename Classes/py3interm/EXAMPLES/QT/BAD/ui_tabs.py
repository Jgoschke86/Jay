#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jstrick/Documents/curr/pygui/StudentFiles/unix/pygui/EXAMPLES/tabs.ui'
#
# Created: Fri Jun 14 00:49:47 2013
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

class Ui_Tabs(object):
    def setupUi(self, Tabs):
        Tabs.setObjectName(_fromUtf8("Tabs"))
        Tabs.resize(526, 348)
        self.centralwidget = QtGui.QWidget(Tabs)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-7, 6, 525, 299))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabA = QtGui.QWidget()
        self.tabA.setObjectName(_fromUtf8("tabA"))
        self.labA = QtGui.QLabel(self.tabA)
        self.labA.setGeometry(QtCore.QRect(34, 55, 471, 134))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.labA.setFont(font)
        self.labA.setObjectName(_fromUtf8("labA"))
        self.tabWidget.addTab(self.tabA, _fromUtf8(""))
        self.tabB = QtGui.QWidget()
        self.tabB.setObjectName(_fromUtf8("tabB"))
        self.labB = QtGui.QLabel(self.tabB)
        self.labB.setGeometry(QtCore.QRect(37, 59, 445, 134))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.labB.setFont(font)
        self.labB.setObjectName(_fromUtf8("labB"))
        self.tabWidget.addTab(self.tabB, _fromUtf8(""))
        self.tabC = QtGui.QWidget()
        self.tabC.setObjectName(_fromUtf8("tabC"))
        self.labC = QtGui.QLabel(self.tabC)
        self.labC.setGeometry(QtCore.QRect(46, 58, 454, 134))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.labC.setFont(font)
        self.labC.setObjectName(_fromUtf8("labC"))
        self.tabWidget.addTab(self.tabC, _fromUtf8(""))
        Tabs.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Tabs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTabs = QtGui.QMenu(self.menubar)
        self.menuTabs.setObjectName(_fromUtf8("menuTabs"))
        Tabs.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Tabs)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Tabs.setStatusBar(self.statusbar)
        self.actionA = QtGui.QAction(Tabs)
        self.actionA.setObjectName(_fromUtf8("actionA"))
        self.actionB = QtGui.QAction(Tabs)
        self.actionB.setObjectName(_fromUtf8("actionB"))
        self.actionC = QtGui.QAction(Tabs)
        self.actionC.setObjectName(_fromUtf8("actionC"))
        self.actionQuit = QtGui.QAction(Tabs)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuTabs.addAction(self.actionA)
        self.menuTabs.addAction(self.actionB)
        self.menuTabs.addAction(self.actionC)
        self.menuTabs.addAction(self.actionQuit)
        self.menubar.addAction(self.menuTabs.menuAction())

        self.retranslateUi(Tabs)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Tabs)

    def retranslateUi(self, Tabs):
        Tabs.setWindowTitle(_translate("Tabs", "Tabs", None))
        self.labA.setText(_translate("Tabs", "Apple", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabA), _translate("Tabs", "A", None))
        self.labB.setText(_translate("Tabs", "Banana", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabB), _translate("Tabs", "B", None))
        self.labC.setText(_translate("Tabs", "Cherry", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabC), _translate("Tabs", "C", None))
        self.menuTabs.setTitle(_translate("Tabs", "Tabs", None))
        self.actionA.setText(_translate("Tabs", "A", None))
        self.actionB.setText(_translate("Tabs", "B", None))
        self.actionC.setText(_translate("Tabs", "C", None))
        self.actionQuit.setText(_translate("Tabs", "Quit", None))

