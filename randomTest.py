import RPi.GPIO as GPIO
import time

red_pin = 12
green_pin = 13
blue_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

pwm = GPIO.PWM(red_pin, 100)
pwm.start(0)

# while True:
#     pwm.start(1)

for x in range(10):
    
    for i in range(0, 100, 1):
        pwm.ChangeDutyCycle(i)
        print(i)
        time.sleep(0.01)
    for i in range(100, 0, -1):
        pwm.ChangeDutyCycle(i)
        print(i)
        time.sleep(0.01)

GPIO.cleanup()