#!/usr/bin/env python

#
# (c) 2013 John Strickler
#
# Layouts
# 
########################################
import sys

from PyQt4.QtGui import QMainWindow, QApplication
from ui_layouts import Ui_Layouts

class LayoutsMain(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_Layouts()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = LayoutsMain()
    main.show()
    sys.exit(app.exec_())


