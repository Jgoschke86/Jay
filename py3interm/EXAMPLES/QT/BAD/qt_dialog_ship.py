import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ShipDimensionsDlg(QDialog):

# for more control:
#    @pyqtSlot()
#    def onOK(self):
#        print "Accepted!"
#        
#    @pyqtSlot()
#    def onCancel(self):
#        print "Cancelled!"

    def _make_line_edit(self,label_text,minval,maxval):
        lab = QLabel(label_text)
        edit = QLineEdit()
        validator = QIntValidator(minval, maxval, self)
        edit.setValidator(validator)
        edit.setText('0')
        lab.setBuddy(edit)
        
        return(lab, edit)

    def _make_layout(self, *widgets):
        layout = QHBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        return layout
 
    def _make_units_layout(self):
        unitsLabel = QLabel("Units:")
                
        unitsCombo = QComboBox()
        unitsCombo.addItems(['Feet','Meters'])
                
        layout = QHBoxLayout()
        layout.addWidget(unitsLabel)
        layout.addWidget(unitsCombo)
 
        return layout
            
    def __init__(self, parent=None):
        super(ShipDimensionsDlg, self).__init__(parent)
        self.setWindowTitle("Ship Dimensions")
                
        (widthLabel, self._widthEdit) = self._make_line_edit("&Width", 10, 500)
        (lengthLabel, self._lengthEdit) = self._make_line_edit("&Length", 10, 2000)

        widthLayout = self._make_layout(widthLabel, self._widthEdit)        
        lengthLayout = self._make_layout(lengthLabel, self._lengthEdit)

        unitsLayout = self._make_units_layout()                             
                
        buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )        
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
        
        self.connect(buttonBox, SIGNAL("accepted()"),self,SLOT('accept()'))
        self.connect(buttonBox, SIGNAL("rejected()"),self,SLOT('reject()'))
        
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(unitsLayout)
        mainLayout.addLayout(widthLayout)
        mainLayout.addLayout(lengthLayout)
        mainLayout.addWidget(buttonBox)
        
        self.setLayout(mainLayout)

# for more control         
#        self.connect(self, SIGNAL("accepted()"), self, SLOT("onOK()"))
#        self.connect(self, SIGNAL("rejected()"), self, SLOT("onCancel()"))

    # Properties

    @property
    def Beam(self):
        return int(self._widthEdit.text())

    @property
    def LOA(self):
        return int(self._lengthEdit.text())

if __name__ == '__main__':        
    app = QApplication(sys.argv)
    s = ShipDimensionsDlg()
    s.exec_()
    print s.Beam, s.LOA
    # app.exec_()
