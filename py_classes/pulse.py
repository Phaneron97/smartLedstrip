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
        self.set_duty_cycle(0)

        for duty_cycle in range(0, self.range+1):
            self.set_duty_cycle(duty_cycle)
            time.sleep(duration / self.range)

        for duty_cycle in range(self.range, -1, -1):
            self.set_duty_cycle(duty_cycle)
            time.sleep(duration / self.range)

    def stop(self):
        self.led.turn_off()

###################### NEW CLASS #####################

# class Pulsing():
#     def __init__(self, pin):
#         self.pin = pin

#     def pulse(self, min_duty_cycle, max_duty_cycle, frequency, duration):
#         start_time = time.time()
#         while time.time() - start_time < duration:
#             for duty_cycle in range(min_duty_cycle, max_duty_cycle + 1):
#                 self.set_duty_cycle(duty_cycle)
#                 self.set_frequency(frequency)
#                 time.sleep(0.01)
#             for duty_cycle in range(max_duty_cycle, min_duty_cycle - 1, -1):
#                 self.set_duty_cycle(duty_cycle)
#                 self.set_frequency(frequency)
#                 time.sleep(0.01)

#     def start_pulse(self, min_duty_cycle, max_duty_cycle, frequency, duration):
#         self.pulse(min_duty_cycle, max_duty_cycle, frequency, duration)
#         self.turn_off()