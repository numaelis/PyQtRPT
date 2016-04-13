SET QMAKE="c:\qt\4.8.6\qmake\qmake.exe"

cd 3rdparty\zint-2.4.4\backend_qt4\
%QMAKE% -config release
nmake clean
nmake

cd ..\..\..\