#!/usr/bin/python

import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)

MOTION_PIN = 7
POWER_PIN = 8
is_on = False

IO.setup(MOTION_PIN, IO.IN)
IO.setup(POWER_PIN, IO.OUT)
IO.output(POWER_PIN, False)

def MOTION(MOTION_PIN):
    print "Motion Detected!"
    global is_on
    if is_on:
        print "Lights off!"
  	IO.output(POWER_PIN, False)
   	is_on = False
    else:
        print "Lights on!!"
   	IO.output(POWER_PIN, True)
   	is_on = True

print "Motion Sensing Lights"
time.sleep(2)
print "Ready!"

try:
    IO.add_event_detect(MOTION_PIN, IO.RISING, callback=MOTION)
    while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print "Quit"
    IO.cleanup()
