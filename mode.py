# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from fontandString import *
from root import *
class Mode(QWidget):
  def __init__(self, parent = None, view = None, func = None):
    super(Mode, self).__init__(parent)
    self.parent = parent
    self.view = view
    self.func = func
    self.modebn = []
    self.vf1layout = QVBoxLayout()         
    for i in range(8):
        self.modebn.append(QPushButton(modeString[i]))
    for i in range(8):
        self.modebn[i].setFixedSize(100,45)
    for i in range(8):
        self.vf1layout.insertWidget(i, self.modebn[i])
    self.vf1layout.setMargin(0)
    self.parent.setLayout(self.vf1layout)
#-----Signal-Slot-----
    for i in range(8):
        self.connect(self.modebn[i], SIGNAL("clicked()"), self.clicked)
#-----Function-----
  def clicked(self):
    button = self.sender()
    if button is None or not isinstance(button,  QPushButton):
        return
    index = self.vf1layout.indexOf(button)
#-----分别是左上，左下  框题头和其中的缓存页
    self.view.parent.setTitle(modeString[index])
    self.view.setviewIndex(index)
    self.func.parent.setTitle(funcViewTitles[index])
    self.func.setfunBt(index)

  def setcommand(self, cmds):
    self.command = cmds
  
