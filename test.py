# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Tabvw(QWidget):
    def __init__(self, parent = None):
        super(Tabvw, self).__init__(parent)
        
        tabWidget = QTabWidget()
        
        bn1 = QPushButton("NO1")
        bn2 = QPushButton("NO2")
        bn3 = QPushButton("NO3")
        
        view = QStackedWidget()      

        
        tabWidget.addTab(view, "&manual")
        tabWidget.addTab(view, "&auto")
        tabWidget.addTab(view, "&single")
        tabWidget.setTabPosition(3)
        self.connect(tabWidget,SIGNAL("currentIndex(int)"),view,SLOT("setCurrentIndex(int)"))        
        
        layout = QGridLayout()
        layout.addWidget(tabWidget, 0, 0)
        
        self.setLayout(layout)

class mannual(QWidget):
    def __init__(self, parent=None):
        super(mannual, self).__init__(parent)
        
        label1 = QLable(u"第一个画面")
        layout = QGridLayout()
        layout.addWidget(label1)

class auto(QWidget):
    def __init__(self, parent=None):
        super(mannual, self).__init__(parent)
        
        label1 = QLable(u"第二个画面")
        layout = QGridLayout()
        layout.addWidget(label1)

class single(QWidget):
    def __init__(self, parent=None):
        super(mannual, self).__init__(parent)
        
        label1 = QLable(u"第三个画面")
        layout = QGridLayout()
        layout.addWidget(label1)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Tabvw()
    form.show()
    app.exec_()
