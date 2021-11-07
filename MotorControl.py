# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO
# import TextToSpeech
import DistanceSensor as distsensor
from bluedot import BlueDot
from time import sleep
import sprite_animation_final
import os
import sys
import pygame

# odd numbers are forwards, even numbers are backwards
in_dict = {1: 23, 2: 24, 3: 27, 4: 17, 5: 6, 6: 5, 7: 12, 8: 16}

en_dict = {1: 25, 2: 22, 3: 13, 4: 26}

temp1 = 1

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
for port in in_dict:
    GPIO.setup(in_dict[port], GPIO.OUT)

for port in en_dict:
    GPIO.setup(en_dict[port], GPIO.OUT)

for port in in_dict:
    GPIO.output(in_dict[port], GPIO.LOW)

p_dict = {1: GPIO.PWM(en_dict[1], 750), 2: GPIO.PWM(en_dict[2], 1000), 3: GPIO.PWM(en_dict[3], 1000),
          4: GPIO.PWM(en_dict[4], 750)}

p_dict[1].ChangeDutyCycle(100)
p_dict[2].ChangeDutyCycle(100)
p_dict[3].ChangeDutyCycle(100)
p_dict[4].ChangeDutyCycle(100)

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
    p_dict[1].ChangeDutyCycle(100)
    p_dict[2].ChangeDutyCycle(50)
    p_dict[3].ChangeDutyCycle(50)
    p_dict[4].ChangeDutyCycle(100)
    moveForward()


def turnRight():
    p_dict[1].ChangeDutyCycle(50)
    p_dict[2].ChangeDutyCycle(100)
    p_dict[3].ChangeDutyCycle(100)
    p_dict[4].ChangeDutyCycle(50)
    moveForward()


bd = BlueDot(cols=2)
bd[0,0].color = "blue"
bd[1,0].color = "red"
bd[1,0].square = True

pygame.init()
clock = pygame.time.Clock()

screen_width = 100
screen_height = 50
screen = pygame.display.set_mode((screen_width, screen_height),pygame.FULLSCREEN)
pygame.display.set_caption("Sprite Animation")
os.environ["DISPLAY"] = ":0"
pygame.display.init()

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = sprite_animation_final.Player(100, 100)
moving_sprites.add(player)

def move(pos):
    print("pressed circle")
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

def square():
    print("pressed square")
    print("before: "+str(player.attack_animation))
    player.attack()
    print("after: "+str(player.attack_animation))
    print("Measured Distance = %.1f cm" % dist.distance())
    sleep(1)
    

for p in p_dict:
    p_dict[p].start(25)

dist = distsensor.DistanceSensor()

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while (1):

    bd[0,0].when_pressed = move
    bd[0,0].when_moved = move
    bd[1,0].when_pressed = square

    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    player.update(0.15)
    pygame.display.flip()
    clock.tick(60)

    # x = str(input())
    # if x == 'a':
    #     print("before: "+str(player.attack_animation))
    #     if(player.attack_animation==False):
    #         player.attack()
    #     else:
    #         print("already animating")
    #     print("after: "+str(player.attack_animation))
    #     x = 'z'
    # elif x == 'd':
    #     print("Raw Distance = "+str(dist.distance()))
    #     print("Measured Distance = %.1f cm" % dist.distance())
    #     sleep(1)
    #     x = 'z'
    # elif x == '[':
    #     print("text to speech")
    #     TextToSpeech.play("Hello World")
    #     x = 'z'

    # elif x == '1':
    #     turnLeft()

    #     x='z'
    # elif x=='2':
    #     turnRight()
    #     x='z'
    # elif x=='r':
    #     print("run")
    #     if(temp1==1):
    #      moveForward()
    #      x='z'
    #     else:
    #      moveBackward()
    #      x='z'


    # elif x=='s':
    #     stopMotors()
    #     x = 'z'

    # elif x=='f':
    #     moveForward()
    #     temp1 = 1
    #     x = 'z'


    # elif x=='b':
    #     moveBackward()
    #     temp1 = 0
    #     x = 'z'

    # elif x == 'l':
    #     print("low")
    #     p_dict[1].ChangeDutyCycle(75)
    #     p_dict[2].ChangeDutyCycle(75)
    #     p_dict[3].ChangeDutyCycle(75)
    #     p_dict[4].ChangeDutyCycle(75)
    #     x = 'z'

    # elif x == 'h':
    #     print("high")
    #     p_dict[1].ChangeDutyCycle(100)
    #     p_dict[2].ChangeDutyCycle(100)
    #     p_dict[3].ChangeDutyCycle(100)
    #     p_dict[4].ChangeDutyCycle(100)
    #     x = 'z'
    
    # elif x=='e':
    #     GPIO.cleanup()
    #     print("GPIO Clean up")
    #     break

    # else:
    #     print("<<<  wrong data  >>>")
    #     print("please enter the defined data to continue.....")

    if(dist.distance()<=20):
        GPIO.output(in_dict[1], GPIO.LOW)
        GPIO.output(in_dict[3], GPIO.LOW)
        GPIO.output(in_dict[5], GPIO.LOW)
        GPIO.output(in_dict[7], GPIO.LOW)