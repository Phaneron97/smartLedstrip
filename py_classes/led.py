import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

class LED:
    pwm_objects = {}
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        # self.pwm = GPIO.PWM(self.pin, 100)
        if self.pin not in LED.pwm_objects:
            self.pwm = GPIO.PWM(self.pin, 1000)
            self.pwm.start(0)
            LED.pwm_objects[self.pin] = self.pwm
        else:
            self.pwm = LED.pwm_objects[self.pin]
        self.pwm.start(0)
        self.current_duty_cycle = 0
        self.current_frequency = 0

    # def __init__(self, pin):
    #     self.pin = pin
    #     GPIO.setup(self.pin, GPIO.OUT)
    #     self.pwm = GPIO.PWM(self.pin, 100)
    #     self.pwm.start(0)
    #     self.current_duty_cycle = 0

    def set_duty_cycle(self, duty_cycle):
        self.pwm.ChangeDutyCycle(duty_cycle)
        self.current_duty_cycle = duty_cycle # store duty cycle (brightness) to get value later
    
    def get_duty_cycle(self):
        return self.current_duty_cycle

    def set_frequency(self, frequency):
        self.pwm.ChangeFrequency(frequency)
        self.current_frequency = frequency # store frequency to get value later

    def get_frequency(self):
        return self.current_frequency

    def set_sleep(self, sleeptime):
        time.sleep(sleeptime)

    def turn_off(self):
        self.set_duty_cycle(0) # no duty cycle
        # self.set_frequency(0) # no frequency