#example12 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside2 Numael Garay, mantrixsoft@gmail.com
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore

from PyQtRPT import PyQtRPT

#Report with Richtext Fields

@QtCore.Slot(int, "QString", "DataObject&", int)
def setValue(recNo, paramName, paramValue, reportPage):
    if (paramName == "text1"):
        if (recNo == 0):
            paramValue.setValue("Mary")
        if (recNo == 1):
            paramValue.setValue("Ella")
        if (recNo == 2):
            paramValue.setValue("Vera")
        
    if (paramName == "text2"):
        if (recNo == 0):
            paramValue.setValue("chocolate")
        if (recNo == 1):
            paramValue.setValue("banana")
        if (recNo == 2):
            paramValue.setValue("apple")
        
    if (paramName == "text4"):
            paramValue.setValue("<body><font size=5>This тект is formatted by the user by means of HTML tags. You can do the text <b>bold</b>, "
                         "<i>italics</i>, <u>underline</u>. To allocate separate words in various color, as example: <font color=#0000FF>blue</font>, "
                         "<font color=#FF0000>red</font>, <font color=#CC6633>brown</font>, <font color=#00FF00>green</font> etc</font></body>")
        

a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example12.xml")
#bac=QPixmap("examples/examples_report/qt_background_portrait.png")
#report.setBackgroundImage(bac)

report.setActivedSignal(True) 

report.recordCount =[3]

QObject.connect(report, SIGNAL("setValue(int, QString, DataObject&, int)"), #pyside temporary solution
                setValue)


report.printExec()
form.show()
a.exec_()
