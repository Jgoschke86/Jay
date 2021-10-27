#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jstrick/Documents/curr/pygui/StudentFiles/unix/pygui/EXAMPLES/wordfinder.ui'
#
# Created: Thu Jun 13 22:28:51 2013
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

class Ui_WordFinder(object):
    def setupUi(self, WordFinder):
        WordFinder.setObjectName(_fromUtf8("WordFinder"))
        WordFinder.resize(408, 353)
        self.centralwidget = QtGui.QWidget(WordFinder)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(14, 11, 381, 284))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labPattern = QtGui.QLabel(self.verticalLayoutWidget)
        self.labPattern.setObjectName(_fromUtf8("labPattern"))
        self.horizontalLayout.addWidget(self.labPattern)
        self.lePattern = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lePattern.setObjectName(_fromUtf8("lePattern"))
        self.horizontalLayout.addWidget(self.lePattern)
        self.btSearch = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btSearch.setObjectName(_fromUtf8("btSearch"))
        self.horizontalLayout.addWidget(self.btSearch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.teText = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        self.teText.setObjectName(_fromUtf8("teText"))
        self.verticalLayout.addWidget(self.teText)
        WordFinder.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(WordFinder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        WordFinder.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(WordFinder)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        WordFinder.setStatusBar(self.statusbar)
        self.actionLoad = QtGui.QAction(WordFinder)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionQuit = QtGui.QAction(WordFinder)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(WordFinder)
        QtCore.QMetaObject.connectSlotsByName(WordFinder)

    def retranslateUi(self, WordFinder):
        WordFinder.setWindowTitle(_translate("WordFinder", "WordFinder", None))
        self.labPattern.setText(_translate("WordFinder", "Pattern:", None))
        self.btSearch.setText(_translate("WordFinder", "Search", None))
        self.menuFile.setTitle(_translate("WordFinder", "File", None))
        self.actionLoad.setText(_translate("WordFinder", "Load...", None))
        self.actionQuit.setText(_translate("WordFinder", "Quit", None))

