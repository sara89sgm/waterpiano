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


pwm.setPWMFreq(50) 

#for x in range(0, 11):
	#pwm1.setPWM(x, 0, init_point)
	#print "Writing servo ", x
	#time.sleep(0.5)

for x in range(0, 11):
        pwm.setPWM(x, 0, init_point)
	print "Writing servo ", x
	time.sleep(0.5)

for x in range(0, 11):
        pwm1.setPWM(x, 4096, 0)
        time.sleep(0.05)

for x in range(0, 11):
        pwm.setPWM(x,4096, 0)
        time.sleep(0.05)

print "Servos initialised"

def playGlassNote(note):
	if(note>59):
		servo_number = note-47
		pwm.setPWM(servo_number,0, 270)
		time.sleep(1)
		pwm.setPWM(servo_number, 0, init_point)
	else :
		servo_number = note-59
		pwm1.setPWM(servo_number, 0, 270) 
		time.sleep(1)
		pwm.setPWM(servo_number, 0, init_point)
#MIDI

pygame.init()

pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post

pygame.midi.init()

print "There are " + str(pygame.midi.get_count()) + " MIDI devices"

print "The default input device number is "  + str(pygame.midi.get_default_input_id())

print pygame.midi.get_default_input_id()
input_id = pygame.midi.get_default_input_id()
print pygame.midi.get_device_info(2)

#Initalise piano keyboard as input

piano = pygame.midi.Input(3)


print "starting"

going = True

while going:

        events = event_get()
        for e in events:
                if e.type in [QUIT]:
                        going = False
                if e.type in [KEYDOWN]:
                        going = False

        if piano.poll():
                midi_events = piano.read(10)
                if int(midi_events[0][0][0]) in [224,225,226]:#Pitch Bender
                        print str(midi_events[0][0][2])#right(0)  center(64)  left(124)

                print "full midi_events " + str(midi_events)
                print "my midi note is " + str(midi_events[0][0][1])
		playGlassNote(midi_events[0][0][1])
                # convert them into pygame events.
                #midi_evs = pygame.midi.midis2events(midi_events, piano.device_id)

                #for m_e in midi_evs:
                        #event_post( m_e )

print "exit button clicked."
i.close()
for x in range(0, 11): 
        pwm1.setPWM(x, 4096, 0)
        time.sleep(0.05)

for x in range(0, 11):
        pwm.setPWM(x,4096, 0)
        time.sleep(0.05)
pygame.midi.quit()
pygame.quit()
exit()


