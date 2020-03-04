
PySide2 QtRPT

Python Binding for QtRPT
Python Report
(PySide2 Shiboken)

License LGPL3 compatible with QtRPT (see license)


QtRPT Report Engine:
QtRPT is the easy-to-use print report engine written in C++ QtToolkit.
It allows combining several reports in one XML file. For separately taken field,
you can specify some condition depending on which this field will display in different font and background color, etc.
The project consists of two parts: report library QtRPT and report designer application QtRptDesigner. Report file is a file in XML format.
The report designer makes easy to create report XML file.
QtRPT (http://www.qtrpt.tk/index.php)

Recommendations:
use QtRptDesigner -> to edit xml files.
view examples.


binaries:
https://sourceforge.net/projects/pyqtrpt/

Important: from Qt5.12, the package must have the same version and subversion de PySide2 and shiboken2. for example the PyQtRPT_xxx_5.12.3 package has a requirement of PySide2_5.12.3 and shiboken2_5.12.3. sometimes when installing Pyside2 it installs shiboken2 automatically, but it does not guarantee that it is the same subversion. in this case it is convenient to uninstall shiboken2 and install it again with the corresponding subversion. 

build:
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
