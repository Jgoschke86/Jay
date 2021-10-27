# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'images.ui'
#
# Created: Thu Jul 11 07:04:00 2013
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

class Ui_Images(object):
    def setupUi(self, Images):
        Images.setObjectName(_fromUtf8("Images"))
        Images.resize(526, 348)
        self.centralwidget = QtGui.QWidget(Images)
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
        Images.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Images)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPictures = QtGui.QMenu(self.menubar)
        self.menuPictures.setObjectName(_fromUtf8("menuPictures"))
        Images.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Images)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Images.setStatusBar(self.statusbar)
        self.actionA = QtGui.QAction(Images)
        self.actionA.setObjectName(_fromUtf8("actionA"))
        self.actionB = QtGui.QAction(Images)
        self.actionB.setObjectName(_fromUtf8("actionB"))
        self.actionC = QtGui.QAction(Images)
        self.actionC.setObjectName(_fromUtf8("actionC"))
        self.actionQuit = QtGui.QAction(Images)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionPictureA = QtGui.QAction(Images)
        self.actionPictureA.setObjectName(_fromUtf8("actionPictureA"))
        self.actionPictureB = QtGui.QAction(Images)
        self.actionPictureB.setObjectName(_fromUtf8("actionPictureB"))
        self.actionPictureC = QtGui.QAction(Images)
        self.actionPictureC.setObjectName(_fromUtf8("actionPictureC"))
        self.menuPictures.addAction(self.actionPictureA)
        self.menuPictures.addAction(self.actionPictureB)
        self.menuPictures.addAction(self.actionPictureC)
        self.menuPictures.addAction(self.actionQuit)
        self.menubar.addAction(self.menuPictures.menuAction())

        self.retranslateUi(Images)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Images)

    def retranslateUi(self, Images):
        Images.setWindowTitle(_translate("Images", "Images", None))
        self.labA.setText(_translate("Images", "Apple", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabA), _translate("Images", "A", None))
        self.labB.setText(_translate("Images", "Banana", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabB), _translate("Images", "B", None))
        self.labC.setText(_translate("Images", "Cherry", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabC), _translate("Images", "C", None))
        self.menuPictures.setTitle(_translate("Images", "Pictures", None))
        self.actionA.setText(_translate("Images", "A", None))
        self.actionB.setText(_translate("Images", "B", None))
        self.actionC.setText(_translate("Images", "C", None))
        self.actionQuit.setText(_translate("Images", "Quit", None))
        self.actionPictureA.setText(_translate("Images", "A", None))
        self.actionPictureB.setText(_translate("Images", "B", None))
        self.actionPictureC.setText(_translate("Images", "C", None))

