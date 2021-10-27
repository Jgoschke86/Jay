#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jstrick/Documents/curr/pygui/StudentFiles/unix/pygui/EXAMPLES/events.ui'
#
# Created: Thu Jun 13 10:15:02 2013
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

class Ui_Events(object):
    def setupUi(self, Events):
        Events.setObjectName(_fromUtf8("Events"))
        Events.resize(375, 262)
        Events.setMouseTracking(False)
        self.centralwidget = QtGui.QWidget(Events)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 3, 362, 200))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labName = QtGui.QLabel(self.verticalLayoutWidget)
        self.labName.setObjectName(_fromUtf8("labName"))
        self.horizontalLayout.addWidget(self.labName)
        self.leName = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.leName.setObjectName(_fromUtf8("leName"))
        self.horizontalLayout.addWidget(self.leName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pb_A = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pb_A.setObjectName(_fromUtf8("pb_A"))
        self.horizontalLayout_2.addWidget(self.pb_A)
        self.pb_B = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pb_B.setObjectName(_fromUtf8("pb_B"))
        self.horizontalLayout_2.addWidget(self.pb_B)
        self.pb_C = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pb_C.setObjectName(_fromUtf8("pb_C"))
        self.horizontalLayout_2.addWidget(self.pb_C)
        self.pb_D = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pb_D.setObjectName(_fromUtf8("pb_D"))
        self.horizontalLayout_2.addWidget(self.pb_D)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMouseTracking(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        Events.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Events)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        Events.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Events)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Events.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(Events)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionClear_name_field = QtGui.QAction(Events)
        self.actionClear_name_field.setObjectName(_fromUtf8("actionClear_name_field"))
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionClear_name_field)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.labName.setBuddy(self.leName)

        self.retranslateUi(Events)
        QtCore.QMetaObject.connectSlotsByName(Events)

    def retranslateUi(self, Events):
        Events.setWindowTitle(_translate("Events", "Events", None))
        self.labName.setText(_translate("Events", "Enter &Name: ", None))
        self.pb_A.setText(_translate("Events", "A", None))
        self.pb_B.setText(_translate("Events", "B", None))
        self.pb_C.setText(_translate("Events", "C", None))
        self.pb_D.setText(_translate("Events", "D", None))
        self.checkBox.setText(_translate("Events", "Do you love Python?", None))
        self.label.setText(_translate("Events", "Move the mouse over this label", None))
        self.menuFile.setTitle(_translate("Events", "File", None))
        self.menuEdit.setTitle(_translate("Events", "Edit", None))
        self.actionQuit.setText(_translate("Events", "Quit", None))
        self.actionClear_name_field.setText(_translate("Events", "Clear name field", None))

