import RPi.GPIO as GPIO
import time


def on():
    print "on"
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)

    print "going high"

    time.sleep(1)
    GPIO.output(16, GPIO.LOW)
    GPIO.cleanup()

def off():
    print "off"
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(26, GPIO.LOW)
    GPIO.cleanup()
'''
def setup():
    led = 11

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(17, GPIO.IN)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, GPIO.LOW)

    try:
        while True:
            if GPIO.input(17) == False:
                GPIO.output(27, GPIO.LOW)
            elif GPIO.input(17) == True:
                GPIO.output(27, GPIO.HIGH)
    except (KeyboardInterrupt):
        GPIO.output(27, GPIO.LOW)
        exit()
        '''
        
        


if __name__ == "__main__":
    on()
