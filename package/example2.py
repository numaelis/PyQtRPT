#example2 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside2 Numael Garay, mantrixsoft@gmail.com
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore

from PyQtRPT import PyQtRPT

table1=[]
table2=[]

for i in range(60):
    table1.append({"value":"DS1: "+ str(i+1)})

for i in range(55):
    table2.append({"value":"DS2: "+ str(i+1)})
        
a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example2.xml")
#bac=QPixmap("examples/examples_report/qt_background_portrait.png")
#report.setBackgroundImage(bac)

report.setActivedSignal(False) 

report.setTableMap([table1,table2], {})

report.recordCount =[len(table1)]
report.recordCount =[len(table2)]
                
report.printExec()

form.show()
a.exec_()
