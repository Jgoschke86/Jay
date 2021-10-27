#!/usr/bin/python

import sys
from PyQt4.QtGui import * 

class HelloWindow(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.create_widgets()
        self._create_menu_bar()
        self.setWindowTitle("Menus")
        
    def create_widgets(self):
        label = QLabel("Fun with menus")
        self.setCentralWidget(label)

    def _create_menu_bar(self):
        self._menubar = self.menuBar()
        
        # File menu
        self._fileMenu = self._menubar.addMenu('&File')

        self._open_action = QAction('Load...', self)
        self._fileMenu.addAction(self._open_action)

        self._quit_action = QAction("&Quit", self)
        self._fileMenu.addAction(self._quit_action) 

        # Edit menu
        self._fileMenu = self._menubar.addMenu('&Edit')

        self._cut_action = QAction('Cut', self)
        self._copy_action = QAction('Copy', self)
        self._paste_action = QAction('Paste', self)

        self._fileMenu.addAction(self._cut_action) 
        self._fileMenu.addAction(self._copy_action) 
        self._fileMenu.addAction(self._paste_action) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HelloWindow()
    main_window.show()
    app.exec_()
