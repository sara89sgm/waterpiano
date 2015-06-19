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

init_point  = 166
if len(sys.argv)>1:
	init_point = int(sys.argv[1])


servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

delay_hit = 0.07

def resetServos (motor, freq):
	global delay_hit
	motor.setPWMFreq(freq) 

	for x in range(0, 12):
		print "Reseting servo ", x
		motor.setPWM(x, 0, 270)
        	time.sleep(delay_hit)
		motor.setPWM(x, 0, init_point)
		time.sleep(delay_hit)
        	motor.setPWM(x, 4096, 0)
        	time.sleep(delay_hit)

resetServos(pwm1, 50)
resetServos(pwm, 50)

print "Servos initialised"

play_note = True

def playGlassNote(note):
	global play_note
	global delay_hit
	if(play_note):
		play_note = False
		if(note>59):
			servo_number = note-60
			print "Note ", note
			print "servo_number ", servo_number
			pwm.setPWM(servo_number,0, 270)
			time.sleep(delay_hit)
			pwm.setPWM(servo_number, 0, init_point)
			time.sleep(delay_hit)
			pwm.setPWM(servo_number, 4096, 0)
		else :
			servo_number = note-48
			pwm1.setPWM(servo_number, 0, 400) 
			time.sleep(delay_hit)
			pwm1.setPWM(servo_number, 0, init_point)
			time.sleep(delay_hit)
			pwm1.setPWM(servo_number, 4096, 0)
	else:
		play_note = True
#MIDI

exit()


