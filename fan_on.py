#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
#switch on Relay with GPO26
GPIO.output(26, GPIO.LOW)
