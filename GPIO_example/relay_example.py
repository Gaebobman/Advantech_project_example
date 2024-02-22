import Jetson.GPIO as GPIO

def setup_gpio():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    print("Current Mode: ", GPIO.getmode())

def main():
    RELAY_PIN = 19
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    
    try:
        while True:
            state = int(input("Enter state (0: Low, 1: High, 2: Quit): "))
            if state == 0:
                GPIO.output(RELAY_PIN, GPIO.LOW)
                print("Low")
            elif state == 1:
                GPIO.output(RELAY_PIN, GPIO.HIGH)
                print("High")
            elif state == 2:
                print("Exiting...")
                break
            else:
                print("Invalid input...")
    except ValueError:
        print("Please enter a valid integer (0, 1, or 2).")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    setup_gpio()
    main()
