import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT


table=[
	{"NN":"hola",
	  "Goods":"23",
	  "Quantity":"tio yuma",
	  "Price":"23",
	  "Sum":"23"},
	{"NN":"23",
	  "Goods":"23",
	  "Quantity":"jejeje",
	  "Price":44,
	  "Sum":"23"}
  ]
paramOne={
        "customer":"jean",
        "date":"30/12/15"
        }

#class myObject(QObject):
#    def __init__(self, parent):
#        QObject.__init__(self)
#        self.parent = parent
#    @QtCore.Slot(int, "QString", "QVariant&", int)#result = int, str, "QVariant", int
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
    
a = QApplication(sys.argv)
form = QDialog()
s= PyQtRPT.QtRPT()
archi=str("example1.xml")

s.loadReport(archi)
aa=QPixmap("qt_background_portrait.png")
s.setBackgroundImage(aa)

s.setTableMap(table)
s.setParamMapOne(paramOne)
s.recordCount =[len(table)]

#not works: QVariant&, python None
#o = myObject(0)
#QObject.connect(s, SIGNAL("setValue(int, QString, QVariant&, int)"),
#                o, SLOT("setValue(int, QString, QVariant&, int)"))

s.printExec(True)
form.show()
a.exec_()
