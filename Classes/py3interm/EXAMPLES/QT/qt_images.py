#!/usr/bin/env python

#
# (c) 2013 John Strickler
#
# Images
# 
########################################
import sys

from PyQt4.QtGui import QMainWindow, QApplication, QPixmap
from ui_images import Ui_Images

class ImagesMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_Images()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(lambda:self.close())

        self.ui.actionPictureA.triggered.connect(
            lambda: self._show_picture('A')
        )
        self.ui.actionPictureB.triggered.connect(
            lambda: self._show_picture('B')
        )
        self.ui.actionPictureC.triggered.connect(
            lambda: self._show_picture('C')
        )

    def _show_picture(self, which_picture):
        if which_picture == 'A':
            image_file = 'apple.png'
            label = self.ui.labA
        elif which_picture == 'B':
            image_file = 'banana.jpg'
            label = self.ui.labB
        elif which_picture == 'C':
            image_file = 'cherry.jpg'
            label = self.ui.labC
            
        img = QPixmap('../../DATA/' + image_file)
        label.setPixmap(img)
        label.setScaledContents(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ImagesMain()
    main.show()
    sys.exit(app.exec_())
