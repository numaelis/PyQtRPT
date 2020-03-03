#example11 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside2 Numael Garay, mantrixsoft@gmail.com
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore

from PyQtRPT import PyQtRPT

#Report with Barcode
table=[
    {"bar1":"L26125000001","bar2":"L26125000002"},
    {"bar1":"L26125000003","bar2":"L26125000004"},
    {"bar1":"L26125000005","bar2":"L26125000006"},
    {"bar1":"L26125000007","bar2":"L26125000008"},
    {"bar1":"L26125000009","bar2":"L26125000010"},
    {"bar1":"L26125000011","bar2":"L26125000012"},
    {"bar1":"L26125000013","bar2":"L26125000014"},
    {"bar1":"L26125000015","bar2":"L26125000016"},
    {"bar1":"L26125000017","bar2":"L26125000018"},
    {"bar1":"L26125000019","bar2":"L26125000020"}
    ]

#@QtCore.Slot(int, "QString", "DataObject&", int)
#def setValue(recNo, paramName, paramValue, reportPage):
#    if paramName == "bar1":
#        if (recNo*2+1 < 10):
#            tmp="0"+str(recNo*2+1)
#        else:
#            tmp=str(recNo*2+1)
#        paramValue.setValue("L261250000"+tmp)
#    if paramName == "bar2":
#        if (recNo*2+2 < 10):
#            tmp="0"+str(recNo*2+2)
#        else:
#            tmp=str(recNo*2+2)
#        paramValue.setValue("L261250000"+tmp)
    

a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example11.xml")
#bac=QPixmap("examples/examples_report/qt_background_portrait.png")
#report.setBackgroundImage(bac)

report.setActivedSignal(False) 
report.setTableMap([table], {})
report.recordCount =[len(table)]


#report.setActivedSignal(True) 
#QObject.connect(report, SIGNAL("setValue(int, QString, DataObject&, int)"), setValue)
#report.recordCount =[10]


report.printExec()
form.show()
a.exec_()
