#!/usr/bin/python

import sys
from PyQt4.QtGui import * 

app = QApplication(sys.argv)

mw = QMainWindow()

label = QLabel("Hello PyQt4 World")
        
mw.setCentralWidget(label)

mw.show()
app.exec_()
