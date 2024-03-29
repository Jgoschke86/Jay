#!/usr/bin/env python

#
# (c) 2013 John Strickler
#
# StandardDialogs
# 
########################################
import sys
import os

from PyQt4.QtGui import *

from ui_standarddialogs import Ui_StandardDialogs

class StandardDialogsMain(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_StandardDialogs()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(lambda:self.close())

        # Connect up the buttons.
        self.ui.btFile.clicked.connect(self._choose_file) 
        self.ui.btColor.clicked.connect(self._choose_color) 
        self.ui.btMessage.clicked.connect(self._show_error) 
        self.ui.btInput.clicked.connect(self._get_input) 
       # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

    def _choose_file(self):
        full_path = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())
        file_name = os.path.basename(str(full_path))
        self.ui.statusbar.showMessage("You chose: " + file_name)

    def _choose_color(self):
        color = QColor()
        result = QColorDialog.getColor(color)
        self.ui.statusbar.showMessage(
            "You chose #{0:02x}{1:02x}{2:02x} ({0},{1},{2})".format(
                result.red(),
                result.green(),
                result.blue()
            )                                                      
        )


    def _show_error(self):
        em = QErrorMessage(self)
        em.showMessage("There is a problem")
        self.ui.statusbar.showMessage('Diplaying Error')

    def _get_input(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        if ok:
            self.ui.statusbar.showMessage("Your name is " + text)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StandardDialogsMain()
    main.show()
    sys.exit(app.exec_())
