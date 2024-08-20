import serial.tools.list_ports

def print_list_com_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"Device: {port.device}")
        print(f"Name: {port.name}")
        print(f"Description: {port.description}")
        print(f"Hardware ID: {port.hwid}")
        print(f"VID: {port.vid}")
        print(f"PID: {port.pid}")
        print(f"Serial Number: {port.serial_number}")
        print(f"Location: {port.location}")
        print(f"Manufacturer: {port.manufacturer}")
        print(f"Product: {port.product}")
        print(f"Interface: {port.interface}")
        print("-" * 40)

def print_port(port):
        print(f"Device: {port.device}")
        print(f"Name: {port.name}")
        print(f"Description: {port.description}")
        print(f"Hardware ID: {port.hwid}")
        print(f"VID: {port.vid}")
        print(f"PID: {port.pid}")
        print(f"Serial Number: {port.serial_number}")
        print(f"Location: {port.location}")
        print(f"Manufacturer: {port.manufacturer}")
        print(f"Product: {port.product}")
        print(f"Interface: {port.interface}")
        print("-" * 40)

def is_port_in_use(port_name):
    try:
        # Attempt to open the port in a non-blocking mode
        with serial.Serial(port_name, timeout=0.1) as ser:
            # If no exception, the port is not in use
            return False
    except (OSError, serial.SerialException):
        # If an exception occurs, the port is in use
        return True

if __name__ == "__main__":
    print_list_com_ports()
