#!/usr/bin/env python2
# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os
from view import *
from fontandString import *
from mode import *
from func import *
from stop import *
#import linuxcnc
import command


class RootWindow(QWidget):
    def __init__(self, parent = None):
        super(RootWindow, self).__init__(parent)
        self.viewframe = []
        self.make4Views(self.viewframe)
        self.setGeometry(240, 30, 800, 640)
        self.shortCutbind()
        self.vw = ViewManager(self.viewframe[0])
        self.fnc = FuncManager(self.viewframe[2], view = self.vw)
        self.md = Mode(self.viewframe[1], view = self.vw, func = self.fnc)
        self.st = Stop(self.viewframe[3])
    def shortCutbind(self):
        QShortcut(QKeySequence("Ctrl+T"), self, lambda: os.system('linuxcnctop &'))
        QShortcut(QKeySequence("Ctrl+M"), self, lambda: os.system('halmeter &'))
        QShortcut(QKeySequence("Ctrl+S"), self, lambda: os.system('halscope &'))

    def make4Views(self, viewframe):
        for i in range(4):
            self.viewframe.append(QGroupBox())
        for i in range(4):
            self.viewframe[i].setTitle(make4view[i])
#总体框架，分四份
        viewgrid = QGridLayout()
        viewgrid.addWidget(self.viewframe[0], 0, 0, 19, 19)
        viewgrid.addWidget(self.viewframe[1], 0, 19, 19, 3)
        viewgrid.addWidget(self.viewframe[2], 19, 0, 3, 15)
        viewgrid.addWidget(self.viewframe[3], 19, 15, 3, 7)
        self.setLayout(viewgrid)
        self.setWindowTitle(u"全电动折弯机")
#分别设置四个框架，其中vf0 用 stackWidget实现    
#vf1为垂直按键     vf2为底部功能按键     vf3为关机，伺服之类
    def setCommand(self, cmds):
        self.command = cmds
        self.vw.setcommand(cmds)
        self.fnc.setcommand(cmds)
        self.md.setcommand(cmds)
        self.st.setcommand(cmds)
    def updateStatus(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = RootWindow()
    form.show()
    app.exec_()
