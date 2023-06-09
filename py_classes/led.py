import pigpio
import time

class LED:
    def __init__(self, pin):
        self.pin = pin
        self.pi = pigpio.pi() # initialize pigpio
        self.pi.set_mode(self.pin, pigpio.OUTPUT) # set pin as output
        self.current_dutycycle = 0
        self.current_frequency = 100

    def set_dutycycle(self, dutycycle):
        self.pi.set_PWM_dutycycle(self.pin, dutycycle)
        self.current_dutycycle = dutycycle

    def get_dutycycle(self):
        return self.current_dutycycle

    def set_frequency(self, frequency):
        self.pi.set_PWM_frequency(self.pin, frequency)
        self.current_frequency = frequency

    def get_frequency(self):
        return self.current_frequency

    # def set_sleep(self, sleeptime):
    #     time.sleep(sleeptime)

    def turn_off(self):
        self.set_dutycycle(0)