cd hybridpy
SET QTGUI_INC="C:\Qt\4.8.6\include\QtGui"
SET QTCORE_INC="C:\Qt\4.8.6\include\QtCore"
SET QT_INC="C:\Qt\4.8.6\include"
SET QTTYPESYSTEM="c:\python34\lib\site-packages\pyside\typesystems"

SET PYSIDE_INC="c:\python34\lib\site-packages\pyside\include"
SET PYSIDE_QtCore_INC="c:\python34\lib\site-packages\pyside\include\pyside\qtcore"
SET PYSIDE_QtGui_INC="c:\python34\lib\site-packages\pyside\include\pyside\qtgui"

C:\python34\lib\site-packages\pyside\shiboken.exe ..\data\global.h --debug-level=full -avoid-protected-hack --enable-pyside-extensions --include-paths=..\hybrid;%PYSIDE_INC%;%PYSIDE_QtGui_INC%;%PYSIDE_QtGui_INC%;%QTCORE_INC%;%QTGUI_INC%;%QT_INC% --typesystem-paths=..\data;%QTTYPESYSTEM% --output-directory=..\hybridpy ..\data\typesystem.xml

cd..