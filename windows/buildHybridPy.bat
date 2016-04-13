SET QMAKE="c:\qt\4.8.6\qmake\qmake.exe"
cd hybridpy
%QMAKE% -config release
nmake clean
nmake

cd..

copy hybrid\QtRPTaps.dll package\QtRPTaps.dll /y 
copy hybrid\QtZint.dll package\QtZint.dll /y 

copy hybridpy\PyQtRPT.dll package\PyQtRPT.pyd /y 

