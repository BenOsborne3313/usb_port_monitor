from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPalette, QColor 
from PySide6.QtUiTools import QUiLoader
from qt_material import apply_stylesheet
import usb_port_monitor.gui.theme.make_theme as make_theme
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
app.setStyle("Fusion")

dir = os.path.abspath(__file__)
window = loader.load(os.path.join(os.path.dirname(dir), "assets/gui_main.ui"), None)
# apply_stylesheet(app, theme='dark_blue.xml', extra=extra)
# palette = QPalette()
# palette.setColor(QPalette.Window, QColor(53, 53, 53))
# palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
# palette.setColor(QPalette.Base, QColor(25, 25, 25))
# palette.setColor(QPalette.AlternateBase, QColor(255, 255, 255))
# palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0))
# palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
# palette.setColor(QPalette.Text, QColor(255, 255, 255))
# palette.setColor(QPalette.Button, QColor(53, 53, 53))
# palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
# palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
# palette.setColor(QPalette.Link, QColor(42, 130, 218))
# palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
# palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
them_path = os.path.join(os.path.dirname(dir), "assets/theme.json")
load_pallet = make_theme.load_theme_from_json(them_path)
app.setPalette(load_pallet)
window.show()
app.exec()
