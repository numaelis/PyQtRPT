#example13 QtRPT, Aleksey Osipov, E-mail: aliks-os@ukr.net
# to pyside Numael Garay, numaelis@gmail.com

#Creation report for user application without XML file

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtCore
import PyQtRPT


@QtCore.Slot("RptFieldObject&")
def setField(fieldObject):
    #print("hola")
    if fieldObject.name == "c1":
        fieldObject.value = "Column 1 Row "+str(fieldObject.recNo()+1)
        if (fieldObject.recNo() == 0):
            fieldObject.backgroundColor = Qt.yellow
        if (fieldObject.recNo() == 1):
            fieldObject.backgroundColor = Qt.magenta
        if (fieldObject.recNo() == 2):
            fieldObject.backgroundColor = Qt.cyan
        if (fieldObject.recNo() == 3):
            fieldObject.backgroundColor = Qt.green
            
    if fieldObject.name == "c2":
        fieldObject.value = "Column 2 Row "+str(fieldObject.recNo()+1)
        if (fieldObject.recNo() == 1):
            fieldObject.backgroundColor = Qt.yellow
        if (fieldObject.recNo() == 2):
            fieldObject.backgroundColor = Qt.magenta
        if (fieldObject.recNo() == 3):
            fieldObject.backgroundColor = Qt.cyan
        if (fieldObject.recNo() == 0):
            fieldObject.backgroundColor = Qt.green
    if (fieldObject.name == "c3"):
        fieldObject.value = "Column 3 Row "+str(fieldObject.recNo()+1)
        if (fieldObject.recNo() == 2):
            fieldObject.backgroundColor = Qt.yellow
        if (fieldObject.recNo() == 3):
            fieldObject.backgroundColor = Qt.magenta
        if (fieldObject.recNo() == 0):
            fieldObject.backgroundColor = Qt.cyan
        if (fieldObject.recNo() == 1):
            fieldObject.backgroundColor = Qt.green
    if (fieldObject.name == "c4") :
        fieldObject.value = "Column 4 Row "+str(fieldObject.recNo()+1)
        if (fieldObject.recNo() == 3):
            fieldObject.backgroundColor = Qt.yellow
        if (fieldObject.recNo() == 0):
            fieldObject.backgroundColor = Qt.magenta
        if (fieldObject.recNo() == 1):
            fieldObject.backgroundColor = Qt.cyan
        if (fieldObject.recNo() == 2):
            fieldObject.backgroundColor = Qt.green

a = QApplication(sys.argv)
form = QDialog()
report= PyQtRPT.QtRPT()

#//Make a page of report
page = PyQtRPT.RptPageObject()

page.pageNo=0
#report.pageList.append(page) #//Append page to the report -> error
report.addPage(page)#-> solution PySide
##//Make a ReportTitleBand
band1 = PyQtRPT.RptBandObject()
band1.name = "ReportTitle"
band1.height = 80
band1.type = PyQtRPT.QtRptName.BandType.ReportTitle
page.addBand(band1) #//Append band to the page
#
##//Make a field
field1 = PyQtRPT.RptFieldObject()
field1.name = "field1"
field1.fieldType = PyQtRPT.QtRptName.FieldType.Text
field1.rect.setTop(0)
field1.rect.setLeft(0)
field1.rect.setHeight(60)
field1.rect.setWidth(700)
field1.font.setBold(True)
field1.font.setPointSize(24)
field1.aligment = Qt.AlignCenter
field1.textWrap = 1
field1.value = "Creation of the report from user application without XML file"
field1.borderLeft = Qt.white
field1.borderRight = Qt.white
field1.borderBottom = Qt.white
field1.borderTop = Qt.white
band1.addField(field1)  #//Append field to the ReportTitleBand


#//Make a MasterHeaderBand
band2 = PyQtRPT.RptBandObject()
band2.name = "MasterHeaderBand"
band2.height = 30
band2.type = PyQtRPT.QtRptName.BandType.MasterHeader
page.addBand(band2) #//Append band to the page

#//Make a field
h1 = PyQtRPT.RptFieldObject()
h1.name = "h1"
h1.fieldType = PyQtRPT.QtRptName.FieldType.Text
h1.rect.setTop(0)
h1.rect.setLeft(0)
h1.rect.setHeight(30)
h1.rect.setWidth(150)
h1.value = "Header 1"
h1.font.setBold(True)
h1.setDefaultBackgroundColor(Qt.lightGray) #//Set default background color
h1.aligment = Qt.AlignCenter
band2.addField(h1)  #//Append field to the MasterHeaderBand

