#!/usr/bin/env python2
# # -*- coding: utf-8 -*-
#import linuxcnc
import sys,  os , time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from root import RootWindow
import view
import command
BASE = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), ".."))
sys.path.insert(0, os.path.join(BASE, "lib", "python"))
sys.excepthook = sys.__excepthook__

if sys.argv[1] != "-ini":
    raise SystemExit, "-ini must be first argument"
inifile = linuxcnc.ini(sys.argv[2])
machine_name = inifile.find('EMC','MACHINE') or "unknown"
print "machine name:",machine_name

#读取配置文件
open_directory = inifile.find("DISPLAY",  "PROGRAM_PREFIX")
max_feed_override = float(inifile.find("DISPLAY", "MAX_FEED_OVERRIDE"))
max_feed_override = int(max_feed_override * 100 +0.5)
max_spindle_override = float(inifile.find("DISPLAY", "MAX_SPINDLE_OVERRIDE") or max_feed_override)
max_spindle_override = int(max_spindle_override * 100 + 0.5)
jog_speed = (
    inifile.find("DISPLAY", "DEFAULT_LINEAR_VELOCITY")
    or inifile.find("TRAJ", "DEFAULT_LINEAR_VELOCITY")
    or inifile.find("TRAJ", "DEFAULT_VELOCITY")
    or 1.0)
jog_speed = (
    inifile.find("DISPLAY", "DEFAULT_ANGULAR_VELOCITY")
    or inifile.find("TRAJ", "DEFAULT_ANGULAR_VELOCITY")
    or inifile.find("TRAJ", "DEFAULT_VELOCITY")
    or jog_speed)
mlv = (
    inifile.find("DISPLAY","MAX_LINEAR_VELOCITY")
    or inifile.find("TRAJ","MAX_LINEAR_VELOCITY")
    or inifile.find("TRAJ","MAX_VELOCITY")
    or 1.0)
mav = (
    inifile.find("DISPLAY","MAX_ANGULAR_VELOCITY")
    or inifile.find("TRAJ","MAX_ANGULAR_VELOCITY")
    or inifile.find("TRAJ","MAX_VELOCITY")
    or mlv)             #vars.max_aspeed.set(float(mav))
mv = inifile.find("TRAJ","MAX_LINEAR_VELOCITY") or inifile.find("AXIS_0","MAX_VELOCITY") or 1.0
#vars.maxvel_speed.set(float(mv)*60)
#vars.max_maxvel.set(float(mv))
nmlfile = inifile.find("EMC", "NML_FILE")
print 'nmlfile: ', nmlfile

if nmlfile:
    emc.nmlfile = os.path.join(os.path.dirname(sys.argv[2]), nmlfile)
# coord_type, display_type
unit_values = {'inch': 1/25.4, 'mm': 1}         # 返回1mm与系统使用的单位的系统之间的转换系数，
def units(s, d=1.0):							 #  1) 系统使用inch，则1mm = 1/25.4inch
    try:                                         #  2) 系统使用mm, 1mm = 1mm
        return float(s)
    except ValueError:
        return unit_values.get(s, d)
slider_min = 0; aslider_min = 0
if inifile.find("DISPLAY", "MIN_LINEAR_VELOCITY"):
    slider_min = float(inifile.find("DISPLAY", "MIN_LINEAR_VELOCITY"))*60
elif inifile.find("DISPLAY", "MIN_VELOCITY"):
    aslider_min = float(inifile.find("DISPLAY", "MIN_VELOCITY"))*60
increments = inifile.find("DISPLAY", "INCREMENTS")
if increments:
    if "," in increments:
        increments = [i.strip() for i in increments.split(",")]
    else:
        increments = increments.split()
print "increment: ", increments
coordinate_display = inifile.find("DISPLAY", "POSITION_UNITS")
lu = units(inifile.find("TRAJ", "LINEAR_UNITS"))
print "lu: ", lu == 1/25.4
# update_ms 更新时间
update_ms = int(1000 * float(inifile.find("DISPLAY","CYCLE_TIME") or 0.020))
#建立根窗口
app = QApplication(sys.argv)
root_window = RootWindow()

#命令通道
c = linuxcnc.command()
s = linuxcnc.stat()
e = linuxcnc.error_channel()
cmds = command.commands(c, s, e)
#-------下列代码用于加载 Post HAL file  ,和post cmd .目前先不使用
#hp = os.path.expanduser("~/");
#postgui_halfile = inifile.find("HAL", "POSTGUI_HALFILE")
#post_cmd = "halcmd -f " + post_hal_file
#ret = os.system(post_cmd)
#if ret != 0:   #加载异常则打印异常信息并退出
#   print post_hal_file + " load error, exit ...!"
#   exit()
#s.poll()

#-------暂时不知用处。。。源自axis.py
s.poll()
print "s.axes: ",s.axes
statfail=0
statwait=.01
while s.axes == 0:
    print "waiting for s.axes"
    time.sleep(statwait)
    statfail+=1
    statwait *= 2
    if statfail > 8:
        raise SystemExit, (
            "A configuration error is preventing emc2 from starting.\n"
            "More information may be available when running from a terminal.")
    s.poll()

def showMessage(self, title, message):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(message)
        msgBox.setWindowTitlt(title)
        msgBox.exec_()

#为方便调试，此举暂时不调用    
#cmds.set_feedrate(100)
def error_task():
    error = e.poll()
    print "kinlin"
    if error:
        kind, text = error
        if kind in (linuxcnc.NML_ERROR,  linuxcnc.OPERATOR_ERROR):
            msgBox = QMessageBox().information(self,"ERROR", text)
        else: 
            msgBox = QMessageBox().information(self,"INFO", text)
#            QMessageBox.information(self, "INFO", unicode(text))
#             showMessage("INFO", unicode(text))
#    root_window.after(200, error_task())
    timer = QTimer()
    timer.timeout.connect(error_task())
    timer.setInterval(200)


def update():
    s.poll()
    root_window.updateStatus()
    error = e.poll()
    print "kinlin"
    if error:
        kind, text = error
        if kind in (linuxcnc.NML_ERROR,  linuxcnc.OPERATOR_ERROR):
            msgBox = QMessageBox().information(self,"ERROR", text)
        else: 
            msgBox = QMessageBox().information(self,"INFO", text)
#            QMessageBox.information(self, "INFO", unicode(text))
#             showMessage("INFO", unicode(text))
#    root_window.after(200, error_task())
#暂时先用 update_ms来更新error信息

update()
#timer = QTimer()
#timer.timeout.connect(update)
#timer.setInterval(200)  #timer.setInterval(update_ms)
#error_task()
root_window.show()
app.exec_()


