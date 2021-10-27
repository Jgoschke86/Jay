#!/usr/bin/python

import sys
from PyQt4.QtGui import * 

class StandardDialogs(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Standard Dialogs')
        self._create_widgets()

    def _show_input_dialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        if ok:
            self._label.setText("Your name is " + text)

    def _show_color_dialog(self):
        color = QColor()
        result = QColorDialog.getColor(color)
        self._label.setText(
            "You chose #{0:02x}{1:02x}{2:02x}".format(
                result.red(),
                result.green(),
                result.blue()
            )                                                      
        )
        
    def _show_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', '/')
        self._label.setText("You chose: " + file_name)
        
        
    def _show_error_dialog(self):
        em = QErrorMessage(self)
        self._label.setText('Diplaying Error')
        em.showMessage("There is a problem")

    def _create_widgets(self):
        vb = QVBoxLayout()
        
        self._bt_color = QPushButton('Select Color', self)
        self._bt_color.clicked.connect(self._show_color_dialog)
        vb.addWidget(self._bt_color)

        self._bt_file = QPushButton('Select File', self)
        self._bt_file.clicked.connect(self._show_file_dialog)
        vb.addWidget(self._bt_file)
        
        self._bt_error = QPushButton('Show Error', self)
        self._bt_error.clicked.connect(self._show_error_dialog)
        vb.addWidget(self._bt_error)

        self._bt_error = QPushButton('Input text', self)
        self._bt_error.clicked.connect(self._show_input_dialog)
        vb.addWidget(self._bt_error)

        
        self._label = QLabel("Push a button...")
        vb.addWidget(self._label)
        
        central_widget = QWidget()
        central_widget.setLayout(vb)
        
        self.setCentralWidget(central_widget)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = StandardDialogs()
    main_window.show()
    app.exec_()
