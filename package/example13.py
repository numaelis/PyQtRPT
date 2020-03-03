#example13 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside2 Numael Garay, mantrixsoft@gmail.com
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore

from PyQtRPT import PyQtRPT

@QtCore.Slot("RptFieldObject&")
def setField(fieldObject):
    fieldObject2 = fieldObject.parentBand.parentReportPage.findFieldObjectByName("field2")
    if fieldObject.name == "field1":
        fieldObject.value = "Get control of report building!"
        fieldObject.aligment = Qt.AlignVCenter | Qt.AlignHCenter
        fieldObject.rect.setWidth(fieldObject.parentBand.width)
        fieldObject.rect.setLeft(0)
        fieldObject.rect.setTop(0)

        fieldObject.borderBottom = Qt.white
        fieldObject.borderTop = Qt.white
        fieldObject.borderLeft = Qt.white
        fieldObject.borderRight = Qt.white

        fieldObject.font.setBold(True)
        fieldObject.font.setPointSize(16)
    if (fieldObject.name == "field2" or fieldObject.name == "field3" or fieldObject.name == "field4" or fieldObject.name == "field5"):
        fieldObject.borderBottom = Qt.blue
        fieldObject.borderTop = Qt.blue
        fieldObject.borderLeft = Qt.blue
        fieldObject.borderRight = Qt.blue
        fieldObject.borderWidth = 1
        fieldObject.aligment = Qt.AlignLeft | Qt.AlignHCenter
        fieldObject.rect.setTop(0)
        fieldObject.rect.setHeight(20)
        fieldObject.rect.setWidth(150)
    if (fieldObject.name == "field2"):
        fieldObject.value = "Column 1 Row "+str(fieldObject.recNo())
        fieldObject.rect.setLeft(0)
        fieldObject.parentBand.height = fieldObject.rect.height()  #Change the hight of the band

        if (fieldObject.recNo() == 0):
            fieldObject.backgroundColor = Qt.yellow
        if (fieldObject.recNo() == 1):
            fieldObject.backgroundColor = Qt.magenta
        if (fieldObject.recNo() == 2):
            fieldObject.backgroundColor = Qt.cyan
    if (fieldObject.name == "field3") :
        fieldObject.value = "Column 2 Row "+str(fieldObject.recNo())
        if (fieldObject2 != 0):
            fieldObject.rect.setLeft(fieldObject2.rect.width() * 1)
        
        fieldObject.parentBand.height = fieldObject.rect.height()  #Change the hight of the band

        if (fieldObject.recNo() == 1):
            fieldObject.backgroundColor = Qt.yellow
        if (fieldObject.recNo() == 2):
            fieldObject.backgroundColor = Qt.magenta
        if (fieldObject.recNo() == 0):
            fieldObject.backgroundColor = Qt.cyan
    
    if (fieldObject.name == "field4"):
        fieldObject.value = "Column 3 Row "+ str(fieldObject.recNo())
        if (fieldObject2 != 0):
            fieldObject.rect.setLeft(fieldObject2.rect.width() * 2)
        
        fieldObject.parentBand.height = fieldObject.rect.height()  #Change the hight of the band

        if (fieldObject.recNo() == 2):
            fieldObject.backgroundColor = Qt.yellow
        if (fieldObject.recNo() == 0):
            fieldObject.backgroundColor = Qt.magenta
        if (fieldObject.recNo() == 1):
            fieldObject.backgroundColor = Qt.cyan
    
    if (fieldObject.name == "field5") :
        fieldObject.value = "Column 4 Row "+str(fieldObject.recNo())
        if (fieldObject2 != 0) :
            fieldObject.rect.setLeft(fieldObject2.rect.width() * 3)
        
        fieldObject.parentBand.height = fieldObject.rect.height()  #Change the hight of the band

        if (fieldObject.recNo() == 0):
            fieldObject.backgroundColor = Qt.yellow
        if (fieldObject.recNo() == 1):
            fieldObject.backgroundColor = Qt.magenta
        if (fieldObject.recNo() == 2):
            fieldObject.backgroundColor = Qt.cyan
    

a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()
if report.loadReport("examples_report/example13.xml")==False:
    print("Report file not found")
report.setActivedSignal(True) 

QObject.connect(report, SIGNAL("setField(RptFieldObject &)"),
                setField)

report.recordCount =[3]
    
report.printExec(True)
form.show()
a.exec_()
