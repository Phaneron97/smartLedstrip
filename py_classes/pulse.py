import time
import pigpio
from py_classes.led import LED

class Pulsing:
    def __init__(self, pin, frequency=100, range_=100):
        self.led = LED(pin)
        self.frequency = frequency
        self.range = range_

    def pulse(self, duration):
        self.led.set_frequency(self.frequency)
        self.led.set_duty_cycle(0)

        for duty_cycle in range(0, self.range+1):
            self.led.set_duty_cycle(duty_cycle)
            time.sleep(duration / self.range)

        for duty_cycle in range(self.range, -1, -1):
            self.led.set_duty_cycle(duty_cycle)
            time.sleep(duration / self.range)

    def stop(self):
        self.led.turn_off()