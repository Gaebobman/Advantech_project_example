import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

print([port.name for port in ports])

# Reference: https://stackoverflow.com/questions/49176095/pyserial-in-pythonlist-out-available-comports-without-for-loop

