TEMPLATE = lib
QT += core gui sql
 #qmake -config release
INCLUDEPATH += ../hybrid
INCLUDEPATH += c:/Qt/4.8.6/include
INCLUDEPATH += c:/Qt/4.8.6/include/QtCore
INCLUDEPATH += c:/Qt/4.8.6/include/QtGui
include(../QtRPT/QtRPT.pri)

INCLUDEPATH +=  c:/python34/lib/site-packages/pyside/include/pyside
INCLUDEPATH +=  c:/python34/lib/site-packages/pyside/include/pyside/qtcore
INCLUDEPATH +=  c:/python34/lib/site-packages/pyside/include/pyside/qtgui
INCLUDEPATH +=  c:/python34/lib/site-packages/pyside/include/shiboken
INCLUDEPATH +=  c:/python34/include

	
LIBS += \
    c:/python34/libs/python34.lib \
    c:/python34/lib/site-packages/PySide/shiboken-python3.4.lib \
    c:/python34/lib/site-packages/PySide/pyside-python3.4.lib \
    ../hybrid/QtRPTaps.lib \
    ../hybrid/QtZint.lib
 
TARGET = ../PyQtRPT
 
SOURCES += \
    PyQtRPT/pyqtrpt_module_wrapper.cpp \
    PyQtRPT/qtrpt_wrapper.cpp \
    PyQtRPT/dataobject_wrapper.cpp \
    PyQtRPT/rptbandobject_wrapper.cpp \
    PyQtRPT/rptfieldobject_wrapper.cpp \
    PyQtRPT/rptpageobject_wrapper.cpp \
    PyQtRPT/rptsql_wrapper.cpp \
    PyQtRPT/rptsqlconnection_wrapper.cpp \
    PyQtRPT/qtrptname_wrapper.cpp \
    PyQtRPT/barcode_wrapper.cpp \
    PyQtRPT/chart_wrapper.cpp \
    PyQtRPT/graphparam_wrapper.cpp \
    PyQtRPT/aggregatevalues_wrapper.cpp\
    PyQtRPT/rpttabelement_wrapper.cpp \
    PyQtRPT/rptcrosstabobject_wrapper.cpp

