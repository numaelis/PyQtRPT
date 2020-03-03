


linux:
0) edit files configuration:  "shiboken_wrap.sh", "bunding.pro"
1) open and build projects: 3rdparty/zint-2.4.4/backend_qt4/Zint.pro and 3rdparty/QtXlsx/QtXlsx.pro
2) run ./shiboken_wrap.sh 
3) open and build projects: first QtRPTaps and then binding
4) copy libraries or run ./copylib.sh

win:
0) edit files configuration:  "shiboken_win.bat", "bunding.pro"
1) open and build projects: 3rdparty/zint-2.4.4/backend_qt4/Zint.pro and 3rdparty/QtXlsx/QtXlsx.pro
2) run ./shiboken_win.bat 
3) open and build projects: first QtRPTaps and then binding
4) copy libraries (replace name PyQtRPT.dll to PyQtRPT.pyd)
