import RPi.GPIO as GPIO
from time import sleep

GPIO.setup(4, GPIO.OUT)

while(1):
    GPIO.output(4, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(4, GPIO.LOW)
    sleep(0.5)