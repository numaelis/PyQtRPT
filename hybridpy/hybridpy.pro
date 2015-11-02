TEMPLATE = lib
QT += core gui sql
 
INCLUDEPATH += hybrid
INCLUDEPATH += ../hybrid
include(../QtRPT/QtRPT.pri)

INCLUDEPATH +=  /usr/lib/python3.4/site-packages/PySide/include/PySide
INCLUDEPATH +=  /usr/lib/python3.4/site-packages/PySide/include/PySide/QtCore
INCLUDEPATH +=  /usr/lib/python3.4/site-packages/PySide/include/PySide/QtGui
INCLUDEPATH +=  /usr/lib/python3.4/site-packages/PySide/include/shiboken
INCLUDEPATH +=  /usr/include/python3.4m
	

LIBS += /usr/lib/libpython3.4m.so.1.0 \
    /usr/lib/python3.4/site-packages/PySide/libshiboken.cpython-34m.so.1.2 \
    /usr/lib/python3.4/site-packages/PySide/libpyside.cpython-34m.so.1.2 \
    ../hybrid/libQtRptLib.a \
    ../hybrid/libQtZint.so
 
TARGET = ../PyQtRptLib
 
SOURCES += \
    PyQtRPT/pyqtrpt_module_wrapper.cpp \
    PyQtRPT/qtrpt_wrapper.cpp \
    PyQtRPT/rptbandobject_wrapper.cpp \
    PyQtRPT/rptfieldobject_wrapper.cpp \
    PyQtRPT/rptpageobject_wrapper.cpp \
    PyQtRPT/rptsql_wrapper.cpp \
    PyQtRPT/rptsqlconnection_wrapper.cpp \
    PyQtRPT/qtrptname_wrapper.cpp



