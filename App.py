# import Weather
# import Message

from gpiozero import Motor
from time import sleep

in1 = 24
in2 = 23
en = 25
temp1=1

frontMotors = Motor(in1, in2)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(in1,GPIO.OUT)
# GPIO.setup(in2,GPIO.OUT)
# GPIO.setup(en,GPIO.OUT)
# GPIO.output(in1,GPIO.LOW)
# GPIO.output(in2,GPIO.LOW)
# p=GPIO.PWM(en,1000)

# p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

speed = 1

while(1):

    x=chr(input())
    
    if x=='r':
        print("run")
        if(temp1==1):
         frontMotors.forward(speed)
         print("forward")
         x='z'
        else:
         frontMotors.backward(speed)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        frontMotors.stop()
        x='z'

    elif x=='f':
        print("forward")
        frontMotors.forward(speed)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        frontMotors.backward(speed)
        temp1=0
        x='z'

    elif x=='-':
        speed-=0.2
    
    elif x=='+':
        speed+=0.2

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

# print(Message.sendMessage(""))
# print(Weather.getCurrentWeather())