#!/bin/sh
cd hybrid/
qmake
make clean
make

cd ../zint-2.4.4/backend_qt4/
qmake
make clean
make
cd ../../hybridpy

QTGUI_INC=/usr/lib/qt4/include/QtGui
QTCORE_INC=/usr/lib/qt4/include/QtCore
QTTYPESYSTEM=/usr/lib/python3.4/site-packages/PySide/typesystems


shiboken ../data/global.h \
    --include-paths=../hybrid:$QTCORE_INC:$QTGUI_INC:/usr/include \
    --typesystem-paths=../data:$QTTYPESYSTEM \
    --output-directory=. \
    ../data/typesystem.xml

qmake
make clean
make

cd ..
cp -f libPyQtRptLib.so.1.0.0 package/PyQtRPT.so
rm -rf libPyQtRptLib.so.1.0.0
rm -rf libPyQtRptLib.so.1.0
rm -rf libPyQtRptLib.so.1
rm -rf libPyQtRptLib.so

cp -f hybrid/libQtZint.so.1.0.0 package/libQtZint.so.1
