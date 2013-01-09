# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Welcome(QWidget):
  def __init__(self, parent = None):
    super(Welcome, self).__init__(parent)
    
    
    self.iconlabel0 = QLabel()
#    self.vf0Img0 = QPixmap("E:\CopyShare\B01.jpg")
    self.vf0Img0 = QPixmap("/home/kinlin/CopyShare/B01.jpg")
    self.iconlabel0.setPixmap(self.vf0Img0)
    self.iconlabel0.setMargin(0)
    layout = QGridLayout()
    layout.addWidget(self.iconlabel0)
    
    self.setLayout(layout)
    
class ManualView(QWidget):
  def __init__(self, parent = None):
    super(ManualView, self).__init__(parent)
    self.InfoBox = QGroupBox()
    self.InfoBox.setTitle(u"实时信息显示")
    self.AlarmBox = QGroupBox()
    self.AlarmBox.setTitle(u"报警信息")
    self.ZPosBox = QGroupBox()
    self.ZPosBox.setTitle(u"后挡料Z轴位置")
    self.YScaleBox = QGroupBox()
    self.YScaleBox.setTitle(u"Y轴")
    self.XScaleBox = QGroupBox()
    self.XScaleBox.setTitle(u"X轴")
    self.RScaleBox = QGroupBox()
    self.RScaleBox.setTitle(u"R轴")
    self.ZScaleBox = QGroupBox()
    self.ZScaleBox.setTitle(u"Z轴")
    self.VScaleBox = QGroupBox()
    self.VScaleBox.setTitle(u"V轴")
    self.GNBox = QGroupBox()   #新增功能按键
    self.GNBox.setTitle(u"功能按钮")
    
    manualgrid = QGridLayout()
    manualgrid.addWidget(self.InfoBox, 0, 0, 1, 3)
    manualgrid.addWidget(self.AlarmBox, 0, 3, 2, 3)
    manualgrid.addWidget(self.ZPosBox, 1, 0, 1, 3)
    manualgrid.addWidget(self.YScaleBox, 2, 0, 1, 2)
    manualgrid.addWidget(self.XScaleBox, 2, 2, 1, 2)
    manualgrid.addWidget(self.RScaleBox, 2, 4, 1, 2)
    manualgrid.addWidget(self.ZScaleBox, 3, 0, 1, 2)
    manualgrid.addWidget(self.VScaleBox, 3, 2, 1, 2)
    manualgrid.addWidget(self.GNBox, 3, 4, 1, 2)
    
#   手动模式总体布局
    self.setLayout(manualgrid)

#   信息显示模块
    self.Xpos = QLCDNumber()
    self.Ypos = QLCDNumber()
    self.Zpos = QLCDNumber()
    self.Apos = QLCDNumber()
    self.infolayout = QGridLayout()
    self.infolayout.addWidget(self.Xpos, 0, 0)
    self.infolayout.addWidget(self.Ypos, 0, 1)
    self.infolayout.addWidget(self.Zpos, 1, 0)
    self.infolayout.addWidget(self.Apos, 1, 1)

    
    self.InfoBox.setLayout(self.infolayout)
    
    def setCommands(self, cmds):
        self.command = cmds
    def updateStatus(self):
        pos = self.command.get_pos()
        self.Xpos.setNumDigits(pos[0])
        self.Ypos.setNumDigits(pos[1])
        self.Zpos.setNumDigits(pos[2])
        self.Apos.setNumDigits(pos[3])
        
class StepView(QWidget):
  def __init__(self, parent = None):
    super(StepView, self).__init__(parent)
    
    self.iconlabel2 = QLabel()
#    self.vf0Img2 = QPixmap("E:\CopyShare\B03.jpg")
    self.vf0Img2 = QPixmap("/home/kinlin/CopyShare/B03.jpg")
    self.iconlabel2.setPixmap(self.vf0Img2)
    self.iconlabel2.setMargin(0)
    layout = QGridLayout()
    layout.addWidget(self.iconlabel2)
    self.setLayout(layout)

class AutoView(QWidget):
  def __init__(self, parent = None):
    super(AutoView, self).__init__(parent)
    
    self.iconlabel3 = QLabel()
#    self.vf0Img3 = QPixmap("E:\CopyShare\B04.jpg")
    self.vf0Img3 = QPixmap("/home/kinlin/CopyShare/B04.jpg")
    self.iconlabel3.setPixmap(self.vf0Img3)
    self.iconlabel3.setMargin(0)
    layout = QGridLayout()
    layout.addWidget(self.iconlabel3)
    
    self.setLayout(layout)
