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

if __name__ == "__main__":
    print_list_com_ports()
