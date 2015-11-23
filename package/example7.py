#example7 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com
#Diagram
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT
from PyQtRPT import *


table=[
        {"Month":"January","EUR":1222,"US":124,"Ukraine":1112,"Georgia":1256,"Other":1552},
         {"Month":"February","EUR":1452,"US":125,"Ukraine":1342,"Georgia":5612,"Other":1552},
         {"Month":"March","EUR":1662,"US":126,"Ukraine":1256,"Georgia":123,"Other":1222},
         {"Month":"April","EUR":4412,"US":127,"Ukraine":1255,"Georgia":1222,"Other":1452},
         {"Month":"May","EUR":1552,"US":128,"Ukraine":1232,"Georgia":126,"Other":1562},
         {"Month":"June","EUR":1662,"US":129,"Ukraine":1267,"Georgia":124,"Other":1266},
         {"Month":"July","EUR":1772,"US":1212,"Ukraine":1267,"Georgia":1244,"Other":1278},
         {"Month":"August","EUR":1882,"US":1211,"Ukraine":1278,"Georgia":1332,"Other":1266},
         {"Month":"September","EUR":1992,"US":1213,"Ukraine":1442,"Georgia":1255,"Other":1892},
         {"Month":"October","EUR":11112,"US":1212,"Ukraine":1212,"Georgia":1288,"Other":1234},
         {"Month":"November","EUR":1342,"US":1245,"Ukraine":1234,"Georgia":128,"Other":1222},
         {"Month":"December","EUR":1552,"US":1233,"Ukraine":1256,"Georgia":6612,"Other":1256}
        ]


@QtCore.Slot("Chart &")
def setValueDiagram(chart):
    if (chart.objectName() == "diagram1"):
        param= PyQtRPT.GraphParam()
        
        param.color=PyQtRPT.colorFromString("rgba(255,255,0,255)")
        param.valueReal = 150
        param.caption = "Graph 1"
      
        chart.setData(param)

        param.color = PyQtRPT.colorFromString("rgba(0,0,255,255)")
        param.valueReal = 70
        param.caption = "Graph 2"
        chart.setData(param)

        param.color = PyQtRPT.colorFromString("rgba(255,0,0,255)")
        param.valueReal = 220
        param.caption = "Graph 3"
        chart.setData(param)

        param.color = PyQtRPT.colorFromString("rgba(0,128,128,255)")
        param.valueReal = 30
        param.caption = "Graph 4"
        chart.setData(param,150)
        
@QtCore.Slot(int, "QString", "DataObject&", int)
def setValue(recNo, paramName, paramValue, reportPage):
    if paramName == "month":
        paramValue.setValue(table[recNo]["Month"])
    if paramName == "eur":
        paramValue.setValue(str(table[recNo]["EUR"]))
    if paramName == "us":
        paramValue.setValue(str(table[recNo]["US"]))
    if paramName == "ukraine":
        paramValue.setValue(str(table[recNo]["Ukraine"]))
    if paramName == "georgia":
        paramValue.setValue(str(table[recNo]["Georgia"]))
    if paramName == "other":
        paramValue.setValue(str(table[recNo]["Other"]))
    
    
a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.setActivedSignal(True) 

report.recordCount =[len(table)]

QObject.connect(report, SIGNAL("setValue(int, QString, DataObject&, int)"), #pyside temporary solution
                setValue)

QObject.connect(report, SIGNAL("setValueDiagram(Chart &)"),
                setValueDiagram)

if report.loadReport("examples/examples_report/example7.xml")==False:
    print("Report file not found")
    
report.printExec(True)
form.show()
a.exec_()
