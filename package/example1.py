#example1 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com
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
mapOne={
        "customer":"jean",
        "date":"30/12/15",
        "image":"examples/pdf.png"
        }


a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples/examples_report/example1.xml")
bac=QPixmap("examples/examples_report/qt_background_portrait.png")
report.setBackgroundImage(bac)

report.setActivedSignal(False) #desactive signal setValue and setValueImage
report.setTableMap([table], mapOne)
report.recordCount =[len(table)]

report.printExec(True)
form.show()
a.exec_()
