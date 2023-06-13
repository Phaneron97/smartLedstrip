import time
import pigpio
from py_classes.led import LED

class Pulsing(LED):
    def __init__(self, pin):
        super().__init__(pin)
        # self.frequency = frequency
        self.range = 255

    def pulse(self, duration, running = True):
        self.set_frequency(self.get_frequency())
        self.set_dutycycle(0)

        for dutycycle in range(0, self.range+1):
            self.set_dutycycle(dutycycle)
            time.sleep(duration / self.range)

        for dutycycle in range(self.range, -1, -1):
            self.set_dutycycle(dutycycle)
            time.sleep(duration / self.range)

    def stop(self):
        self.led.turn_off()