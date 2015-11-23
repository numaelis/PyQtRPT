#example5 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT

table=[]

for i in range(1,21):
    if i==3 or i==5 or i==7:
        quant = -i*10
    else:
        quant = i*10
    price =i*100
    suma = quant * price
    table.append({"NN":i,"Goods": "Goods "+str(i),"Quantity":quant,"Price":price,"Sum":suma})

#class myObject(QObject):
#    def __init__(self, parent):
#        QObject.__init__(self)
#        self.parent = parent
#    @QtCore.Slot(int, "QString", "QObject&", int)
#    def setValue(self, recNo, paramName, paramValue, reportPage):
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

        
@QtCore.Slot(int, "QString", "DataObject&", int)
def setValue(recNo, paramName, paramValue, reportPage):
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

report.loadReport("examples_report/example5.xml")
#bac=QPixmap("examples/examples_report/qt_background_portrait.png")
#report.setBackgroundImage(bac)

report.setActivedSignal(True) 

report.recordCount =[len(table)]

QObject.connect(report, SIGNAL("setValue(int, QString, DataObject&, int)"), #pyside temporary solution
                setValue)


report.printExec(True)
form.show()
a.exec_()
