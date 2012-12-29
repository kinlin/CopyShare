# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import view
#import linuxcnc

modeString = (u"手动模式", u"单步模式", u"自动模式", u"程序编辑", u"常量编辑", u"模具编辑", u"系统设置", u"帮助")
funcViewTitles = (u'功能按钮-手动模式', u'功能按钮-单步模式', u'功能按钮-自动模式',
                  u'功能按钮-程序编辑', u'功能按钮-常量编辑',
                  u'功能按钮-模具编辑', u'功能按钮-系统设置', u'功能按钮-帮助')
                  
class RootWindow(QWidget):
    def __init__(self, parent = None):
        super(RootWindow, self).__init__(parent)
        self.viewframe = []
        self.make4Views(self.viewframe)
        self.setGeometry(240, 30, 800, 640)
    def make4Views(self, viewframe):
         self.vf0 = QGroupBox()
         self.vf0.setTitle(u"欢迎使用")
         self.vf1 = QGroupBox()
         self.vf1.setTitle(u"模式切换")
         self.vf2 = QGroupBox()
         self.vf2.setTitle("C")
         self.vf3 = QGroupBox()
         self.vf3.setTitle("D")
         for i in range(4):
             self.viewframe.append(QWidget())
         
         
#总体框架，分四份
         viewgrid = QGridLayout()
         viewgrid.addWidget(self.vf0, 0, 0, 19, 19)
         viewgrid.addWidget(self.vf1, 0, 19, 19, 3)
         viewgrid.addWidget(self.vf2, 19, 0, 3, 15)
         viewgrid.addWidget(self.vf3, 19, 15, 3, 7)
         self.setLayout(viewgrid)
         self.setWindowTitle(u"全电动折弯机")
#分别设置四个框架，其中vf0 用 stackWidget实现    vf1为垂直按键     vf2为底部功能按键     vf3为关机，伺服之类
#----------------------------------------------左上模块
         vf0layout = QGridLayout()       
         
         self.vf0viewwid = QStackedWidget()
         self.viewframe0 = view.Welcome()
         self.viewframe1 = view.ManualView()
         self.viewframe2 = view.StepView()
         self.viewframe3 = view.AutoView()
         
         self.vf0viewwid.addWidget(self.viewframe0)
         self.vf0viewwid.addWidget(self.viewframe1)
         self.vf0viewwid.addWidget(self.viewframe2)
         self.vf0viewwid.addWidget(self.viewframe3)
         self.vf0viewwid.setCurrentIndex(0)
        
         vf0layout.addWidget(self.vf0viewwid, 0, 0)
         vf0layout.setMargin(0)         

         self.vf0.setLayout(vf0layout)
#----------------------------------------------右上模块         
         self.vf1layout = QVBoxLayout()         
         self.modebn = []
         for i in range(8):
             self.modebn.append(QPushButton(modeString[i]))
         for i in range(8):
             self.vf1layout.insertWidget(i, self.modebn[i])
         self.vf1layout.setMargin(0)
         self.vf1.setLayout(self.vf1layout)

#-------------------------------------------------左下模块
         vf2bt1 = QPushButton(u"测试1")
         vf2bt2 = QPushButton(u"测试2")
         vf2bt3 = QPushButton(u"测试3")
         
         self.vf2layout = QGridLayout()
         self.vf2layout.addWidget(vf2bt1, 0, 0)
         self.vf2layout.addWidget(vf2bt2, 0, 1)
         self.vf2layout.addWidget(vf2bt3, 0, 2)
         
         self.vf2.setLayout(self.vf2layout)
         


#-------------------------------------------------右下模块
         vf3bt1 = QPushButton(u"伺服")
         vf3bt2 = QPushButton(u"关机")
         
         vf3layout = QGridLayout()
         vf3layout.setMargin(0)  
         
         vf3layout.addWidget(vf3bt1, 0, 0)
         vf3layout.addWidget(vf3bt2, 0, 1)
         self.vf3.setLayout(vf3layout)
         
         for i in range(8):
             self.connect(self.modebn[i], SIGNAL("clicked()"), self.clicked)
             
    def setviewframe(self):     
        viewframe = view.ManualView()
    
         
    def clicked(self):
        button = self.sender()
        if button is None or not isinstance(button,  QPushButton):
            return
        index = self.vf1layout.indexOf(button)
        self.vf0viewwid.setCurrentIndex(index + 1)
        self.vf0.setTitle(modeString[index])
###################################
#布局右边的按钮
#####################
class viewManager(QWidget):
    def __init__(self, parent = None):
        super(viewManager, self).__init__(parent)  
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = RootWindow()
    form.show()
    app.exec_()
