#!/usr/bin/env python

#
# (c) 2013 John Strickler
#
# Selectables
# 
########################################
import sys

from PyQt4.QtGui import QMainWindow, QApplication
from ui_selectables import Ui_Selectables

class SelectablesMain(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_Selectables()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = SelectablesMain()
    main.show()
    sys.exit(app.exec_())


