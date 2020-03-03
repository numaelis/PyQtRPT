PyQtRPT 
Python Binding for QtRPT
(PySide2 Shiboken2)
Author: Numael Garay, mantrixsoft@gmail.com
License LGPL3 compatible with QtRPT (see license)

this package has been built with: Python3.5, Pyside2(Qt5.9), Qt Framework 5.9
S.O. Debian 9


""""""
QtRPT (http://www.qtrpt.tk/index.php)
Version 2.0.1
Programmer: Aleksey Osipov
Web-site: http://www.aliks-os.tk

Announcements:(http://www.qtrpt.tk/index.php?page=announcements.php)
License:

For a long time the QtRPT project is distributed under the LGPL license. This license allows you to dynamically 
link with your source code. In order to facilitate the user to use QtRPT and allow to produce statically linking, 
I decided to change the Apache 2.0 license.
License Apache 2.0 more permissive compared to LGPL, I hope that the transition will not create problems for you.
Please note that QtRPT to generate bar code uses the Zint library, which is distributed under license GPL, 
in this case, you must use your project is also under this license or disable the use of the Zint library.
""""""

        
for run examples:
    export LD_LIBRARY_PATH=PyQtRPT
    python3 example1.py 


for run Designer and open xml files:
    export LD_LIBRARY_PATH=PyQtRPT
    ./QtRptDesigner

links:
http://www.qtrpt.tk/
http://lynxline.com/superhybrids-part-2-now-qt-pyside/


