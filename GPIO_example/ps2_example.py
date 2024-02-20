import Jetson.GPIO as GPIO
import time 

def read_joystick(channels):
	print(GPIO.input(channels[0]), GPIO.input(channels[1]), GPIO.input(channels[2]))

GPIO.cleanup() 
GPIO.setmode(GPIO.BOARD)

JOYSTICK_CHANNELS = [21, 19, 23]
GPIO.setup(JOYSTICK_CHANNELS, GPIO.IN)


while True:
	read_joystick(JOYSTICK_CHANNELS)
	time.sleep(0.1)
