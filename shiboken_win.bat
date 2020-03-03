cd binding
SET QTGUI_INC="C:\Qt\Qt5.9.6\5.9.6\msvc2015_64\include\QtGui"
SET QTCORE_INC="C:\Qt\Qt5.9.6\5.9.6\msvc2015_64\include\QtCore"
SET QTXML_INC="C:\Qt\Qt5.9.6\5.9.6\msvc2015_64\include\QtXml"
SET QTSQL_INC="C:\Qt\Qt5.9.6\5.9.6\msvc2015_64\include\QtSql"
SET QTPRINT_INC="C:\Qt\Qt5.9.6\5.9.6\msvc2015_64\include\QtPrintSupport"
SET QTWD_INC="C:\Qt\Qt5.9.6\5.9.6\msvc2015_64\include\QtWidgets"
SET QTQML_INC="C:\Qt\Qt5.9.6\5.9.6\msvc2015_64\include\QtQml"

SET QT_INC="C:\Qt\Qt5.9.6\5.9.6\msvc2015_64\include"
SET QTTYPESYSTEM="C:\Python36\Lib\site-packages\PySide2\typesystems"

SET PYSIDE_INC="C:\Python36\Lib\site-packages\PySide2\include"
SET PYSIDE_QtCore_INC="C:\Python36\Lib\site-packages\PySide2\include\PySide2\QtCore"
SET PYSIDE_QtGui_INC="C:\Python36\Lib\site-packages\PySide2\include\PySide2\QtGui"

SET PYSIDE_QtXml_INC="C:\Python36\Lib\site-packages\PySide2\include\PySide2\QtXml"
SET PYSIDE_QtSql_INC="C:\Python36\Lib\site-packages\PySide2\include\PySide2\QtSql"
SET PYSIDE_QtP_INC="C:\Python36\Lib\site-packages\PySide2\include\PySide2\QtPrintSupport"
SET PYSIDE_QtW_INC="C:\Python36\Lib\site-packages\PySide2\include\PySide2\QtWidgets"
SET PYSIDE_QtQml_INC="C:\Python36\Lib\site-packages\PySide2\include\PySide2\QtQml"

C:\Python36\Lib\site-packages\PySide2\shiboken2.exe ..\data\global.h --debug-level=full --avoid-protected-hack --enable-pyside-extensions --include-paths=..\QTRPTaps;..\CommonFiles;..\3rdparty\zint-2.4.4\backend;..\3rdparty\zint-2.4.4\backend_qt4;..\QtRPT;%PYSIDE_INC%;%PYSIDE_QtGui_INC%;%PYSIDE_QtCore_INC%;%QTCORE_INC%;%QTGUI_INC%;%QT_INC%;%QTXML_INC%;%QTSQL_INC%;%QTPRINT_INC%;%QTWD_INC%;%QTQML_INC% --typesystem-paths=..\data;%QTTYPESYSTEM% --output-directory=..\binding ..\data\typesystem.xml
cd..