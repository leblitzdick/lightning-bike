import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# power switch relais
power = 18

GPIO.setup(power, GPIO.OUT)

GPIO.output(power, GPIO.LOW)
time.sleep(30)
GPIO.output(power, GPIO.HIGH) 

GPIO.cleanup()



