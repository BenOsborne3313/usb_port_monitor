from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow
import serial.tools.list_ports
import usb_port_monitor.gui.theme.make_theme as make_theme
from usb_port_monitor.gui.ui_gui_main import Ui_MainWindow
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("USB Port Monitor")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        dir = os.path.abspath(__file__)
        them_path = os.path.join(os.path.dirname(dir), "assets/theme.json")
        load_pallet = make_theme.load_theme_from_json(them_path)
        self.setPalette(load_pallet)

        self.com_port_timer = QtCore.QTimer()
        self.com_port_timer.timeout.connect(self.populate_ports_dict)
        self.com_port_timer.start(100)
                


    def populate_ports_dict(self):
        self.ports_dict = {}
        self.ui.port_list.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.ports_dict[port.device] = port
            item = QtWidgets.QListWidgetItem(port.device)
            self.ui.port_list.addItem(item)
    

if __name__ == "__main__":

    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window_main = MainWindow()
    window_main.show()
    app.exec()




