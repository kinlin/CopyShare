# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Welcome(QWidget):
  def __init__(self, parent = None):
    super(Welcome, self).__init__(parent)
    
    
    self.iconlabel0 = QLabel()
    self.vf0Img0 = QPixmap("E:\CopyShare\B01.jpg")
    self.iconlabel0.setPixmap(self.vf0Img0)
    self.iconlabel0.setMargin(0)
    layout = QGridLayout()
    layout.addWidget(self.iconlabel0)
    
    self.setLayout(layout)
    
class ManualView(QWidget):
  def __init__(self, parent = None):
    super(ManualView, self).__init__(parent)
    self.iconlabel1 = QLabel()                            #测试代码
    self.vf0Img1 = QPixmap("E:\CopyShare\B02.jpg")
    self.iconlabel1.setPixmap(self.vf0Img1)
    self.iconlabel1.setMargin(0)
    layout = QGridLayout()
    layout.addWidget(self.iconlabel1)
    self.setLayout(layout)
     
#     self.InfoBox = QGroupBox()
#     self.AlarmBox = QGroupBox()
#     self.ZPosBox = QGroupBox()
#     self.YScaleBox = QGroupBox()
#     self.XScaleBox = QGroupBox()
#     self.RScaleBox = QGroupBox()
#     self.ZScaleBox = QGroupBox()
#     self.GNBox = QGroupBox()   #新增功能按键
#     
#     self.manualgrid = QGridLayout()
#     self.manualgrid.addWidget(self.InfoBox)
class StepView(QWidget):
  def __init__(self, parent = None):
    super(StepView, self).__init__(parent)
    
    self.iconlabel2 = QLabel()
    self.vf0Img2 = QPixmap("E:\CopyShare\B03.jpg")
    self.iconlabel2.setPixmap(self.vf0Img2)
    self.iconlabel2.setMargin(0)
    layout = QGridLayout()
    layout.addWidget(self.iconlabel2)
    
    self.setLayout(layout)

class AutoView(QWidget):
  def __init__(self, parent = None):
    super(AutoView, self).__init__(parent)
    
    self.iconlabel3 = QLabel()
    self.vf0Img3 = QPixmap("E:\CopyShare\B04.jpg")
    self.iconlabel3.setPixmap(self.vf0Img3)
    self.iconlabel3.setMargin(0)
    layout = QGridLayout()
    layout.addWidget(self.iconlabel3)
    
    self.setLayout(layout)
