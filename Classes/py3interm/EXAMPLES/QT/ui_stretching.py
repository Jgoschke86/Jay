# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stretching.ui'
#
# Created: Sat Aug 31 11:11:21 2013
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

class Ui_Stretching(object):
    def setupUi(self, Stretching):
        Stretching.setObjectName(_fromUtf8("Stretching"))
        Stretching.resize(294, 201)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Stretching.sizePolicy().hasHeightForWidth())
        Stretching.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(Stretching)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.button_A = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_A.sizePolicy().hasHeightForWidth())
        self.button_A.setSizePolicy(sizePolicy)
        self.button_A.setObjectName(_fromUtf8("button_A"))
        self.verticalLayout.addWidget(self.button_A)
        self.button_B = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_B.sizePolicy().hasHeightForWidth())
        self.button_B.setSizePolicy(sizePolicy)
        self.button_B.setObjectName(_fromUtf8("button_B"))
        self.verticalLayout.addWidget(self.button_B)
        self.button_C = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.button_C.sizePolicy().hasHeightForWidth())
        self.button_C.setSizePolicy(sizePolicy)
        self.button_C.setObjectName(_fromUtf8("button_C"))
        self.verticalLayout.addWidget(self.button_C)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Stretching.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Stretching)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTesting = QtGui.QMenu(self.menubar)
        self.menuTesting.setObjectName(_fromUtf8("menuTesting"))
        Stretching.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Stretching)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Stretching.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(Stretching)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuTesting.addAction(self.actionQuit)
        self.menubar.addAction(self.menuTesting.menuAction())

        self.retranslateUi(Stretching)
        QtCore.QMetaObject.connectSlotsByName(Stretching)

    def retranslateUi(self, Stretching):
        Stretching.setWindowTitle(_translate("Stretching", "Stretching", None))
        self.button_A.setText(_translate("Stretching", "A", None))
        self.button_B.setText(_translate("Stretching", "B", None))
        self.button_C.setText(_translate("Stretching", "C", None))
        self.menuTesting.setTitle(_translate("Stretching", "Testing", None))
        self.actionQuit.setText(_translate("Stretching", "Quit", None))

