#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)

sleep_time = raw_input('Sleep Time: ')

if not sleep_time:
	sleep_time	= 0.5

sleep_time	= float(sleep_time)

try:
	while True:
		GPIO.output(37,True)
		time.sleep(sleep_time)
		GPIO.output(37,False)
		GPIO.output(35,True)
		time.sleep(sleep_time)
		GPIO.output(35,False)
		GPIO.output(33,True)
		time.sleep(sleep_time)
		GPIO.output(33,False)
		GPIO.output(31,True)
		time.sleep(sleep_time)
		GPIO.output(31,False)
		GPIO.output(29,True)
		time.sleep(sleep_time)
		GPIO.output(29,False)

except KeyboardInterrupt: 
	GPIO.output(37,False)
	GPIO.output(35,False)
	GPIO.output(33,False)
	GPIO.output(31,False)
	GPIO.output(29,False)
	print('Cikis Yapildi')

finally:
	GPIO.cleaup()
