import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
import logging


class HCSR04(object):
	TRIG = 23                                  #Associate pin 23 to TRIG
	ECHO = 24                                  #Associate pin 24 to ECHO
	def __init__(self, trig=TRIG, echo=ECHO,**kwargs):
		self._logger = logging.getLogger('Turbo_GPIO.HCSR04')
		self._trig = trig
		self._echo = echo
		self._logger.debug('echo = 0x{0:2x}'.format(self._echo ))
		self._logger.debug('trig= 0x{0:2x}'.format(self._trig))
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
	def read_distance(self):
		self._logger.debug('read_distance')
		GPIO.setup(self._trig,GPIO.OUT)                  #Set pin as GPIO out
		GPIO.setup(self._echo,GPIO.IN)                   #Set pin as GPIO in

		GPIO.output(self._trig, False)                 #Set TRIG as LOW
		self._logger.debug('Waiting For Sensor To Settle')
		time.sleep(2)                            #Delay of 2 seconds

		GPIO.output(self._trig, True)                  #Set TRIG as HIGH
		time.sleep(0.00001)                      #Delay of 0.00001 seconds
		GPIO.output(self._trig, False)                 #Set TRIG as LOW

		while GPIO.input(self._echo)==0:               #Check whether the ECHO is LOW
			pulse_start = time.time()              #Saves the last known time of LOW pulse

		while GPIO.input(self._echo)==1:               #Check whether the ECHO is HIGH
			pulse_end = time.time()                #Saves the last known time of HIGH pulse 

		pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

		distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
		distance = round(distance, 2)            #Round to two decimal points

		if distance > 2 and distance < 400:      #Check whether the distance is within range
			self._logger.debug("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
			return distance
		else:
			self._logger.debug("Out Of Range")                   #display out of range
			return -1