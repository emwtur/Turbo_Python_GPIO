#!/usr/bin/python
import logging
import time
#logging.basicConfig(level=logging.DEBUG)
import Turbo_GPIO.HCSR04 as HCSR04


sensor = HCSR04.HCSR04()

distance = sensor.read_distance()
print 'Distance      = {0:0.2f} cm'.format(distance)
time.sleep(2)


