import sys
from PyQt4.QtGui import * 

class HelloWindow(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("Common Widgets")
        
        lab = QLabel("&Name:")
        le = QLineEdit()
        lab.setBuddy(le)

        hb = QHBoxLayout()
        hb.addWidget(lab)
        hb.addWidget(le)

        bt = QPushButton('Push Me')
        cb = QComboBox()
        for n,(k,v) in enumerate((('apple',1),('banana',2),('mango',3)),1):
            cb.insertItem(n,k,v)
        
        vb = QVBoxLayout()
        vb.addWidget(bt)
        vb.addLayout(hb)
        vb.addWidget(cb)
        
        mainwidget = QWidget()
        mainwidget.setLayout(vb)
        
        self.setCentralWidget(mainwidget)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HelloWindow()
    main_window.show()
    app.exec_()
