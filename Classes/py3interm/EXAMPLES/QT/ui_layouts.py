#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_layouts.ui'
#
# Created: Wed Jun 12 13:12:27 2013
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

class Ui_Layouts(object):
    def setupUi(self, Layouts):
        Layouts.setObjectName(_fromUtf8("Layouts"))
        Layouts.resize(411, 268)
        self.centralwidget = QtGui.QWidget(Layouts)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 411, 221))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        Layouts.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Layouts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Layouts.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Layouts)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Layouts.setStatusBar(self.statusbar)

        self.retranslateUi(Layouts)
        QtCore.QMetaObject.connectSlotsByName(Layouts)

    def retranslateUi(self, Layouts):
        Layouts.setWindowTitle(_translate("Layouts", "Layouts", None))
        self.label.setText(_translate("Layouts", "VBox Row 1", None))
        self.label_2.setText(_translate("Layouts", "VBox Row 2", None))
        self.label_6.setText(_translate("Layouts", "<html><head/><body><p>VBox Row 3<br/>HBox Col 1</p></body></html>", None))
        self.label_7.setText(_translate("Layouts", "VBox Row 3\n"
"HBox Col 2", None))
        self.label_4.setText(_translate("Layouts", "VBox Row 3\n"
"HBox Col 3", None))
        self.label_3.setText(_translate("Layouts", "VBox Row 4", None))

