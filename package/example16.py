#example16 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com

#Report defined SQL parameters

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT


a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example16.xml")

strSQL ="SELECT * FROM artists ORDER BY lastname, firstname"

report.setUserSqlConnection(0, "DB1", "QSQLITE", "examples_report/example.sqlite", "", "", "", 0, "", strSQL)

report.printExec()
form.show()
a.exec_()
