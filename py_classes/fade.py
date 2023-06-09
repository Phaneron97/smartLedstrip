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
        self.set_duty_cycle(0)

        for duty_cycle in range(0, self.range+1):
            self.set_duty_cycle(duty_cycle)
            time.sleep(duration / self.range)

    def fade_out(self, duration, running):
        self.set_frequency(self.get_frequency())
        self.set_duty_cycle(self.range)

        for duty_cycle in range(self.range, -1, -1):
            self.set_duty_cycle(duty_cycle)
            time.sleep(duration / self.range)

    # def stop(self):
    #     self.turn_off()


###################### NEW CLASS #####################

# class Fading():
#     def __init__(self, pin):
#         self.pin = pin

#     def fade(self, start_duty_cycle, end_duty_cycle, duration):
#         start_time = time.time()
#         steps = int(duration / 0.01)
#         duty_cycle_step = (end_duty_cycle - start_duty_cycle) / steps
#         for step in range(steps):
#             duty_cycle = start_duty_cycle + (duty_cycle_step * step)
#             self.set_duty_cycle(int(duty_cycle))
#             time.sleep(0.01)


