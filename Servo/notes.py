#Importing GPIO module(CASE SENSITIVE)(REQUIRED)
import RPi.GPIO as GPIO
#Imports sleep for making servo sleep
from time import sleep
#Sets naming mode for naming of pins
GPIO.setmode(GPIO.BOARD)
# variable=GPIO.PWM(GPIO Pin#,50hz)
servo=GPIO.PWM(3,50)
# variable.start(Starting Value)
servo.start(0)

# Servo movement range is from 2.5 to 12.5
# 2.5   = completely turned right     (-90/0)
# 7.5   = turned middle               (0,90)
# 12.5  = completely turned left      (90/180)

# Formula for servo movement in Degrees
# x = degrees value
# y = (10.5/180 * x) + 2
# z = .1/60 * x  --- Formula for servo movement time in ms --- Servo movement speed is .1 sec/60 degrees
# servo.ChangeDutyCycle(y)
# time.sleep(z+.1)  ---  extra .1 considers for any errors or delays in servo runtime.

#Function for formula
def rotate(x):
    y = (10.5/180 * x) + 2
    z = .1/60 * x
    servo.ChangeDutyCycle(y)
    sleep(z)

#Function for formula with user input
def rotateInput():
    x=input("Enter Degrees Value")
    y = (10.5/180 * x) + 2
    z = .1/60 * x
    servo.ChangeDutyCycle(y)
    sleep(z)