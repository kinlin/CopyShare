# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from fontandString import *

class FuncManager(QWidget):
  def __init__(self, parent = None, view = None):
    super(FuncManager, self).__init__(parent)
    self.parent = parent
    self.FunBt = QStackedWidget()
    self.FunBt.addWidget(ManualFunc())
    self.FunBt.addWidget(StepFunc())
    self.FunBt.addWidget(AutoFunc())
    self.FunBt.setCurrentIndex(0)
    
    self.vf2layout = QGridLayout()
    self.vf2layout.addWidget(self.FunBt)
    self.vf2layout.setMargin(0)
    self.parent.setLayout(self.vf2layout)
  def setfunBt(self, i=None):
    return self.FunBt.setCurrentIndex(i)
  def setcommand(self, cmds):
    self.command = cmds
class ManualFunc(QWidget):
  def __init__(self, parent = None, view = None):
    super(ManualFunc, self).__init__(parent)
    self.manualFunBt = []
    self.menuBn = QComboBox()
    for i in range(len(menuBns)):
        self.menuBn.insertItem(i, menuBns[i])
    for i in range(len(manulFuncBtnNames)):
        self.manualFunBt.append(QPushButton(manulFuncBtnNames[i]))
    self.manualFunBtview = QHBoxLayout()
    self.manualFunBtview.addWidget(self.menuBn)
    for i in range(len(manulFuncBtnNames)):
        self.manualFunBtview.addWidget(self.manualFunBt[i])
    self.setLayout(self.manualFunBtview)
#-----ManualFunc中的信号处理-----
    self.connect(self.menuBn, SIGNAL("currentIndexChanged(int)"),  self.menuFnc)
#-----ManualFunc中的函数-----
  def menuFnc(self):
    index = self.menuBn.currentIndex()
    text = u"%s 被选中" %menuBns[index]
    msgBox = QMessageBox().information(self,"INFO", text)


class StepFunc(QWidget):
  def __init__(self, parent = None, view = None):
    super(StepFunc, self).__init__(parent)
    self.StepViewFunBt = []
    for i in range(len(stepFuncBtnNames)):
        self.StepViewFunBt.append(QPushButton(stepFuncBtnNames[i]))
    self.setpviewFunBtview = QHBoxLayout()
    for i in range(len(stepFuncBtnNames)):
        self.setpviewFunBtview.addWidget(self.StepViewFunBt[i])
    self.setLayout(self.setpviewFunBtview)    

class AutoFunc(QWidget): 
    pass

