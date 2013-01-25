# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from fontandString import *

class Stop(QWidget):
  def __init__(self, parent = None, view = None, func = None):
    super(Stop, self).__init__(parent)
    self.parent = parent
    vf3bt1 = QPushButton(u"伺服")
    vf3bt2 = QPushButton(u"关机")
    vf3layout = QGridLayout()
    vf3layout.setMargin(0)  
    vf3layout.addWidget(vf3bt1, 0, 0)
    vf3layout.addWidget(vf3bt2, 0, 1)
    self.parent.setLayout(vf3layout)

  def setcommand(self, cmds):
    self.command = cmds
