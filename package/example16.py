#example16 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside2 Numael Garay, mantrixsoft@gmail.com
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore

from PyQtRPT import PyQtRPT

#Report defined SQL parameters


a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example16.xml")

strSQL ="SELECT * FROM artists ORDER BY lastname, firstname"

report.setUserSqlConnection(0, "DB1", "QSQLITE", "examples_report/example.sqlite", "", "", "", 0, "", strSQL)

report.printExec()
form.show()
a.exec_()
