#example2 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT

table1=[]
table2=[]

for i in range(60):
    table1.append({"value":"DS1: "+ str(i+1)})

for i in range(55):
    table2.append({"value":"DS2: "+ str(i+1)})

@QtCore.Slot(int, "QString", "DataObject&", int)
def setValue(recNo, paramName, paramValue, reportPage):
    if paramName == "value":
        if reportPage == 0:
            paramValue.setValue(str(table1[recNo]["value"]))
        else:
            paramValue.setValue(str(table2[recNo]["value"]))
    
        
a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples/examples_report/example2.xml")
#bac=QPixmap("examples/examples_report/qt_background_portrait.png")
#report.setBackgroundImage(bac)

report.setActivedSignal(True) 

report.recordCount =[len(table1)]
report.recordCount =[len(table2)]

QObject.connect(report, SIGNAL("setValue(int, QString, DataObject&, int)"), #pyside temporary solution
                setValue)
                
report.printExec()
form.show()
a.exec_()
