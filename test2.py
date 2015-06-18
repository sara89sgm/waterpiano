#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:

# sg90: 500-2400 us
# default 150 -600
servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

pwm.setPWMFreq(50)                        # Set frequency to 60 Hz

for i in xrange(12):
  print i
  # Change speed of continuous servo on channel O
  pwm.setPWM(i, 0, 350)
  time.sleep(.1)
  pwm.setPWM(i, 0, 300)
  time.sleep(.1)
  
  # turn servo off
  pwm.setPWM(i, 4096, 0)
  time.sleep(.5)



