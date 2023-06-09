import time
import pigpio
from py_classes.led import LED

class Fading(LED):
    def __init__(self, pin):
        super().__init__(pin)
        # self.frequency = frequency  # Get the frequency from the LED parent class
        self.range = 255

    def fade_in(self, duration, running):
        self.set_frequency(self.get_frequency())
        self.set_dutycycle(0)

        for dutycycle in range(0, self.range+1):
            self.set_dutycycle(dutycycle)
            time.sleep(duration / self.range)

    def fade_out(self, duration, running):
        self.set_frequency(self.get_frequency())
        self.set_dutycycle(self.range)

        for dutycycle in range(self.range, -1, -1):
            self.set_dutycycle(dutycycle)
            time.sleep(duration / self.range)

    # def stop(self):
    #     self.turn_off()


###################### NEW CLASS #####################

# class Fading():
#     def __init__(self, pin):
#         self.pin = pin

#     def fade(self, start_dutycycle, end_dutycycle, duration):
#         start_time = time.time()
#         steps = int(duration / 0.01)
#         dutycycle_step = (end_dutycycle - start_dutycycle) / steps
#         for step in range(steps):
#             dutycycle = start_dutycycle + (dutycycle_step * step)
#             self.set_dutycycle(int(dutycycle))
#             time.sleep(0.01)


