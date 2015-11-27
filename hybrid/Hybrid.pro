
TARGET = QtRPT
TEMPLATE = lib
include(../QtRPT/QtRPT.pri)
DEFINES += QTRPT_LIBRARY
#CONFIG += staticlib
CONFIG += qt
QT += core gui
	 
UI_DIR = build
RCC_DIR = build
MOC_DIR = build
OBJECTS_DIR = build



OTHER_FILES += \
            ../data/global.h \
            ../data/typesystem.xml
