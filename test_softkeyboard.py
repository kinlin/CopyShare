# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from softkeyboard import * 
from mywidget import *
class test(QWidget):
    def __init__(self):
        QWidget.__init__(self, windowTitle = u"测试软键盘")
        # self.lineedit = MyLineedit()
        # 对于不同的应用，可以传入不同的初始值
        self.label = EditLabel("hahaha")
        self.bn = QPushButton(u"测试")
        self.setLayout(QVBoxLayout())
        # self.layout().addWidget(self.lineedit)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.bn)
        
        # self.connect(VirtualKeyboard, SIGNAL("PushString"), self.getstring)
    def getstring(self, strings):
        self.label.setText(strings)


app = QApplication(sys.argv)
window = test()
window.show()
app.exec_()
