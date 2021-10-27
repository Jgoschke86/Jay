import sys
from PyQt4.QtGui import * 
from PyQt4.QtCore import *
from qt_dialog_ship import ShipDimensionsDlg

class HelloWindow(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.create_widgets()
        self.setWindowTitle("Selectable")
        
    def create_widgets(self):
        self.label = QLabel("Hello PyQt4 World")
        
        # create a vertical layout for the central widget
        vb =  QVBoxLayout()

        MilkRadioButton = QRadioButton("Milk", checked=True)
        HalfAndHalfRadioButton = QRadioButton("Half-and-half")
        SoyRadioButton = QRadioButton("Soy Milk")

        SugarCheckBox = QCheckBox("Sugar")    

        vb.addWidget(MilkRadioButton)
        vb.addWidget(HalfAndHalfRadioButton)
        vb.addWidget(SoyRadioButton)
        vb.addWidget(SugarCheckBox)
        
        
        
        hb = QHBoxLayout()
        
        

        central_widget = QWidget()
        central_widget.setLayout(vb)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HelloWindow()
    main_window.show()
    app.exec_()
