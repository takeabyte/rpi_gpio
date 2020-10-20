import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, GPIO.HIGH)
GPIO.output(26, 0)
GPIO.cleanup() 
