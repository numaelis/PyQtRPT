#example17 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com


import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT
import random

doubleVector=[]
for i in range(15):
    doubleVector.append(32767 * (1/random.randint(2,100)))
        
@QtCore.Slot(int, "QString", "DataObject&", int)
def setValue(recNo, paramName, paramValue, reportPage):
    if paramName == "number":
        paramValue.setValue("%.2f" % round(doubleVector[recNo]/100, 2))
    
    
a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example17.xml")


report.setActivedSignal(True) 

report.recordCount =[len(doubleVector)]

QObject.connect(report, SIGNAL("setValue(int, QString, DataObject&, int)"), 
                setValue)


report.printExec()
form.show()
a.exec_()
