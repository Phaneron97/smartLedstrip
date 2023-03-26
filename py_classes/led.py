import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class LED:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 100)
        self.pwm.start(0)
        self.current_duty_cycle = 0

    def set_duty_cycle(self, duty_cycle):
        self.pwm.ChangeDutyCycle(duty_cycle)
        self.current_duty_cycle = duty_cycle
    
    def get_duty_cycle(self):
        return self.current_duty_cycle

    def set_frequency(self, frequency):
        self.pwm.ChangeFrequency(frequency)

    def set_sleep(self, sleeptime):
        time.sleep(sleeptime)

# class LED:
#     def __init__(self, pin):
#         self.pin = pin
#         GPIO.setup(self.pin, GPIO.OUT)
#         self.pwm = GPIO.PWM(self.pin, 100)
#         self.pwm.start(0)
#         self.current_duty_cycle = 0

#     def set_duty_cycle(self, duty_cycle, transition_time=0):
#         if transition_time == 0:
#             self.pwm.ChangeDutyCycle(duty_cycle)
#             self.current_duty_cycle = duty_cycle
#             return

#         duty_cycle_step = (duty_cycle - self.current_duty_cycle) / (transition_time * 10)

#         for i in range(10):
#             self.pwm.ChangeDutyCycle(self.current_duty_cycle + (duty_cycle_step * i))
#             time.sleep(transition_time / 10)
#         self.pwm.ChangeDutyCycle(duty_cycle)
#         self.current_duty_cycle = duty_cycle
