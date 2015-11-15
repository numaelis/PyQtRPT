#example1 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT


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
        "image":"examples/pdf.png"
        }

#class myObject(QObject):
#    def __init__(self, parent):
#        QObject.__init__(self)
#        self.parent = parent
#    @QtCore.Slot(int, "QString", "QObject&", int)
#    def setValue(self, recNo, paramName, paramValue, reportPage):
#        if paramName == "customer":
#            paramValue = "I Am"
#        if paramName == "date":
#            paramValue = "12/12/12"
#        if paramName == "NN":
#            paramValue = recNo+1;
#        if paramName == "Goods":
#            print("hellow")
#            paramValue = table[recNo]["Goods"]
#        if paramName == "Quantity":
#            paramValue = table[recNo]["Quantity"]       
#        if paramName == "Price":
#            paramValue = table[recNo]["Price"]       
#        if paramName == "Sum":
#            paramValue = table[recNo]["Sum"]
#    @QtCore.Slot(int, "QString", "QImage&", int)
#    def setValueImage(self, recNo, paramName, paramValue, reportPage):
#        print(paramValue)
#        if paramName=="image":
#            paramValue.load("examples/pdf.png")

@QtCore.Slot(int, "QString", "QImage&", int)
def setValueImage(recNo, paramName, paramValue, reportPage):
    if paramName=="image":
        paramValue.load("examples/pdf.png")
        
@QtCore.Slot(int, "QString", "DataObject&", int)
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

report.loadReport("examples/examples_report/example1.xml")
bac=QPixmap("examples/examples_report/qt_background_portrait.png")
report.setBackgroundImage(bac)

report.setActivedSignal(True) 

report.recordCount =[len(table)]

#not works: QVariant&, python None
#o = myObject(0)
#QObject.connect(report, SIGNAL("setValue(int, QString, QObject&, int)"),
#                o, SLOT("setValue(int, QString, QObject&, int)"))

QObject.connect(report, SIGNAL("setValue(int, QString, DataObject&, int)"), 
                setValue)

QObject.connect(report, SIGNAL("setValueImage(int, QString, QImage&, int)"),
                setValueImage)

report.printExec(True)
form.show()
a.exec_()
