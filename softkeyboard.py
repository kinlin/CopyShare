# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from fontandString import *
import sys
#import virtkey
class softkeyboard(QDialog):
  def __init__(self, parent = None, focusEntry = None):
    super(softkeyboard, self).__init__(parent)
    self.parent = parent
    self.setWindowTitle(u'键盘')
    self.setFixedSize(260, 260)
    self.focusEntry = focusEntry
    self.softbn = []
    self.softkeylayout()


  def softkeylayout(self):
    sfBtnNames = ('7', '8', '9','4', '5','6','1', '2','3','0','.','-',u'  退格  ',u'  确定  ')
    self.sfbnlayout = QGridLayout()
    self.sfbnlayout.setContentsMargins(0, 0, 8, 6)
    for i in range(4):
        for j in range(3):
            self.softbn.append(QPushButton(sfBtnNames[i*3+j]))
            self.sfbnlayout.addWidget(self.softbn[i*3+j], i, j, 1, 1)
    self.softbn.append(QPushButton(sfBtnNames[12]))
    self.sfbnlayout.addWidget(self.softbn[12], 0, 3, 2, 1)
    self.softbn.append(QPushButton(sfBtnNames[13]))
    self.sfbnlayout.addWidget(self.softbn[13], 2, 3, 2, 1)
    
    for i in range(12):
        self.softbn[i].setFixedSize(65, 65)
        self.softbn[i].setFont(font1)
    self.softbn[12].setFixedSize(65, 130)
    self.softbn[12].setFont(font1)
    self.softbn[13].setFixedSize(65, 130)
    self.softbn[13].setFont(font1)
    
    self.setLayout(self.sfbnlayout)
    #----信号连接-----
    for i in range(12):
        self.connect(self.softbn[i], SIGNAL("clicked()"), lambda key=i: self.keyvaluedeal(self.softbn[key]))
  def keyvaluedeal(self, args):
    self.args = args
    msgBox = QMessageBox().information(self,"INFO", "clicked")
#    self.parent.setText('button pressed')
         
         

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = softkeyboard()
    form.show()
    app.exec_()
