# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

modeString = (u"预览界面",u"手动模式", u"单步模式", u"自动模式", u"程序编辑", u"常量编辑", u"模具编辑", u"系统设置", u"帮助")
class RootWindow(QWidget):
    def __init__(self, parent = None):
        super(RootWindow, self).__init__(parent)
        self.viewframe = []
        self.make4Views(self.viewframe)
        self.setGeometry(240, 30, 800, 640)
    def make4Views(self, viewframe):
         vf0 = QGroupBox()
         vf0.setTitle("A")
         vf1 = QGroupBox()
         vf1.setTitle("B")
         vf2 = QGroupBox()
         vf2.setTitle("C")
         vf3 = QGroupBox()
         vf3.setTitle("D")
         for i in range(4):
             self.viewframe.append(QWidget())
         
         
#总体框架，分四份
         viewgrid = QGridLayout()
         viewgrid.addWidget(viewframe[0], 0, 0, 19, 19)
         viewgrid.addWidget(viewframe[1], 0, 19, 19, 3)
         viewgrid.addWidget(viewframe[2], 19, 0, 3, 15)
         viewgrid.addWidget(viewframe[3], 19, 15, 3, 7)

         self.setLayout(viewgrid)
         self.setWindowTitle(u"全电动折弯机")

#分别设置四个框架，其中vf0 用 stackWidget实现    vf1为垂直按键     vf2为底部功能按键     vf3为关机，伺服之类
#----------------------------------------------左上模块
         vf0layout = QGridLayout()
         vf0view = QFrame()         
         self.iconlabel1 = QLabel()
         self.iconlabel2 = QLabel()
         self.iconlabel3 = QLabel()         
         vf0Img1 = QPixmap("E:\CopyShare\B02.jpg")
         vf0Img2 = QPixmap("E:\CopyShare\B03.jpg")
         vf0Img3 = QPixmap("E:\CopyShare\B04.jpg")

         self.iconlabel1.setPixmap(vf0Img1)
         self.iconlabel1.setMargin(0)         
         self.iconlabel2.setPixmap(vf0Img2)
         self.iconlabel2.setMargin(0)
         self.iconlabel3.setPixmap(vf0Img3)
         self.iconlabel3.setMargin(0)
         
         self.vf0viewwid = QStackedWidget()
         self.vf0viewlayout = QGridLayout()
         self.vf0viewwid.addWidget(self.iconlabel1)
         self.vf0viewwid.addWidget(self.iconlabel2)
         self.vf0viewwid.addWidget(self.iconlabel3)
         self.vf0viewwid.setCurrentIndex(0)
         
         self.vf0viewlayout.addWidget(self.vf0viewwid)
         
         vf0view.setLayout(self.vf0viewlayout)
         
         vf0layout.addWidget(vf0, 0, 0)
         vf0layout.addWidget(vf0view, 0, 0)
         vf0layout.setMargin(0)         
         viewframe[0].setLayout(vf0layout)
#----------------------------------------------右上模块         
         self.vf1layout = QVBoxLayout()
         self.vf1layout.addWidget(vf1)
         self.vf1viewlyout = QVBoxLayout()
         vf1.setLayout(self.vf1viewlyout)
         
         self.modebn = []
         for i in range(1, 9):
             self.modebn.append(QPushButton(modeString[i]))
         for i in range(8):
             self.vf1viewlyout.insertWidget(i, self.modebn[i])
         self.vf1layout.setMargin(0)
         viewframe[1].setLayout(self.vf1layout)

#-------------------------------------------------左下模块
         vf2bt1 = QPushButton(u"测试1")
         vf2bt2 = QPushButton(u"测试2")
         vf2bt3 = QPushButton(u"测试3")
         
         vf2layout = QGridLayout()
         vf2layout.addWidget(vf2, 0, 0)
         vf2layout.setMargin(0)
         
         vf2viewlayout = QHBoxLayout()
         vf2viewlayout.addWidget(vf2bt1)
         vf2viewlayout.addWidget(vf2bt2)
         vf2viewlayout.addWidget(vf2bt3)
         vf2.setLayout(vf2viewlayout)
         
         viewframe[2].setLayout(vf2layout)
         


#-------------------------------------------------右下模块
         vf3bt1 = QPushButton(u"伺服")
         vf3bt2 = QPushButton(u"关机")
         
         vf3layout = QGridLayout()
         vf3layout.addWidget(vf3, 0, 0)
         vf3layout.setMargin(0)  
         
         vf3viewlayout = QHBoxLayout()
         vf3viewlayout.addWidget(vf3bt1)
         vf3viewlayout.addWidget(vf3bt2)
         vf3.setLayout(vf3viewlayout)
         
         viewframe[3].setLayout(vf3layout)

#         self.connect(self.modebn[1], SIGNAL("isFlat(int)"), self.vf0viewwid, SLOT("setCurrentIndex(int)"))
         for i in range(8):
             self.connect(self.modebn[i], SIGNAL("clicked()"), self.clicked)
         
    def anyButton(self, who):
        self.label1.setText(u"你按了'%s'键" % who)
         
    def clicked(self):
        button = self.sender()
        if button is None or not isinstance(button,  QPushButton):
            return
#        self.iconlabel1.setText(u"%s" %self.vf1viewlyout.indexOf(button))
        self.vf0viewwid.setCurrentIndex(self.vf1viewlyout.indexOf(button))
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
