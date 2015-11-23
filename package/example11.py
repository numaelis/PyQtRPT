#example11 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com

#Report with Barcode

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT

@QtCore.Slot(int, "QString", "DataObject&", int)
def setValue(recNo, paramName, paramValue, reportPage):
    if paramName == "bar1":
        if (recNo*2+1 < 10):
            tmp="0"+str(recNo*2+1)
        else:
            tmp=str(recNo*2+1)
        paramValue.setValue("L261250000"+tmp)
    if paramName == "bar2":
        if (recNo*2+2 < 10):
            tmp="0"+str(recNo*2+2)
        else:
            tmp=str(recNo*2+2)
        paramValue.setValue("L261250000"+tmp)
    

a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example11.xml")
#bac=QPixmap("examples/examples_report/qt_background_portrait.png")
#report.setBackgroundImage(bac)

report.setActivedSignal(True) 

report.recordCount =[10]

QObject.connect(report, SIGNAL("setValue(int, QString, DataObject&, int)"), #pyside temporary solution
                setValue)


report.printExec()
form.show()
a.exec_()
