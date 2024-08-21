from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
import serial.tools.list_ports
import usb_port_monitor.gui.theme.make_theme as make_theme
from usb_port_monitor.gui.ui_gui_main import Ui_MainWindow
from usb_port_monitor.com_port_funcs import print_port, is_port_in_use
from multiprocessing import Queue, Process
import multiprocessing
import time
import sys
import os
import markdown

multiprocessing.freeze_support()


def resource(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def ports_data_collection_process(queue):
    while True:
        attemp_get_ports_data(queue)
        time.sleep(0.1)

def attemp_get_ports_data(queue):
    if queue.full():
        return
    
    ports = serial.tools.list_ports.comports()

    ports_dict = {}

    for port in ports:
        ports_dict[port.device] = is_port_in_use(port.device)

    queue.put(ports_dict)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):

        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("USB Port Monitor")
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)

        
        them_path = resource("assets/theme.json")
        
        load_pallet = make_theme.load_theme_from_json(them_path)
        self.setPalette(load_pallet)

        icon_path = resource("assets/usb-symbol-icon.jpg")
        self.setWindowIcon(QIcon(icon_path))

        #need some special sauce since it is in the base folder...
        if hasattr(sys, '_MEIPASS'):
            #we are bundled
            readme_path = resource(r"README.md")
        else:
            readme_path = resource(r"../../../README.md")

        with open(readme_path, "r") as f:
            readme = f.read()
        html = markdown.markdown(readme)
        self.ui.textEdit.setHtml(html)
        self.ui.textEdit.setReadOnly(True)

        self.ports_dict_queue = Queue(maxsize=10)
        self.ports_in_use_dict = {}
        attemp_get_ports_data(self.ports_dict_queue)

        self.populate_ports_dict()
        #start the process to get the ports data
        self.process = Process(target=ports_data_collection_process, args=(self.ports_dict_queue,))
        self.process.daemon = True
        self.process.start()
        self.com_port_timer = QtCore.QTimer()
        self.com_port_timer.timeout.connect(self.update_ports_list)
        self.com_port_timer.start(100)

        self.ui.clear_button.clicked.connect(self.clear_ports_list)
            
    def clear_ports_list(self):
        self.ui.port_list.clear()
        self.populate_ports_dict = ()
        self.ports_dict = {}

    def update_ports_list(self):
        #we want to display the most recently connected ports at the top of the list
        # any disconnected ports we will set the text color to red
        #insert the last item at the top of the list
        
        if not self.ports_dict_queue.empty():
            self.ports_in_use_dict = self.ports_dict_queue.get()
        
        ports = serial.tools.list_ports.comports()
        

        ports_removed = set(self.ports_dict.keys()) - set([port.device for port in ports])
        ports_added = set([port.device for port in ports]) - set(self.ports_dict.keys())
        # print(f"Ports Removed: {ports_removed}, Ports Added: {ports_added}, Ports Dict: {self.ports_dict.keys()}")

        for port_name in set(self.ports_dict.keys()) | set([port.device for port in ports]):
            port = self.ports_dict.get(port_name, None)
            if port is None:
                #find it in the list of ports
                for p in ports:
                    if p.device == port_name:
                        port = p
                        break
            if port.device in ports_added:
                item = QtWidgets.QListWidgetItem(f"{port.device} - {port.description}")
                #set item according to palette
                if port.device in self.ports_in_use_dict.keys() and self.ports_in_use_dict[port.device]:
                    item.setForeground(QtCore.Qt.green)
                self.ui.port_list.insertItem(0, item)
                self.ports_dict[port.device] = port
                print_port(port)
            if port.device in ports_removed:
                items = self.ui.port_list.findItems(f"{port.device} - {port.description}", QtCore.Qt.MatchExactly)
                for item in items:
                    index = self.ui.port_list.row(item)
                    # print(f"Index: {index}")
                    item = self.ui.port_list.takeItem(index)
                    item.setForeground(QtCore.Qt.red)
                    self.ui.port_list.insertItem(index, item)
            else:
                items = self.ui.port_list.findItems(f"{port.device} - {port.description}", QtCore.Qt.MatchExactly)
                for item in items:
                    index = self.ui.port_list.row(item)
                    item = self.ui.port_list.takeItem(index)
                    item =  QtWidgets.QListWidgetItem(f"{port.device} - {port.description}")
                    if port.device in self.ports_in_use_dict.keys() and self.ports_in_use_dict[port.device]:
                        item.setForeground(QtCore.Qt.green)
                    self.ui.port_list.insertItem(index, item)



    def populate_ports_dict(self):
        self.ports_dict = {}

    

if __name__ == "__main__":

    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window_main = MainWindow()
    window_main.show()
    app.exec()




