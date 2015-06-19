#!/usr/bin/env python

from Adafruit_PWM_Servo_Driver import PWM

import time
import sys


# Initialise the PWM device using the default address
pwm = PWM(0x40)
pwm1 = PWM(0x41)

init_point  = 166
if len(sys.argv)>1:
        init_point = int(sys.argv[1])

delay_hit = 0.07


def resetServos(motor, freq):
        motor.setPWMFreq(freq)

        for x in range(0, 12):
                print "LReseting servo ", x
                motor.setPWM(x, 0, 270)
                time.sleep(delay_hit)
                motor.setPWM(x, 0, init_point)
                time.sleep(delay_hit)
                motor.setPWM(x, 4096, 0)
                time.sleep(delay_hit)




def playGlassNote(note):
        global delay_hit

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
                pwm1.setPWM(servo_number, 0, 270)
                time.sleep(delay_hit)
                pwm1.setPWM(servo_number, 0, init_point)
                time.sleep(delay_hit)
                pwm1.setPWM(servo_number, 4096, 0)


def playTwinkle():
	playGlassNote(55)
	time.sleep(0.5)
	playGlassNote(55)
	time.sleep(0.5)
	playGlassNote(62)
        time.sleep(0.5)
        playGlassNote(62)
        time.sleep(0.5)
	playGlassNote(64)
	time.sleep(0.5)
	playGlassNote(64)
	time.sleep(0.5)
	playGlassNote(62)
	time.sleep(1)
	playGlassNote(60)
        time.sleep(0.5)
        playGlassNote(60)
        time.sleep(0.5)
	playGlassNote(59)
        time.sleep(0.5)
        playGlassNote(59)
        time.sleep(0.5)
	playGlassNote(57)
        time.sleep(0.5)
        playGlassNote(57)
        time.sleep(0.5)
	playGlassNote(55)
	time.sleep(1)
	playGlassNote(62)
        time.sleep(0.5)
        playGlassNote(62)
        time.sleep(0.5)
	playGlassNote(60)
        time.sleep(0.5)
        playGlassNote(60)
        time.sleep(0.5)
	playGlassNote(59)
        time.sleep(0.5)
        playGlassNote(59)
        time.sleep(0.5)
        playGlassNote(57)
        time.sleep(1)
	playGlassNote(62)
        time.sleep(0.5)
        playGlassNote(62)
        time.sleep(0.5)
        playGlassNote(60)
        time.sleep(0.5)
        playGlassNote(60)
        time.sleep(0.5)
        playGlassNote(59)
        time.sleep(0.5)
        playGlassNote(59)
        time.sleep(0.5)
        playGlassNote(57)
        time.sleep(1)
	playGlassNote(60)
        time.sleep(0.5)
        playGlassNote(60)
        time.sleep(0.5)
        playGlassNote(59)
        time.sleep(0.5)
        playGlassNote(59)
        time.sleep(0.5)
        playGlassNote(57)
        time.sleep(0.5)
        playGlassNote(57)
        time.sleep(0.5)
        playGlassNote(55)
        time.sleep(1)
        playGlassNote(62)
        time.sleep(0.5)
        playGlassNote(62)
        time.sleep(0.5)
        playGlassNote(60)
        time.sleep(0.5)
        playGlassNote(60)
        time.sleep(0.5)
        playGlassNote(59)
        time.sleep(0.5)
        playGlassNote(59)
        time.sleep(0.5)
        playGlassNote(57)
        time.sleep(1)
def playShakeItOff():

        playGlassNote(64)
        playGlassNote(67)
        playGlassNote(69)
        playGlassNote(69)
        playGlassNote(71)
        playGlassNote(67)
        time.sleep(0.5)
        playGlassNote(64)
        time.sleep(0.5)
        playGlassNote(62)
        playGlassNote(59)
        playGlassNote(57)
        playGlassNote(55)
        playGlassNote(55)
        playGlassNote(55)
        time.sleep(0.5)
        playGlassNote(69)
        playGlassNote(69)
        playGlassNote(69)
        playGlassNote(71)
        playGlassNote(67)
        playGlassNote(64)

playTwinkle()
