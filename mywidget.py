# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from fontandString import *
from softkeyboard import *
import sys  

class EditLabel(QLabel):
    def __init__(self, text):
        super(EditLabel, self).__init__()
        self.setText(text)
    def mousePressEvent(self, event):
        form = VirtualKeyboard()
        self.connect(form, SIGNAL("PushString"), self.getstrings)
        form.exec_()
    def getstrings(self,strings):
        self.setText(strings)
class KeyButton(QPushButton):
    def __init__(self, key):
        super(KeyButton, self).__init__()
        self._key = key
        self._activeSize = QSize(65,65)
        self.connect(self, SIGNAL("clicked()"), self.emitKey)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        
    def emitKey(self):
        self.emit(SIGNAL("sigKeyButtonClicked"), self._key)
    def enterEvent(self, event):
        self.setFixedSize(self._activeSize)
    def leaveEvent(self, event):
        self.setFixedSize(self.sizeHint())
    def sizeHint(self):
        return QSize(55, 55)
        
class VirtualKeyboard(QDialog):
    def __init__(self):
        super(VirtualKeyboard, self).__init__()
        self.setFixedSize(300, 300)
        self.globalLayout = QVBoxLayout()
        self.containLayout = QHBoxLayout()
        self.keysLayout = QGridLayout()
        self.buttonLayout = QVBoxLayout()
        self.keysLayout.setContentsMargins(0, 0, 8, 6)
        self.setWindowTitle(softFunBn[4])
        self.inputString = ""
        self.keyListByLines = [
                            ['1', '2', '3'],
                            ['4', '5', '6'],
                            ['7', '8', '9'],
                            ['-', '0', '.']  ]
        self.clearButton = QPushButton(softFunBn[0])
        self.clearButton.setFixedSize(self.sizeHint())
        self.backButton = QPushButton(softFunBn[1])
        self.backButton.setFixedSize(self.sizeHint())
        self.okButton = QPushButton(softFunBn[2])
        self.okButton.setFixedSize(self.sizeHint())
        self.cancelButton = QPushButton(softFunBn[3])
        self.cancelButton.setFixedSize(self.sizeHint())
        self.inputLine = QLineEdit()
        
        for lineIndex, line in enumerate(self.keyListByLines):
            for keyIndex, key in enumerate(line):
                buttonName = "keyButton" + key.capitalize()
                self.__setattr__(buttonName, KeyButton(key))
                self.keysLayout.addWidget(self.getButtonByKey(key), self.keyListByLines.index(line), line.index(key))
                self.getButtonByKey(key).setText(key)
                self.connect(self.getButtonByKey(key), SIGNAL("sigKeyButtonClicked"), self.addInputByKey)
                self.keysLayout.setColumnMinimumWidth(keyIndex, 80)
            self.keysLayout.setRowMinimumHeight(lineIndex, 80)
        
        self.connect(self.clearButton, SIGNAL("clicked()"), self.clearBn)
        self.connect(self.backButton, SIGNAL("clicked()"), self.backBn)
        self.connect(self.okButton, SIGNAL("clicked()"), self.okBn)
        self.connect(self.cancelButton, SIGNAL("clicked()"), self.cancelBn)
        
        self.buttonLayout.addWidget(self.clearButton)
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.addWidget(self.okButton)
        self.buttonLayout.addWidget(self.cancelButton)
        
        self.containLayout.addLayout(self.keysLayout)
        self.containLayout.addLayout(self.buttonLayout)
        self.globalLayout.addWidget(self.inputLine)
        self.globalLayout.addLayout(self.containLayout)
        
                
        self.setLayout(self.globalLayout)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
    def getButtonByKey(self, key):
        return getattr(self, "keyButton" + key.capitalize())
    def sizeHint(self):
        return QSize(55, 55)
    def addInputByKey(self, key):
        # msgBox = QMessageBox().information(self,"INFO", "clicked")
        self.inputString += key
        self.inputLine.setText(self.inputString)
    def clearBn(self):
        self.inputLine.clear()
        self.inputString = ""
    def backBn(self):
        self.inputLine.backspace()
        self.inputString = self.inputString[:-1]
    def okBn(self):
        self.emit(SIGNAL("PushString"), self.inputString)
        self.close()
    def cancelBn(self):
        self.close()
        
    ####
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = VirtualKeyboard()
    form.show()
    app.exec_()