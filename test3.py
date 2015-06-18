#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x41, debug=True)

# sg90: 500-2400 us
#500us = min
#1000us = -90
#1500us = 0
#2000us = 90
#2400us = max

HOME = .001500
MS_PER_DEG = .0005 / 45

FREQUENCY = 60

def calculate_duration(deg):
  '''Given a value from -90 to 90, return the needed pulse width'''
  return HOME + (deg * MS_PER_DEG)

def calculate_pulse(deg):
  dur = calculate_duration(deg)
  print int(dur * 100000)
  return int(calculate_duration(deg) * 60 * 4096)

def set_degree(p, servo, deg):
  p.setPWM(servo, 0, calculate_pulse(deg))
  
pwm.setPWMFreq(FREQUENCY)
for i in xrange(12):
  set_degree(pwm, i, int(sys.argv[1]))

time.sleep(.100)

print "turn all off"
for i in xrange(12):
  pwm.setPWM(i, 4096, 0)

#for i in xrange(18):
#	deg = (i * 10) - 90
#	pulses = calculate_pulse(deg)
#	print "%d -> %d" % (deg, pulses)
#	pwm.setPWM(8, 0, pulses)
#        time.sleep(.25)
