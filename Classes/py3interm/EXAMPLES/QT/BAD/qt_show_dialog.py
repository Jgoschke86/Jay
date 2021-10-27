import sys
from PyQt4.QtGui import * 
from PyQt4.QtCore import *
from qt_dialog_ship import ShipDimensionsDlg

class HelloWindow(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.create_widgets()

    @pyqtSlot()
    def getShipDimensions(self):
        s = ShipDimensionsDlg(self)
        s.setModal(True)
        # call exec_(), not show()
        if s.exec_():
            print "Your ship is {0} x {1}".format(s.Beam,s.LOA)
        else:
            print "exec_ FALSE"
        
    def create_widgets(self):
        self.label = QLabel("Hello PyQt4 World")
        hello_button = QPushButton("Set dimensions")
        
        # create a vertical layout for the central widget
        vb =  QVBoxLayout()
        vb.addWidget(self.label)
        vb.addWidget(hello_button)
        central_widget = QWidget()
        central_widget.setLayout(vb)
        self.setCentralWidget(central_widget)  

        hello_button.connect(hello_button, SIGNAL("clicked()"), self, SLOT("getShipDimensions()"))

        # hello_button.clicked.connect(getShipDimensions)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HelloWindow()
    main_window.show()
    app.exec_()
