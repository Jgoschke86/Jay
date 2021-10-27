#!/usr/bin/python

import sys
from PyQt4.QtGui import * 

class HelloWindow(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.create_widgets()
        self.setWindowTitle('Layouts')
        
    def create_widgets(self):
        self.label = QLabel("Hello PyQt4 World")
        self.label2 = QLabel("(2nd row of VBox)")
        self.label3 = QLabel("(3nd row of VBox)")
        
        # create a vertical layout for the central widget
        vb =  QVBoxLayout()
        vb.addWidget(self.label)
        vb.addWidget(self.label2)
        vb.addWidget(self.label3)
        central_widget = QWidget()
        central_widget.setLayout(vb)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HelloWindow()
    main_window.show()
    app.exec_()
