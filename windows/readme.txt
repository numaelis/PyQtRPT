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


Instructions build:(tested in win 7(64), python 3.4(32bit), PySide 1.2.4, Qt 4.8.6(MSVC 10,32bit), qtRPTProject 1.5.5)

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
  |-builds.bats
<<<<<<<<<<<<<<<
if disable the use of the Zint library:
  *in QtRPT/QtRPT.pri uncomment #DEFINES += NO_BARCODE result: DEFINES += NO_BARCODE
  *in data/global.h delete lines:
      #include "../3rdparty/zint-2.4.4/backend_qt4/qzint.h"
      #include "../3rdparty/zint-2.4.4/backend_qt4/qzint_global.h"
  *in hybrid/Hybrid.pro uncomment #CONFIG += staticlib
  *in hybridpy/hybridpy.pro changue:
	../hybrid/QtRPTaps.lib \ 
	../hybrid/QtZint.lib
	for:
	../hybrid/QtRPTaps.lib
  *in buildHybridPy.bat delete lines:
      copy hybrid\QtRPTaps.dll package\QtRPTaps.dll /y 
	  copy hybrid\QtZint.dll package\QtZint.dll /y 
<<<<<<<<<<<<<<<
apply patch:

    pyqtrpt155_Win32.patch

<<<<<<<<<<<<<
build:

1) buildZint.bat

2) buildHybrid.bat

3) shibokenHybrid.bat

4) buildHybridPy.bat

      (if error QMetaObject)
      in hybridpy/PyQtRPT/rptsql_wrapper.h
      in hybridpy/PyQtRPT/qtrpt wrapper .h
      in hybridpy/PyQtRPT/barcode_wrapper.h
      in hybridpy/PyQtRPT/char_wrapper.h
      in hybridpy/PyQtRPT/dataobject_wrapper.h
      add en public: const QMetaObject* metaObject() const;
      and buildHybridPy.bat
           
<<<<<<<<<<<

-create 3 libs in package: PyQtRPT.pyd, QtRPTaps.dll and QtZint.dll

<<<<<<<<<<<<<<<
run examples:
python3 example1.py

<<<<<<<<<<<<<<<<
links:
http://www.qtrpt.tk/
http://lynxline.com/superhybrids-part-2-now-qt-pyside/
