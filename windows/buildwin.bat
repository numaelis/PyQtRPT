
SET QMAKE="c:\qt\4.8.6\qmake\qmake.exe"

cd 3rdparty\zint-2.4.4\backend_qt4\
%QMAKE%
nmake clean
nmake

cd ..\..\..\hybrid\
%QMAKE%
nmake clean
nmake

cd ..\hybridpy
SET QTGUI_INC="C:\Qt\4.8.6\include\QtGui"
SET QTCORE_INC="C:\Qt\4.8.6\include\QtCore"
SET QT_INC="C:\Qt\4.8.6\include"
SET QTTYPESYSTEM="C:\Python34\Lib\site-packages\PySide\typesystems"

SET PYSIDE_INC="C:\python34\lib\site-packages\PySide\include"
SET PYSIDE_QtCore_INC="C:\python34\lib\site-packages\PySide\include\PySide\QtCore"
SET PYSIDE_QtGui_INC="C:\python34\lib\site-packages\PySide\include\PySide\QtGui"

C:\python34\lib\site-packages\pyside\shiboken.exe ..\data\global.h --debug-level=full -avoid-protected-hack --enable-pyside-extensions --include-paths=..\hybrid;%PYSIDE_INC%;%PYSIDE_QtGui_INC%;%PYSIDE_QtGui_INC%;%QTCORE_INC%;%QTGUI_INC%;%QT_INC% --typesystem-paths=..\data;%QTTYPESYSTEM% --output-directory=..\hybridpy ..\data\typesystem.xml


%QMAKE%
nmake clean
nmake