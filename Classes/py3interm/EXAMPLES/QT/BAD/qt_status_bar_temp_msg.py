import sys
from PyQt4.QtGui import * 

class HelloWindow(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.create_widgets()
        self.create_status_bar()
    
    def _hello_clicked(self):
        self._sb.showMessage('Button pushed',1000)
    
    def create_widgets(self):
        self.label = QLabel("Hello PyQt4 World")
        self.hello_button = QPushButton("Push Me!")
        self.hello_button.clicked.connect(self._hello_clicked)
        
        # create a vertical layout for the central widget
        vb =  QVBoxLayout()
        vb.addWidget(self.label)
        vb.addWidget(self.hello_button)
        central_widget = QWidget()
        central_widget.setLayout(vb)
        self.setCentralWidget(central_widget)

    def create_status_bar(self):
        sb_label_left = QLabel("All systems go")
        sb_label_right = QLabel("100")
        self._sb = QStatusBar()
        self._sb.addWidget(sb_label_left)     # on right, may be overwritten
        self._sb.addPermanentWidget(sb_label_right)  # stays on left
        self.setStatusBar(self._sb)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HelloWindow()
    main_window.show()
    app.exec_()
