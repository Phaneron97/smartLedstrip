import pigpio
import time

# GPIO pins
PIN_12 = 12
PIN_13 = 13
PIN_18 = 18

# Initialize pigpio
pi = pigpio.pi()

# Set initial duty cycle and frequency
initial_duty_cycle = 0  # Range: 0-255
initial_frequency = 100  # Frequency in Hz

# Set the initial duty cycle and frequency for each pin
pi.set_PWM_dutycycle(PIN_12, initial_duty_cycle)
pi.set_PWM_frequency(PIN_12, initial_frequency)

while True:
   for i in range(0, 255, 1):
      pi.set_PWM_dutycycle(PIN_12, i)
      time.sleep(0.01)
   for i in range(255, 0, -1):
      pi.set_PWM_dutycycle(PIN_12, i)
      time.sleep(0.01)