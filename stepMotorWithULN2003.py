import RPi.GPIO as GPIO
import time
from time import sleep

in1 = 22
in2 = 21
in3 = 24
in4 = 23
CLOCKWISE = True
COUNTER_CLOCKWISE- = False

step_sleep = 0.02 # quickness of movement
step_count = int(4096/2) # 5.625*(1/64) per step, 4096 steps is 360°
direction = COUNTER_CLOCKWISE # True for clockwise, False for counter-clockwise

step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]

# setup
GPIO.setmode( GPIO.BOARD )
GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )

# initial voltage levels
GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )

motor_pins = [in1,in2,in3,in4]
motor_step_counter = 0

# functions
def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()

# main
try:
    i = 0
    for i in range(step_count):
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction==True:
            motor_step_counter = (motor_step_counter - 1) % 8
        elif direction==False:
            motor_step_counter = (motor_step_counter + 1) % 8
        else: 
            print( "direction should always be either True or False" )
            cleanup()
            exit( 1 )
        time.sleep( step_sleep )
except Exception as e:
    print(e)
    cleanup()
    exit( 1 )
finally:
    cleanup()
    exit( 0 )
