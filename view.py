# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from fontandString import *
import ui_PosInfo
class ViewManager(QWidget):
  def __init__(self, parent = None):
    super(ViewManager, self).__init__(parent)
    self.parent = parent
    self.vf0layout = QGridLayout()
    self.views = QStackedWidget()
    self.views.addWidget(ManualView(flag = 1))
    self.views.addWidget(StepView())
    self.views.addWidget(AutoView())
    self.views.addWidget(Welcome())
    self.views.setCurrentIndex(3)
    self.vf0layout.addWidget(self.views)
    self.vf0layout.setMargin(0)
    self.parent.setLayout(self.vf0layout)
  def setviewIndex(self, i=None):
    return self.views.setCurrentIndex(i)
  def setcommand(self, cmds):
    self.command = cmds    
    
class PosInfo(QWidget, ui_PosInfo.Ui_PosInfo):
    def __init__(self, parent = None):
        super(PosInfo, self).__init__(parent)
        self.setupUi(self)

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
  def __init__(self, parent = None, flag=None):
    super(ManualView, self).__init__(parent)
    self.flag = flag
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
    manualgrid.setContentsMargins(0, 5, 0, 0)
#   手动模式总体布局
    self.setLayout(manualgrid)

#   信息显示模块
#    self.pos= []
#    self.posInfo = []
#    self.unitmm = []
#    for i in range(4):
#        self.posInfo.append(QLCDNumber())
#    for i in range(4):
#        self.pos.append(QLabel(AXISES[i]))
#    for i in range(4):
#        self.unitmm.append(QLabel('mm'))
    self.infolayout = QGridLayout()
#    self.infolayout.addWidget(self.pos[0], 0, 0)
#    self.infolayout.addWidget(self.pos[1], 0, 1)
#    self.infolayout.addWidget(self.pos[2], 1, 0)
#    self.infolayout.addWidget(self.pos[3], 1, 1)
    self.posinfo = PosInfo()
    self.infolayout.addWidget(self.posinfo)
    self.infolayout.setContentsMargins(15, 0, 0, 0)
    self.InfoBox.setLayout(self.infolayout)
#    self.posinfo.connect(form, )
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
