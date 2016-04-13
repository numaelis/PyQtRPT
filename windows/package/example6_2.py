#example6_2 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com

#Report with grouping data Master Data Band 2

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT


table=[
{"Market":"US", "Goods":"Goods 0", "Quantity":0, "Price":0,"Sum":0},
{"Market":"Europe", "Goods":"Goods 1", "Quantity":10, "Price":100,"Sum":1000},
{"Market":"Ukraine", "Goods":"Goods 2", "Quantity":20, "Price":200,"Sum":2000},
{"Market":"US", "Goods":"Goods 3", "Quantity":30, "Price":300,"Sum":3000},
{"Market":"Georgia", "Goods":"Goods 4", "Quantity":40, "Price":400,"Sum":4000},
{"Market":"Europe", "Goods":"Goods 5", "Quantity":50, "Price":500,"Sum":5000},
{"Market":"Georgia", "Goods":"Goods 6", "Quantity":60, "Price":600,"Sum":6000},
{"Market":"US", "Goods":"Goods 7", "Quantity":70, "Price":700,"Sum":7000},
{"Market":"US", "Goods":"Goods 8", "Quantity":80, "Price":800,"Sum":8000},
{"Market":"Europe", "Goods":"Goods 9", "Quantity":90, "Price":900,"Sum":9000},
{"Market":"Ukraine", "Goods":"Goods 10", "Quantity":100, "Price":1000,"Sum":10000},
{"Market":"Georgia", "Goods":"Goods 11", "Quantity":110, "Price":1100,"Sum":11000},
{"Market":"Ukraine", "Goods":"Goods 12", "Quantity":120, "Price":1200,"Sum":12000},
{"Market":"Georgia", "Goods":"Goods 13", "Quantity":130, "Price":1300,"Sum":13000},
{"Market":"Europe", "Goods":"Goods 14", "Quantity":140, "Price":1400,"Sum":14000},
{"Market":"Other", "Goods":"Goods 15", "Quantity":150, "Price":1500,"Sum":15000},
{"Market":"Other", "Goods":"Goods 16", "Quantity":160, "Price":1600,"Sum":16000},
{"Market":"Other", "Goods":"Goods 17", "Quantity":170, "Price":1700,"Sum":17000},
{"Market":"Other", "Goods":"Goods 18", "Quantity":180, "Price":1800,"Sum":18000},
{"Market":"Other", "Goods":"Goods 19", "Quantity":190, "Price":1900,"Sum":19000},
{"Market":"Other", "Goods":"Goods 20", "Quantity":200, "Price":2000,"Sum":20000},
{"Market":"Other", "Goods":"Goods 21", "Quantity":210, "Price":2100,"Sum":21000},
{"Market":"Other", "Goods":"Goods 22", "Quantity":220, "Price":2200,"Sum":22000},
{"Market":"Other", "Goods":"Goods 23", "Quantity":230, "Price":2300,"Sum":23000},
{"Market":"Other", "Goods":"Goods 24", "Quantity":240, "Price":2400,"Sum":24000},
{"Market":"US", "Goods":"Goods 25", "Quantity":250, "Price":2500,"Sum":25000},
{"Market":"Other", "Goods":"Goods 26", "Quantity":260, "Price":2600,"Sum":26000}
]



a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example6b.xml")
#bac=QPixmap("examples/examples_report/qt_background_portrait.png")
#report.setBackgroundImage(bac)

report.setActivedSignal(False) #desactive signal setValue and setValueImage
report.setTableMap([table], {})
report.recordCount =[len(table)]

report.printExec()
form.show()
a.exec_()
