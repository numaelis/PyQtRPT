SET QMAKE="c:\qt\4.8.6\qmake\qmake.exe"

cd hybrid
%QMAKE% -config release
::nmake clean
nmake
cd ..