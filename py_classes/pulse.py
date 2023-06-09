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

###################### NEW CLASS #####################

# class Pulsing():
#     def __init__(self, pin):
#         self.pin = pin

#     def pulse(self, min_dutycycle, max_dutycycle, frequency, duration):
#         start_time = time.time()
#         while time.time() - start_time < duration:
#             for dutycycle in range(min_dutycycle, max_dutycycle + 1):
#                 self.set_dutycycle(dutycycle)
#                 self.set_frequency(frequency)
#                 time.sleep(0.01)
#             for dutycycle in range(max_dutycycle, min_dutycycle - 1, -1):
#                 self.set_dutycycle(dutycycle)
#                 self.set_frequency(frequency)
#                 time.sleep(0.01)

#     def start_pulse(self, min_dutycycle, max_dutycycle, frequency, duration):
#         self.pulse(min_dutycycle, max_dutycycle, frequency, duration)
#         self.turn_off()