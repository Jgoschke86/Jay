import sys
from PyQt4.QtGui import * 
from PyQt4.QtCore import *

class HelloWindow(QMainWindow):
    def buttonPushed(self):
        self._bt.setText('Ouch!')
    
    @pyqtSlot()
    def _fruitSelected(self):
        self._bt.setText(self._cb.currentText())

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("Actions")
        
        lab = QLabel("&Name:")
        le = QLineEdit()
        lab.setBuddy(le)

        hb = QHBoxLayout()
        hb.addWidget(lab)
        hb.addWidget(le)

        self._bt = QPushButton('Push Me')
        self._bt.clicked.connect(self.buttonPushed)
        
        self._cb = QComboBox()
        self._cb.addItems(('apple','banana','mango','plum','lime'))
        self._cb.activated.connect(self._fruitSelected)
        
        vb = QVBoxLayout()
        vb.addWidget(self._bt)
        vb.addLayout(hb)
        vb.addWidget(self._cb)
        
        mainwidget = QWidget()
        mainwidget.setLayout(vb)
        
        self.setCentralWidget(mainwidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HelloWindow()
    main_window.show()
    app.exec_()
