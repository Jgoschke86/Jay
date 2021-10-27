#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jstrick/Documents/curr/pygui/StudentFiles/unix/pygui/EXAMPLES/developerinfodialog.ui'
#
# Created: Fri Jun 14 02:34:17 2013
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

class Ui_DeveloperInfoDialog(object):
    def setupUi(self, DeveloperInfoDialog):
        DeveloperInfoDialog.setObjectName(_fromUtf8("DeveloperInfoDialog"))
        DeveloperInfoDialog.resize(477, 174)
        self.buttonBox = QtGui.QDialogButtonBox(DeveloperInfoDialog)
        self.buttonBox.setGeometry(QtCore.QRect(87, 127, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(DeveloperInfoDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 15, 455, 96))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labName = QtGui.QLabel(self.verticalLayoutWidget)
        self.labName.setObjectName(_fromUtf8("labName"))
        self.horizontalLayout_3.addWidget(self.labName)
        self.leName = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.leName.setObjectName(_fromUtf8("leName"))
        self.horizontalLayout_3.addWidget(self.leName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labEmail = QtGui.QLabel(self.verticalLayoutWidget)
        self.labEmail.setObjectName(_fromUtf8("labEmail"))
        self.horizontalLayout_4.addWidget(self.labEmail)
        self.leEmail = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.leEmail.setObjectName(_fromUtf8("leEmail"))
        self.horizontalLayout_4.addWidget(self.leEmail)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.rbPython = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rbPython.setChecked(True)
        self.rbPython.setObjectName(_fromUtf8("rbPython"))
        self.horizontalLayout_5.addWidget(self.rbPython)
        self.rbPerl = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rbPerl.setObjectName(_fromUtf8("rbPerl"))
        self.horizontalLayout_5.addWidget(self.rbPerl)
        self.rbRuby = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rbRuby.setObjectName(_fromUtf8("rbRuby"))
        self.horizontalLayout_5.addWidget(self.rbRuby)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(DeveloperInfoDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DeveloperInfoDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DeveloperInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DeveloperInfoDialog)

    def retranslateUi(self, DeveloperInfoDialog):
        DeveloperInfoDialog.setWindowTitle(_translate("DeveloperInfoDialog", "DeveloperInfoDialog", None))
        self.labName.setText(_translate("DeveloperInfoDialog", "Name", None))
        self.labEmail.setText(_translate("DeveloperInfoDialog", "Email Address: ", None))
        self.rbPython.setText(_translate("DeveloperInfoDialog", "Python", None))
        self.rbPerl.setText(_translate("DeveloperInfoDialog", "Perl", None))
        self.rbRuby.setText(_translate("DeveloperInfoDialog", "Ruby", None))