h2 = PyQtRPT.RptFieldObject()
h2.name = "h2"
h2.fieldType = PyQtRPT.QtRptName.FieldType.Text
h2.rect.setTop(0)
h2.rect.setLeft(149)
h2.rect.setHeight(30)
h2.rect.setWidth(150)
h2.value = "Header 2"
h2.font.setBold(True)
h2.setDefaultBackgroundColor(Qt.lightGray) #//Set default background color
h2.aligment = Qt.AlignCenter
band2.addField(h2)  #//Append field to the MasterHeaderBand

h3 = PyQtRPT.RptFieldObject()
h3.name = "h3"
h3.fieldType = PyQtRPT.QtRptName.FieldType.Text
h3.rect.setTop(0)
h3.rect.setLeft(298)
h3.rect.setHeight(30)
h3.rect.setWidth(150)
h3.value = "Header 3"
h3.font.setBold(True)
h3.setDefaultBackgroundColor(Qt.lightGray) #//Set default background color
h3.aligment = Qt.AlignCenter
band2.addField(h3)  #//Append field to the MasterHeaderBand

h4 = PyQtRPT.RptFieldObject()
h4.name = "h4"
h4.fieldType = PyQtRPT.QtRptName.FieldType.Text
h4.rect.setTop(0)
h4.rect.setLeft(447)
h4.rect.setHeight(30)
h4.rect.setWidth(150)
h4.value = "Header 4"
h4.font.setBold(True)
h4.setDefaultBackgroundColor(Qt.lightGray) #//Set default background color
h4.aligment = Qt.AlignCenter
band2.addField(h4)  #//Append field to the MasterHeaderBand

#//Make a MasterDataBand
band3 = PyQtRPT.RptBandObject()
band3.name = "MasterData"
band3.height = 30
band3.type = PyQtRPT.QtRptName.BandType.MasterData
page.addBand(band3) #//Append band to the page

#//Make a field
c1 = PyQtRPT.RptFieldObject()
c1.name = "c1"
c1.fieldType = PyQtRPT.QtRptName.FieldType.Text
c1.rect.setTop(0)
c1.rect.setLeft(0)
c1.rect.setHeight(30)
c1.rect.setWidth(150)
band3.addField(c1)  #//Append field to the MasterDataBand

c2 = PyQtRPT.RptFieldObject()
c2.name = "c2"
c2.fieldType = PyQtRPT.QtRptName.FieldType.Text
c2.rect.setTop(0)
c2.rect.setLeft(149)
c2.rect.setHeight(30)
c2.rect.setWidth(150)
band3.addField(c2)  #//Append field to the MasterDataBand

c3 = PyQtRPT.RptFieldObject()
c3.name = "c3"
c3.fieldType = PyQtRPT.QtRptName.FieldType.Text
c3.rect.setTop(0)
c3.rect.setLeft(298)
c3.rect.setHeight(30)
c3.rect.setWidth(150)
band3.addField(c3)  #//Append field to the MasterDataBand

c4 = PyQtRPT.RptFieldObject()
c4.name = "c4"
c4.fieldType = PyQtRPT.QtRptName.FieldType.Text
c4.rect.setTop(0)
c4.rect.setLeft(447)
c4.rect.setHeight(30)
c4.rect.setWidth(150)
band3.addField(c4)  #//Append field to the MasterDataBand

#//Make a PageFooterBand
band4 = PyQtRPT.RptBandObject()
band4.name = "PageFooterBand"
band4.height = 50
band4.type = PyQtRPT.QtRptName.BandType.PageFooter
page.addBand(band4) #//Append band to the page

pf = PyQtRPT.RptFieldObject()
pf.name = "pf"
pf.fieldType = PyQtRPT.QtRptName.FieldType.Text
pf.borderLeft = Qt.white
pf.borderRight = Qt.white
pf.borderBottom = Qt.white
pf.borderTop = Qt.white
pf.font.setBold(True)
pf.rect.setTop(0)
pf.rect.setLeft(330)
pf.rect.setHeight(30)
pf.rect.setWidth(150)
pf.value = "<Page> of <TotalPages>"
band4.addField(pf)  #//Append field to the PageFooterBand

report.setActivedSignal(True) 

QObject.connect(report, SIGNAL("setField(RptFieldObject &)"),
                setField)
report.recordCount =[4]
    
report.printExec()
form.show()
a.exec_()
