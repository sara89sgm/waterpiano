#!/usr/bin/env python

from Adafruit_PWM_Servo_Driver import PWM

import time
import pygame
import pygame.midi
import sys
from pygame.locals import *

pwm = PWM(0x40)
pwm.setPWMFreq(50) 

if len(sys.argv) < 4:
	print "usage: test.py <start> <end>";
	sys.exit(-1)

start = int(sys.argv[1])
end = int(sys.argv[2])

pwm.setPWM(0, start, end)
#pwm.setPWM(0, 4096, 0)
