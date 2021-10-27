# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'presinfo.ui'
#
# Created: Sun Sep  8 23:33:46 2013
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

class Ui_PresInfo(object):
    def setupUi(self, PresInfo):
        PresInfo.setObjectName(_fromUtf8("PresInfo"))
        PresInfo.resize(377, 309)
        self.centralwidget = QtGui.QWidget(PresInfo)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 381, 261))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labTermNum = QtGui.QLabel(self.verticalLayoutWidget)
        self.labTermNum.setObjectName(_fromUtf8("labTermNum"))
        self.horizontalLayout_2.addWidget(self.labTermNum)
        self.leTermNum = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.leTermNum.setObjectName(_fromUtf8("leTermNum"))
        self.horizontalLayout_2.addWidget(self.leTermNum)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.btGetInfo = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btGetInfo.setObjectName(_fromUtf8("btGetInfo"))
        self.verticalLayout_2.addWidget(self.btGetInfo)
        self.pteInfo = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        self.pteInfo.setObjectName(_fromUtf8("pteInfo"))
        self.verticalLayout_2.addWidget(self.pteInfo)
        PresInfo.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PresInfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFIle = QtGui.QMenu(self.menubar)
        self.menuFIle.setObjectName(_fromUtf8("menuFIle"))
        PresInfo.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PresInfo)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PresInfo.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(PresInfo)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFIle.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(PresInfo)
        QtCore.QMetaObject.connectSlotsByName(PresInfo)

    def retranslateUi(self, PresInfo):
        PresInfo.setWindowTitle(_translate("PresInfo", "President Info", None))
        self.labTermNum.setText(_translate("PresInfo", "Enter Term Number:", None))
        self.btGetInfo.setText(_translate("PresInfo", "Get Information", None))
        self.menuFIle.setTitle(_translate("PresInfo", "FIle", None))
        self.actionQuit.setText(_translate("PresInfo", "Quit", None))

