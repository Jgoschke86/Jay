#!/usr/bin/python

import sys
import re
from PyQt4.QtGui import * 
from PyQt4.QtCore import *

class WordFinder(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle("Word Finder")
        self._create_menu_bar()
        self._create_widgets()
        self._create_status_bar()
    
    def _clear_file_window(self):
        self._file_window.clear()
            
    def _load_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file for matching', '/')
        with open(fname) as F:
            self._words = [ line.rstrip() for line in F.readlines() ]
        self._numwords = len(self._words)
        self._clear_file_window()

        self._file_window.insertPlainText("\n".join(self._words)+"\n")
        

    def _do_search(self):
        pattern = str(self._pattern_edit.text())
        if pattern == '':
            pattern = '.'
        rx = re.compile(pattern)
 
        self._clear_file_window()       
        self._pattern_search.setEnabled(False)
        self._pattern_search.setVisible(False)
        count = 0
        for word in self._words:
            if rx.search(word):
                self._file_window.insertPlainText(word + '\n')
                count += 1
        self._pattern_search.setEnabled(True)
        self._pattern_search.setVisible(True)
        self._statusbar_label.setText(
            "Matched {0} out of {1} words".format(count,self._numwords))
        
        
    def _create_menu_bar(self):
        self._menubar = self.menuBar()
        self._fileMenu = self._menubar.addMenu('&File')
        self._open_action = QAction('Load...', self)
        self._open_action.triggered.connect(self._load_file)
        # self.connect(self._open_action, SIGNAL('triggered()'), self._load_file)
        self._fileMenu.addAction(self._open_action)

        self._quit_action = QAction("&Quit", self)
        self.connect(self._quit_action, SIGNAL('triggered()'), SLOT('close()'))
        self._fileMenu.addAction(self._quit_action) 
        
        
    def _create_widgets(self):
        
        self._pattern_label = QLabel("Pattern:")
        self._pattern_edit = QLineEdit()
        self._pattern_search = QPushButton("Search")
        topLayout = QHBoxLayout()
        topLayout.addWidget(self._pattern_label)
        topLayout.addWidget(self._pattern_edit)
        topLayout.addWidget(self._pattern_search)
        
        self._pattern_search.clicked.connect(self._do_search)

        self._file_window = QTextEdit()
        
        # create a vertical layout for the central widget
        mainLayout =  QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addWidget(self._file_window)

        central_widget = QWidget()
        central_widget.setLayout(mainLayout)
        self.setCentralWidget(central_widget)

    def _create_status_bar(self):
        self._statusbar_label = QLabel("")
        sb = QStatusBar()
        sb.addWidget(self._statusbar_label)
        self.setStatusBar(sb)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = WordFinder()
    main_window.show()
    app.exec_()
