cd binding

QTGUI_INC=~/Qt5.9.6/5.9.6/gcc_64/include/QtGui/
QTCORE_INC=~/Qt5.9.6/5.9.6/gcc_64/include/QtCore/
QTXML_INC=~/Qt5.9.6/5.9.6/gcc_64/include/QtXml/
QTSQL_INC=~/Qt5.9.6/5.9.6/gcc_64/include/QtSql/
QTPRINT_INC=~/Qt5.9.6/5.9.6/gcc_64/include/QtPrintSupport/
QTWD_INC=~/Qt5.9.6/5.9.6/gcc_64/include/QtWidgets/
QTQML_INC=~/Qt5.9.6/5.9.6/gcc_64/include/QtQml/
QT_INC=~/Qt5.9.6/5.9.6/gcc_64/include/
QTTYPESYSTEM=~/.local/lib/python3.5/site-packages/PySide2/typesystems/

CLANG=/usr/lib/clang/4.0/include/
export LD_LIBRARY_PATH=~/.local/lib/python3.5/site-packages/PySide2/

~/.local/lib/python3.5/site-packages/PySide2/shiboken2 ../data/global.h \
    --include-paths=../hybrid:$QTCORE_INC:$QTGUI_INC:$QTXML_INC:$QTSQL_INC:$QTQML_INC:$QTPRINT_INC:$QTWD_INC:../CommonFiles/:../3rdparty/zint-2.4.4/backend/:../3rdparty/zint-2.4.4/backend_qt4:../QtRPT:/usr/lib/gcc:$CLANG:$QT_INC \
    --typesystem-paths=../data:$QTTYPESYSTEM \
    --output-directory=. \
    ../data/typesystem.xml \
    --generator-set=shiboken \
    --avoid-protected-hack \
    --debug-level=full --enable-pyside-extensions
