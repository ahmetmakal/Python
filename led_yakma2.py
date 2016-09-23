#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
for i in range(37,35,33,31,29):
    print i
    GPIO.setup(i, GPIO.OUT) 

sleep_time	= float(0.5)

try:
	while True:
		for b in range(37,35,33,31,29):
		GPIO.output(b, True)
		time.sleep(sleep_time)
		GPIO.output(b, False)


except KeyboardInterrupt: 
	GPIO.output(37,False)
	GPIO.output(35,False)
	GPIO.output(33,False)
	GPIO.output(31,False)
	GPIO.output(29,False)
	print('Cikis Yapildi')

finally:
	GPIO.cleaup()
