// numaelis@gmail.com
PyQtRPT
Python Binding for QtRPT
Python PySide Shiboken QtRPT
License(GPL) compatible with QtRPT, zint
or
LGPL only QtRPT.


""""""
QtRPT (http://www.qtrpt.tk/index.php)
Version 1.5.5
Programmer: Aleksey Osipov
Web-site: http://www.aliks-os.tk

Announcements:(http://www.qtrpt.tk/index.php?page=announcements.php)
License:

For a long time the QtRPT project is distributed under the LGPL license. This license allows you to dynamically link with your 
source code. In order to facilitate the user to use QtRPT and allow to produce statically linking, I decided to change the 
Apache 2.0 license.
License Apache 2.0 more permissive compared to LGPL, I hope that the transition will not create problems for you.
Please note that QtRPT to generate bar code uses the Zint library, which is distributed under license GPL, in this case,
you must use your project is also under this license or disable the use of the Zint library.
""""""


Instructions build:(tested in opensuse 64, python 3.4, PySide 1.2.4, Qt 4.8.6, qtRPTProject 1.5.5)

download qtRPTProject 1.5.5 and 
   copy in PyQtRPTDir:
  	CommonFiles
	QtRPT
	3rdparty 
	QtRptDesigner
   copy in package:
        QtRptDemo/examples/examples_report
	
final dir:
PyQtRPTDir/
  |-data/
  |	|-global.h
  |	|-typesystem.xml
  |-hybrid/
  |	|-hybrid.pro
  |-hybridpy/
  |	|-hybridpy.pro
  |-package/
  |	|-example1.py
  |     |-more examples ....
  |	|-examples_report/  from---> QtRptDemo/examples/
  |-CommonFiles/
  |-QtRPT/
  |-3rdparty/zint-2.4.4/
  |-QtRptDesigner/
  |-build.sh
<<<<<<<<<<<<<<<
if disable the use of the Zint library:
  *in QtRPT/QtRPT.pri uncomment #DEFINES += NO_BARCODE result: DEFINES += NO_BARCODE
  *in data/global.h delete lines:
      #include "../3rdparty/zint-2.4.4/backend_qt4/qzint.h"
      #include "../3rdparty/zint-2.4.4/backend_qt4/qzint_global.h"
  *in hybrid/Hybrid.pro uncomment #CONFIG += staticlib
  *in hybridpy/hybridpy.pro changue:
	../hybrid/libQtRPTaps.so \ 
	../hybrid/libQtZint.so
	for:
	../hybrid/libQtRPTaps.a
  *in build.sh delete lines:
      cp -f hybrid/libQtRPTaps.so.1.0.0 package/libQtRPTaps.so.1
      cp -f hybrid/libQtZint.so.1.0.0 package/libQtZint.so.1

<<<<<<<<<<<<<<
patch:

patch -p1 < pyqtrpt155.patch
<<<<<<<<<<<<<<<<

config build.sh

QTGUI_INC=/usr/lib/qt4/include/QtGui
QTCORE_INC=/usr/lib/qt4/include/QtCore
QTTYPESYSTEM=/usr/lib/python3.4/site-packages/PySide/typesystems

<<<<<<<<<<<<<<
config hybridpy.pro

INCLUDEPATH +=  /usr/lib/python3.4/site-packages/PySide/include/PySide
INCLUDEPATH +=  /usr/lib/python3.4/site-packages/PySide/include/PySide/QtCore
INCLUDEPATH +=  /usr/lib/python3.4/site-packages/PySide/include/PySide/QtGui
INCLUDEPATH +=  /usr/lib/python3.4/site-packages/PySide/include/shiboken
INCLUDEPATH +=  /usr/include/python3.4m
	

LIBS += /usr/lib/libpython3.4m.so.1.0 \
    /usr/lib/python3.4/site-packages/PySide/libshiboken.cpython-34m.so.1.2 \
    /usr/lib/python3.4/site-packages/PySide/libpyside.cpython-34m.so.1.2 \
<<<<<<<<<<<<<

build:
sh build.sh
-create 3 libs in package: PyQtRPT.so, libQtRPTaps.so.1 and libQtZint.so.1

<<<<<<<<<<<<<<<
install libQtRPTaps and libQtZint:
permanently:
    example: sudo cp -f package/libQtRPTaps.so.1 /usr/lib/libQtRPTaps.so.1
    ex: sudo cp -f package/libQtZint.so.1 /usr/lib/libQtZint.so.1
temporary:
    ex: cd package/
        export LD_LIBRARY_PATH=.
<<<<<<<<<<<<<<<<
run examples:
python3 example1.py

<<<<<<<<<<<<<<<<
links:
http://www.qtrpt.tk/
http://lynxline.com/superhybrids-part-2-now-qt-pyside/
