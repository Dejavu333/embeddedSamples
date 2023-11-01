import RPi.GPIO as GPIO
import time

# GPIO pins
directionPin = 24
turningSignalPin = 23

# setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(directionPin, GPIO.IN)
GPIO.setup(turningSignalPin, GPIO.IN)
GPIO.setup(directionPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # to avoid floating state
GPIO.setup(turningSignalPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # to avoid floating state

# variables
directionPinLastState = 0
counter = 0
directionPinState = 0
turningSignalPinState = 0

# main
try:
    while True:
        directionPinState = GPIO.input(directionPin)
        turningSignalPinState = GPIO.input(turningSignalPin)
        if directionPinState != directionPinLastState:
            if turningSignalPinState != directionPinState:
                counter += 1 
            else:
                counter -= 1 
            print(f"directionPinState: {directionPinState}, turningSignalPinState: {turningSignalPinState}")
            print(counter)
        directionPinLastState = directionPinState
        time.sleep(0.001)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
    GPIO.cleanup()
    exit(0)
except Exception as e:
    print(e)
    GPIO.cleanup()
    exit(0)
finally:
    GPIO.cleanup()
    exit(0)
