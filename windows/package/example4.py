#example4 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
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



a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example4.xml")
#bac=QPixmap("examples/examples_report/qt_background_portrait.png")
#report.setBackgroundImage(bac)

report.setActivedSignal(False) #desactive signal setValue and setValueImage
report.setTableMap([table], {})
report.recordCount =[len(table)]

report.printExec(True)
form.show()
a.exec_()
