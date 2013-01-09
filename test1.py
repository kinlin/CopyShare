# # -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class RootWindow(QWidget):
    def __init__(self, parent = None):
        super(RootWindow, self).__init__(parent)
        layout = QGridLayout()
        tabwidget = QTabWidget()
        a = QPushButton("NO1")
        b = QPushButton("NO2")
        tabwidget.addTab(a, "NO1")
        tabwidget.addTab(b, "NO2")
        layout.addWidget(tabwidget)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = RootWindow()
    form.show()
    app.exec_()


