#!/usr/bin/env python

#
# (c) 2013 John Strickler
#
# Tabs
# 
########################################
import sys

from PyQt4.QtGui import QMainWindow, QApplication
from ui_tabs import Ui_Tabs

class TabsMain(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_Tabs()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(lambda:self.close())
        self.ui.actionA.triggered.connect(lambda: self._show_tab('A'))
        self.ui.actionB.triggered.connect(lambda: self._show_tab('B'))
        self.ui.actionC.triggered.connect(lambda: self._show_tab('C'))
        
    def _show_tab(self, which_tab):
        if which_tab == 'A':
            self.ui.tabWidget.setCurrentIndex(0)
            self.ui.labA.setText('Aardvark')
        elif which_tab == 'B':
            self.ui.tabWidget.setCurrentIndex(1)
            self.ui.labB.setText('Bonobo')
        elif which_tab == 'C':
            self.ui.tabWidget.setCurrentIndex(2)
            self.ui.labC.setText('Coatimundi')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TabsMain()
    main.show()
    sys.exit(app.exec_())


