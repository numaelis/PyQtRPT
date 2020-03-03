#example3 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside2 Numael Garay, mantrixsoft@gmail.com
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtPrintSupport import *
from PySide2 import QtCore

from PyQtRPT import PyQtRPT

mapOne={"FirstName":"Aleksey",
        "LastName":"Osipov",
        "Email":"aliks-os@ukr.net"}

@QtCore.Slot(int, "QString", "DataObject&", int)
def setValue(recNo, paramName, paramValue, reportPage):
    if paramName == "FirstName":
        paramValue.setValue(mapOne["FirstName"])
    if paramName == "LastName":
        paramValue.setValue(mapOne["LastName"])
    if paramName == "Email":
        paramValue.setValue(mapOne["Email"])
    
a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example3.xml")
#bac=QPixmap("examples/examples_report/qt_background_portrait.png")
#report.setBackgroundImage(bac)

report.setActivedSignal(True) 

QObject.connect(report, SIGNAL("setValue(int, QString, DataObject&, int)"), #pyside temporary solution
                setValue)


printer = QPrinter()
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOrientation(QPrinter.Portrait)
printer.setPaperSize(QPrinter.A4)
printer.setFullPage(True)


preview = QPrintPreviewWidget(printer)


preview.show()
preview.fitInView()             
QObject.connect(preview, SIGNAL("paintRequested(QPrinter*)"), report, SLOT("printPreview(QPrinter*)"))
preview.updatePreview()

           
form.show()

a.exec_()


