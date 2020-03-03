#example1 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside2 Numael Garay, mantrixsoft@gmail.com
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore

from PyQtRPT import PyQtRPT

table=[
	{"NN":1,
	  "Goods":"g0",
	  "Quantity":10,
	  "Price":100,
	  "Sum":1000},
	{"NN":2,
	  "Goods":"g1",
	  "Quantity":20,
	  "Price":200,
	  "Sum":4000},
      {"NN":3,
	  "Goods":"g2",
	  "Quantity":30,
	  "Price":300,
	  "Sum":9000}  
  ]
mapOne={
        "customer":"jean",
        "date":"30/12/15",
        "image":"examples_report/picture.png"
        }

#class myObject(QObject):
#    def __init__(self, parent):
#        QObject.__init__(self)
#        self.parent = parent
#    @QtCore.Slot(int, "QString", "DataObject&", int)
#    def setValue(self, recNo, paramName, paramValue, reportPage):
#        if paramName == "customer":
#            paramValue.setValue("I Am")
#        if paramName == "date":
#            paramValue.setValue("12/12/12")
#        if paramName == "NN":
#            paramValue.setValue(str(recNo+1))
#        if paramName == "Goods":
#            paramValue.setValue(str(table[recNo]["Goods"]))
#        if paramName == "Quantity":
#            paramValue.setValue(str(table[recNo]["Quantity"]))
#        if paramName == "Price":
#            paramValue.setValue(str(table[recNo]["Price"]))
#        if paramName == "Sum":
#            paramValue.setValue(str(table[recNo]["Sum"]))
#    @QtCore.Slot(int, "QString", "QImage&", int)
#    def setValueImage(self, recNo, paramName, paramValue, reportPage):
#        print(paramValue)
#        if paramName=="image":
#            paramValue.load(mapOne["image"])

@Slot(int, "QString", "QImage&", int)
def setValueImage(recNo, paramName, paramValue, reportPage):
    if paramName=="image":
        paramValue.load(mapOne["image"])
        
@Slot(int, "QString", "DataObject&", int)
def setValue(recNo, paramName, paramValue, reportPage):
    if paramName == "customer":
        paramValue.setValue("I Am")
    if paramName == "date":
        paramValue.setValue("12/12/12")
    if paramName == "NN":
        paramValue.setValue(str(recNo+1))
    if paramName == "Goods":
        paramValue.setValue(str(table[recNo]["Goods"]))
    if paramName == "Quantity":
        paramValue.setValue(str(table[recNo]["Quantity"]))
    if paramName == "Price":
        paramValue.setValue(str(table[recNo]["Price"]))
    if paramName == "Sum":
        paramValue.setValue(str(table[recNo]["Sum"]))
        
a = QApplication(sys.argv)

form = QDialog()

report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example1.xml")
bac=QPixmap("examples_report/qt_background_portrait.png")
report.setBackgroundImage(bac)

report.setActivedSignal(True) 

QObject.connect(report, SIGNAL ('setValue(int, QString, DataObject&, int)'), setValue)

QObject.connect(report, SIGNAL("setValueImage(int, QString, QImage&, int)"), setValueImage)

report.recordCount =[len(table)]
report.printExec(True)
form.show()
a.exec_()
