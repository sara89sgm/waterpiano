#!/usr/bin/env python

from Adafruit_PWM_Servo_Driver import PWM

import time
import pygame
import pygame.midi
import sys
from pygame.locals import *

# Initialise the PWM device using the default address
pwm = PWM(0x40)
pwm1 = PWM(0x41)
# Note if you'd like more debug output you can instead run:
pwm = PWM(0x40, debug=True)

init_point  = 350
if len(sys.argv)>1:
	init_point = int(sys.argv[1])


servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096


pwm.setPWMFreq(50) 

for x in range(0, 11):
	pwm1.setPWM(x, 0, init_point)
	pwm1.setPWM(x, 4096, 0)

print "Servos initialised"



