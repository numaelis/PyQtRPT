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
paramOne={
        "customer":"jean",
        "date":"30/12/15"
        }

#class myObject(QObject):
#    def __init__(self, parent):
#        QObject.__init__(self)
#        self.parent = parent
#    @QtCore.Slot(int, "QString", "QVariant&", int)
#    def setValue(self, recNo, paramName, paramValue, reportPage):
#        if paramName == "customer":
#            paramValue = "I Am"
#        if paramName == "date":
#            paramValue = "12/12/12"
#        if paramName == "NN":
#            paramValue = recNo+1;
#        if paramName == "Goods":
#            print("hellow")
#            #if (ui->tableWidget->item(recNo,0) == 0) return;
#            paramValue = table[recNo]["Goods"]
#        if paramName == "Quantity":
#           #if (ui->tableWidget->item(recNo,1) == 0) return;
#            paramValue = table[recNo]["Quantity"]       
#        if paramName == "Price":
#           #if (ui->tableWidget->item(recNo,2) == 0) return;
#            paramValue = table[recNo]["Price"]       
#        if paramName == "Sum":
#           #if (ui->tableWidget->item(recNo,3) == 0) return;
#            paramValue = table[recNo]["Sum"]
#    @QtCore.Slot(int, "QString", "QImage&", int)
#    def setValueImage(self, recNo, paramName, paramValue, reportPage):
#        print(paramValue)
#        if paramName=="image":
#            paramValue.load("examples/pdf.png")

@QtCore.Slot(int, "QString", "QImage&", int)
def setValueImage(recNo, paramName, paramValue, reportPage):
    print(paramValue)
    if paramName=="image":
        paramValue.load("examples/pdf.png")
        
a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()
file=str("examples/examples_report/example1.xml")

report.loadReport(file)
bac=QPixmap("examples/examples_report/qt_background_portrait.png")
report.setBackgroundImage(bac)
#add func in qtrpt:
report.setTableMap(table)
report.setParamMapOne(paramOne)
report.recordCount =[len(table)]

#not works: QVariant&, python None 
#o = myObject(0)
#QObject.connect(s, SIGNAL("setValue(int, QString, QVariant&, int)"),
#                o, SLOT("setValue(int, QString, QVariant&, int)"))
QObject.connect(report, SIGNAL("setValueImage(int, QString, QImage&, int)"),
                setValueImage)

report.printExec(True)
form.show()
a.exec_()
