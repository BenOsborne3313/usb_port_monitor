from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from qt_material import apply_stylesheet
import sys
import os

# Extra stylesheets
extra = {
    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',
    # Font
    'font_family': 'Roboto',
    # Density
    'density_scale': '0',
    # Button Shape
    'button_shape': 'default',
}

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
dir = os.path.abspath(__file__)
window = loader.load(os.path.join(os.path.dirname(dir), "assets/gui_main.ui"), None)
apply_stylesheet(app, theme='dark_teal.xml', extra=extra)
window.show()
app.exec()
