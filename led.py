from time import sleep
import gpiozero

# functions
def blink(led, blinkCount, blinkSpeed):
    print("starts blinking...")
    for i in range(blinkCount):
        led.on()
        sleep(blinkSpeed)
        led.off()
        sleep(blinkSpeed)
    print("done blinking")

# constants, variables
led = gpiozero.LED(17)

# main
blink(led,5,2)
