from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPalette, QColor 
from PySide6.QtUiTools import QUiLoader
from qt_material import apply_stylesheet
import usb_port_monitor.gui.theme.make_theme as make_theme
import sys
import os




if __name__ == "__main__":

    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    dir = os.path.abspath(__file__)
    window = loader.load(os.path.join(os.path.dirname(dir), "assets/gui_main.ui"), None)
    them_path = os.path.join(os.path.dirname(dir), "assets/theme.json")
    load_pallet = make_theme.load_theme_from_json(them_path)
    app.setPalette(load_pallet)
    window.show()
    app.exec()

