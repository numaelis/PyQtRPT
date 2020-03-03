#example1 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside2 Numael Garay, mantrixsoft@gmail.com
import sys,os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore

from PyQtRPT import PyQtRPT


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
        "date":"30/12/18",
        "image":"examples_report/picture.png"
        }

a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()
 
report.loadReport("examples_report/example1.xml")
bac=QPixmap("examples_report/qt_background_portrait.png")
report.setBackgroundImage(bac)

report.setActivedSignal(False) #desactive signal setValue and setValueImage
report.setTableMap([table], mapOne)
report.recordCount =[len(table)]


report.printExec(True)


#more options:
    #printExec(bool maximum = false, bool direct = false, QString printerName = QString()); -> report.printExec(True,True,"HP-Deskjet-D1400-series")
    #printPDF(const QString &filePath, bool open = true); -> report.printPDF("example1.pdf",False) or report.printPDF(os.getcwd()+QDir.separator()+"example1.pdf",True)
    #printHTML(const QString &filePath, bool open = true);
    #printXLSX(const QString &filePath, bool open = true);
    
form.show()
a.exec_()
