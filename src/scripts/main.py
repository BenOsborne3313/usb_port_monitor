from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow
import sys
from usb_port_monitor.gui.gui_main import MainWindow

def main():
    print("USB Port Monitor")
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window_main = MainWindow()
    window_main.show()
    app.exec()

#only run if this is the main file
if __name__ == "__main__":
    main()