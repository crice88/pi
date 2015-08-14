import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

POWER_PIN = 8 
MOTION_PIN = 11

GPIO.setup(MOTION_PIN, GPIO.IN)
GPIO.setup(POWER_PIN, GPIO.OUT)
GPIO.output(POWER_PIN, False)

global is_on
is_on = False

print "PIR Module Test (Please press CTRL+C to exit)"
time.sleep(2)
print "Ready"

while True:
    if GPIO.input(MOTION_PIN):
	print "Motion Detected!!"
	if is_on:
	    print "Lights off!"
	    GPIO.output(POWER_PIN, False)
	    is_on = False
	    time.sleep(2)
	else:
            print "Lights on!"
	    GPIO.output(POWER_PIN, True)
	    is_on = True
	    time.sleep(2)
    time.sleep(1)
    print(GPIO.input(MOTION_PIN))

