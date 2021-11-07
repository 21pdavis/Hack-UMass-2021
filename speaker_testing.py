import RPi.GPIO as GPIO
from time import sleep

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

while(1):
    GPIO.output(4, GPIO.HIGH)
    sleep(0.0005)
    GPIO.output(4, GPIO.LOW)
    sleep(0.0005)

    print(GPIO.input(4))

    x = str(input())
    if x == 'a':
        GPIO.cleanup()
        break