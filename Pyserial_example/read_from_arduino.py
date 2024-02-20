import serial 
import time 

PORT = '/dev/ttyACM0'
BAUDRATE = 9600
arduino = serial.Serial(PORT, BAUDRATE=115200, timeout=.1) 


while True:
    # The last bit gets rid of the new-line chars
    # You can change this to whatever you want
    data = arduino.readline()[:-2] 
    if data:
        print(data)
    time.sleep(1) 