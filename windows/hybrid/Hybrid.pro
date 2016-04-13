
TEMPLATE = lib
#CONFIG += dll

include(../QtRPT/QtRPT.pri)
include(../QtRPT/config.pri)
DEFINES += QTRPTAPS_LIBRARY
TARGET = QtRPTaps # adaptation pyside
CONFIG += staticlib # comentar y descomentar para generar dll y despues el lib
DLLDESTDIR = $${DEST_DIRECTORY}
DESTDIR    = $${DEST_DIRECTORY}

#CONFIG += qt
QT += core gui sql
	 
MOC_DIR = build
UI_DIR = build
UI_HEADERS_DIR = build
UI_SOURCES_DIR = build
OBJECTS_DIR = build
RCC_DIR = build
