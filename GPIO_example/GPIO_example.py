import Jetson.GPIO as GPIO
import time

GPIO.cleanup() 
GPIO.setmode(GPIO.BOARD)
print("Current Mode: ", GPIO.getmode())

# Switch example
INPUT_PIN = 13
GPIO.setup(INPUT_PIN, GPIO.IN)


while True:    
    input_state = GPIO.input(INPUT_PIN)
    if input_state == GPIO.LOW:
        print("Switch pressed")
    else:
        print("Wating...")
    time.sleep(0.1) 


"""
# On/Off example
LED_PIN = 33
GPIO.setup(LED_PIN, GPIO.OUT)

for i in range(5):
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("High ", LED_PIN)
    time.sleep(3)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)
    print("Low", LED_PIN)
"""

GPIO.cleanup()


