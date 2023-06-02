import pigpio
import time

class LED:
    def __init__(self, pin):
        self.pin = pin
        self.pi = pigpio.pi() # initialize pigpio
        self.pi.set_mode(self.pin, pigpio.OUTPUT) # set pin as output
        self.current_duty_cycle = 0
        self.current_frequency = 100

    def set_duty_cycle(self, duty_cycle):
        self.pi.set_PWM_dutycycle(self.pin, duty_cycle)
        self.current_duty_cycle = duty_cycle

    def get_duty_cycle(self):
        return self.current_duty_cycle

    def set_frequency(self, frequency):
        self.pi.set_PWM_frequency(self.pin, frequency)
        self.current_frequency = frequency

    def get_frequency(self):
        return self.current_frequency

    def set_sleep(self, sleeptime):
        time.sleep(sleeptime)

    def turn_off(self):
        self.set_duty_cycle(0)