# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO
import TextToSpeech
import DistanceSensor
from bluedot import BlueDot
from time import sleep

# odd numbers are forwards, even numbers are backwards
in_dict = {1: 23, 2: 24, 3: 27, 4: 17, 5: 6, 6: 5, 7: 12, 8: 16}

en_dict = {1: 25, 2: 22, 3: 13, 4: 26}

temp1 = 1

GPIO.setmode(GPIO.BCM)
for port in in_dict:
    GPIO.setup(in_dict[port], GPIO.OUT)

for port in en_dict:
    GPIO.setup(en_dict[port], GPIO.OUT)

for port in in_dict:
    GPIO.output(in_dict[port], GPIO.LOW)

p_dict = {1: GPIO.PWM(en_dict[1], 1000), 2: GPIO.PWM(en_dict[2], 1000), 3: GPIO.PWM(en_dict[3], 1000),
          4: GPIO.PWM(en_dict[4], 1000)}


def moveForward():
    GPIO.output(in_dict[1], GPIO.HIGH)
    GPIO.output(in_dict[2], GPIO.LOW)
    GPIO.output(in_dict[3], GPIO.HIGH)
    GPIO.output(in_dict[4], GPIO.LOW)
    GPIO.output(in_dict[5], GPIO.HIGH)
    GPIO.output(in_dict[6], GPIO.LOW)
    GPIO.output(in_dict[7], GPIO.HIGH)
    GPIO.output(in_dict[8], GPIO.LOW)


def moveBackward():
    GPIO.output(in_dict[1], GPIO.LOW)
    GPIO.output(in_dict[2], GPIO.HIGH)
    GPIO.output(in_dict[3], GPIO.LOW)
    GPIO.output(in_dict[4], GPIO.HIGH)
    GPIO.output(in_dict[5], GPIO.LOW)
    GPIO.output(in_dict[6], GPIO.HIGH)
    GPIO.output(in_dict[7], GPIO.LOW)
    GPIO.output(in_dict[8], GPIO.HIGH)


def stopMotors():
    GPIO.output(in_dict[1], GPIO.LOW)
    GPIO.output(in_dict[2], GPIO.LOW)
    GPIO.output(in_dict[3], GPIO.LOW)
    GPIO.output(in_dict[4], GPIO.LOW)
    GPIO.output(in_dict[5], GPIO.LOW)
    GPIO.output(in_dict[6], GPIO.LOW)
    GPIO.output(in_dict[7], GPIO.LOW)
    GPIO.output(in_dict[8], GPIO.LOW)


def turnLeft():
    GPIO.output(in_dict[1], GPIO.HIGH)
    GPIO.output(in_dict[2], GPIO.LOW)
    GPIO.output(in_dict[3], GPIO.LOW)
    GPIO.output(in_dict[4], GPIO.HIGH)
    GPIO.output(in_dict[5], GPIO.HIGH)
    GPIO.output(in_dict[6], GPIO.LOW)
    GPIO.output(in_dict[7], GPIO.LOW)
    GPIO.output(in_dict[8], GPIO.HIGH)


def turnRight():
    GPIO.output(in_dict[1], GPIO.LOW)
    GPIO.output(in_dict[2], GPIO.HIGH)
    GPIO.output(in_dict[3], GPIO.HIGH)
    GPIO.output(in_dict[4], GPIO.LOW)
    GPIO.output(in_dict[5], GPIO.LOW)
    GPIO.output(in_dict[6], GPIO.HIGH)
    GPIO.output(in_dict[7], GPIO.HIGH)
    GPIO.output(in_dict[8], GPIO.LOW)


bd = BlueDot()


def move(pos):
    if pos.top:
        moveForward()
    elif pos.bottom:
        moveBackward()
    elif pos.left:
        turnLeft()
    elif pos.right:
        turnRight()
    elif pos.middle:
        stopMotors()


for p in p_dict:
    p_dict[p].start(25)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while (1):

    bd.when_pressed = move
    bd.when_moved = move

    x = str(input())
    if x == 'd':
        dist = DistanceSensor.distance()
        print("Measured Distance = %.1f cm" % dist)
        sleep(1)
    elif x == '[':
        print("text to speech")
        TextToSpeech.play("Hello World")
        x = 'z'

    elif x == '1':
        turnLeft()

        x='z'
    elif x=='2':
        turnRight()
        x='z'
    elif x=='r':
        print("run")
        if(temp1==1):
         moveForward()
         x='z'
        else:
         moveBackward()
         x='z'


    elif x=='s':
        stopMotors()
        x = 'z'

    elif x=='f':
        moveForward()
        temp1 = 1
        x = 'z'


    elif x=='b':
        moveBackward()
        temp1 = 0
        x = 'z'

    elif x == 'l':
        print("low")
        p_dict[1].ChangeDutyCycle(25)
        p_dict[2].ChangeDutyCycle(25)
        p_dict[3].ChangeDutyCycle(25)
        p_dict[4].ChangeDutyCycle(25)
        x = 'z'

    elif x == 'm':
        print("medium")
        p_dict[1].ChangeDutyCycle(50)
        p_dict[2].ChangeDutyCycle(50)
        p_dict[3].ChangeDutyCycle(50)
        p_dict[4].ChangeDutyCycle(50)
        x = 'z'

    elif x == 'h':
        print("high")
        p_dict[1].ChangeDutyCycle(75)
        p_dict[2].ChangeDutyCycle(75)
        p_dict[3].ChangeDutyCycle(75)
        p_dict[4].ChangeDutyCycle(75)
        x = 'z'
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")