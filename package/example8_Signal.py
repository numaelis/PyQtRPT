#example8 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com

#Report with Autoheight

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT

table=[
    { "No" : 1, "Text" : "Qt Framework and tools can be installed using an online installer, offline installers, "
                  "or by building the source packages yourself. The online installers give you the option to "
                  "download or install only certain modules or add-ons. An offline installer is a single "
                  "package which contains all of Qt and Add-Ons relevant for a target platform."},
    

    { "No" : 2, "Text" : "The open-source versions are found at the Downloads page and the commercial versions are available for a free trial from Digia."},
    

    { "No" : 3, "Text" : "After downloading, start the installer like any executable on the development platform. "
          "Select the components that you want to install and follow the instructions of the "
          "installation program to complete the installation. Use the Maintenance Tool under "
          " <install_dir> to add, update, or remove installed components."},
    

    { "No" : 4, "Text" : "We invite you to explore the rest of Qt. We prepared overviews which help you decide which "
          "APIs to use and our examples demonstrate how to use them."},
    

    { "No" : 5, "Text" : "Qt features a wide range of different technologies. The following topics are key areas of "
          "functionality and can be used as a starting point for learning how to to get the most of Qt."},
    

    { "No" : 6, "Text" : "After downloading, start the installer like any executable on the development platform. "
          "Select the components that you want to install and follow the instructions of the "
          "installation program to complete the installation. Use the Maintenance Tool under "
          " <install_dir> to add, update, or remove installed components."},
    

    { "No" : 7, "Text" : "After downloading, start the installer like any executable on the development platform. "
          "Select the components that you want to install and follow the instructions of the "
          "installation program to complete the installation. Use the Maintenance Tool under "
          " <install_dir> to add, update, or remove installed components."},
   

    { "No" : 8, "Text" : "Qt features a wide range of different technologies. The following topics are key areas of "
          "functionality and can be used as a starting point for learning how to to get the most of Qt."},
    

    { "No" : 9, "Text" : "Qt features a wide range of different technologies. The following topics are key areas of "
          "functionality and can be used as a starting point for learning how to to get the most of Qt."},
    

    { "No" : 10, "Text" : "After downloading, start the installer like any executable on the development platform. "
          "Select the components that you want to install and follow the instructions of the "
          "installation program to complete the installation. Use the Maintenance Tool under "
          " <install_dir> to add, update, or remove installed components."},
    

    { "No" : 11, "Text" : "After downloading, start the installer like any executable on the development platform. "
          "Select the components that you want to install and follow the instructions of the "
          "installation program to complete the installation. Use the Maintenance Tool under "
          " <install_dir> to add, update, or remove installed components."},
    

    { "No" : 12, "Text" : "After downloading, start the installer like any executable on the development platform. "
          "Select the components that you want to install and follow the instructions of the "
          "installation program to complete the installation. Use the Maintenance Tool under "
          " <install_dir> to add, update, or remove installed components."},
    

    { "No" : 13, "Text" : "After downloading, start the installer like any executable on the development platform. "
          "Select the components that you want to install and follow the instructions of the "
          "installation program to complete the installation. Use the Maintenance Tool under "
          " <install_dir> to add, update, or remove installed components."},
    

    { "No" : 14, "Text" : "After downloading, start the installer like any executable on the development platform. "
          "Select the components that you want to install and follow the instructions of the "
          "installation program to complete the installation. Use the Maintenance Tool under "
          " <install_dir> to add, update, or remove installed components."},
    

    { "No" : 15, "Text" : "After downloading, start the installer like any executable on the development platform. "
          "Select the components that you want to install and follow the instructions of the "
          "installation program to complete the installation. Use the Maintenance Tool under "
          " <install_dir> to add, update, or remove installed components."},
    

   { "No" : 16, "Text" : "Qt features a wide range of different technologies. The following topics are key areas of "
          "functionality and can be used as a starting point for learning how to to get the most of Qt."}
]

        
@QtCore.Slot(int, "QString", "DataObject&", int)
def setValue(recNo, paramName, paramValue, reportPage):
    if paramName == "No":
        paramValue.setValue(str(table[recNo]["No"]))
    if paramName == "Text":
        paramValue.setValue(str(table[recNo]["Text"]))
        
a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

report.loadReport("examples_report/example8.xml")
#bac=QPixmap("examples/examples_report/qt_background_portrait.png")
#report.setBackgroundImage(bac)

report.setActivedSignal(True) #desactive signal setValue and setValueImage
report.setTableMap([table], {})
report.recordCount =[len(table)]

QObject.connect(report, SIGNAL("setValue(int, QString, DataObject&, int)"), #pyside temporary solution
                setValue)
                
report.printExec()
form.show()
a.exec_()

