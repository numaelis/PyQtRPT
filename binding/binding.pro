TEMPLATE = lib
QT += core
#gui xml sql widgets printsupport

INCLUDEPATH += ../QtRPT
INCLUDEPATH += ../bin/release/lib/
include(../QtRPT/QtRPT.pri)
include(../QtRPT/config.pri)
linux{
    CONFIG += plugin
}
linux{
    INCLUDEPATH +=  ~/.local/lib/python3.5/site-packages/PySide2/include/PySide2/
    INCLUDEPATH +=  ~/.local/lib/python3.5/site-packages/PySide2/include/PySide2/QtCore
    INCLUDEPATH +=  ~/.local/lib/python3.5/site-packages/PySide2/include/PySide2/QtGui

    INCLUDEPATH +=  ~/.local/lib/python3.5/site-packages/PySide2/include/PySide2/QtWidgets
    INCLUDEPATH +=  ~/.local/lib/python3.5/site-packages/PySide2/include/PySide2/QtPrintSupport
    INCLUDEPATH +=  ~/.local/lib/python3.5/site-packages/PySide2/include/PySide2/QtSql
    INCLUDEPATH +=  ~/.local/lib/python3.5/site-packages/PySide2/include/PySide2/QtXml
    INCLUDEPATH +=  ~/.local/lib/python3.5/site-packages/PySide2/include/shiboken2/
    INCLUDEPATH +=  /usr/include/python3.5m/
    INCLUDEPATH +=  ~/Qt5.9.6/5.9.6/gcc_64/include/
    INCLUDEPATH +=  ~/Qt5.9.6/5.9.6/gcc_64/include/QtCore
    INCLUDEPATH +=  ~/Qt5.9.6/5.9.6/gcc_64/include/QtGui
    INCLUDEPATH +=  ~/Qt5.9.6/5.9.6/gcc_64/include/QtWidgets
    INCLUDEPATH +=  ~/Qt5.9.6/5.9.6/gcc_64/include/QtPrintSupport
    INCLUDEPATH +=  ~/Qt5.9.6/5.9.6/gcc_64/include/QtSql
    INCLUDEPATH +=  ~/Qt5.9.6/5.9.6/gcc_64/include/QtXml


    LIBS += /usr/lib/x86_64-linux-gnu/libpython3.5m.so.1.0 \
        ~/.local/lib/python3.5/site-packages/PySide2/libshiboken2.abi3.so.5.9 \
        ~/.local/lib/python3.5/site-packages/PySide2/libpyside2.abi3.so.5.9# \
    #    ../bin/release/lib/libQtRPTaps.so# \ # adaptation pyside
    #    ../bin/release/lib/libQtZint.so \
    #    ../bin/release/lib/libQtXlsx.so
}
win32{
    INCLUDEPATH +=  C:/Python36/Lib/site-packages/PySide2/include/PySide2/
    INCLUDEPATH +=  C:/Python36/Lib/site-packages/PySide2/include/PySide2/QtCore
    INCLUDEPATH +=  C:/Python36/Lib/site-packages/PySide2/include/PySide2/QtGui
    INCLUDEPATH +=  C:/Python36/Lib/site-packages/PySide2/include/PySide2/QtWidgets
    INCLUDEPATH +=  C:/Python36/Lib/site-packages/PySide2/include/PySide2/QtPrintSupport
    INCLUDEPATH +=  C:/Python36/Lib/site-packages/PySide2/include/PySide2/QtSql
    INCLUDEPATH +=  C:/Python36/Lib/site-packages/PySide2/include/PySide2/QtXml
    INCLUDEPATH +=  C:/Python36/Lib/site-packages/PySide2/include/shiboken2/
    INCLUDEPATH +=  C:/Python36/include
    INCLUDEPATH +=  C:/Qt/Qt5.9.6/5.9.6/msvc2015_64/include
    INCLUDEPATH +=  C:/Qt/Qt5.9.6/5.9.6/msvc2015_64/include/QtCore
    INCLUDEPATH +=  C:/Qt/Qt5.9.6/5.9.6/msvc2015_64/include/QtGui
    INCLUDEPATH +=  C:/Qt/Qt5.9.6/5.9.6/msvc2015_64/include/QtWidgets
    INCLUDEPATH +=  C:/Qt/Qt5.9.6/5.9.6/msvc2015_64/include/QtPrintSupport
    INCLUDEPATH +=  C:/Qt/Qt5.9.6/5.9.6/msvc2015_64/include/QtSql
    INCLUDEPATH +=  C:/Qt/Qt5.9.6/5.9.6/msvc2015_64/include/QtXml


    LIBS += c:/python36/libs/python36.lib \
        C:/Python36/Lib/site-packages/PySide2/shiboken2.lib \
        C:/Python36/Lib/site-packages/PySide2/pyside2.lib# \
        #../bin/release/lib/QtZint.lib
}
TARGET = ../PyQtRPT

HEADERS += \
    PyQtRPT/qtrpt_wrapper.h\
    PyQtRPT/pyqtrpt_python.h

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
    PyQtRPT/rptcrosstabobject_wrapper.cpp #\
    #../build-binding-Desktop_Qt_5_9_6_GCC_64bit-Release/tmp-lin64/moc_qtrpt.cpp

OTHER_FILES += \
    ../data/typesystem.xml


win32 {
    MOC_DIR = tmp-win32
    UI_DIR = tmp-win32
    UI_HEADERS_DIR = tmp-win32
    UI_SOURCES_DIR = tmp-win32
    OBJECTS_DIR = tmp-win32
    RCC_DIR = tmp-win32
}
linux {
    MOC_DIR = tmp-lin64
    UI_DIR = tmp-lin64
    UI_HEADERS_DIR = tmp-lin64
    UI_SOURCES_DIR = tmp-lin64
    OBJECTS_DIR = tmp-lin64
    RCC_DIR = tmp-lin64
}
