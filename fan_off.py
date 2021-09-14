#!/usr/bin/env python
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
#switch off GPO26
GPIO.output(26, GPIO.HIGH)
GPIO.cleanup()
