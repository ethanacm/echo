import RPi.GPIO as GPIO
import time
from subprocess import call

def on():
    print "on"
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(16, GPIO.OUT)
    #GPIO.output(16, GPIO.HIGH)
    print "going high"
    #time.sleep(1)
    GPIO.output(16, GPIO.LOW)
    time.sleep(1)
    GPIO.cleanup()
    print "success"

def off():
    print "on"
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)
    #GPIO.output(26, GPIO.HIGH)
    print "going high"
    #time.sleep(1)
    GPIO.output(26, GPIO.LOW)
    time.sleep(1)
    GPIO.cleanup()
    print "success"

def flash():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT) #off
    GPIO.setup(16, GPIO.OUT) # on
    #GPIO.output(26, GPIO.HIGH)
    print "going high"
    #time.sleep(1)
    for i in range(5):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26, GPIO.OUT) #off
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, True)
        time.sleep(.5)
        GPIO.output(16, False)
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26, GPIO.OUT) #off
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, True)
        time.sleep(.5)
        GPIO.output(16, False)
	GPIO.cleanup()
    GPIO.cleanup()
    print "success"

def g_off():
	GPIO.output(26, True)
	time.sleep(1)
	GPIO.output(26, False)

def g_on():
        GPIO.output(16, True)
        time.sleep(1)
        GPIO.output(16, False)

def test():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT) #off
    GPIO.setup(16, GPIO.OUT) # on
    g_on()
    g_off()
    #GPIO.cleanup()
def test_flash():
    call(["zap5-setup"])
    for i in range(15):
	call(["zap5-off"])
	call(["zap5-on"])

if __name__ == "__main__":
    test_flash()
