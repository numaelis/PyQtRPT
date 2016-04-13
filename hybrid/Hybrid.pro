
TARGET = QtRPTaps # adaptation pyside
TEMPLATE = lib
include(../QtRPT/QtRPT.pri)
DEFINES += QTRPTAPS_LIBRARY
#CONFIG += staticlib
CONFIG += qt
QT += core gui
	 
UI_DIR = build
RCC_DIR = build
MOC_DIR = build
OBJECTS_DIR = build
