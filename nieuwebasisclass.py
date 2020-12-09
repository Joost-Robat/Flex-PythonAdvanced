import pygame
from pygame import *
import time

characterAmount = 0

class character0 :
    _speed = 40
    _strength = 80
    _magic = 10
    _lifepoints = 90
    _points = 100

    def __init__(self):
        characterAmount =+ 1
        print("Character amount is now " + str(characterAmount) + ".")

    def Die(self):
        if character0._lifepoints == 0:
            print(self + "just died!")
            del (self)
        else:
            pass

class Endboss(character0) :
    _strength = 150
    _lifepoints = 1000

    def SMASH(self) :
        print("The Endboss used it's powerfull fist to SMASH!")
        if KEYDOWN != K_RIGHT or KEYDOWN != K_LEFT:
            character0._lifepoints =- 25

player0 = character0()
endboss0 = Endboss()

endboss0.SMASH()
time.sleep(1)
print(player0._lifepoints)
endboss0.SMASH()
time.sleep(1)
print(player0._lifepoints)
endboss0.SMASH()
time.sleep(1)
print(player0._lifepoints)
endboss0.SMASH()
time.sleep(1)
print(player0._lifepoints)

player0.Die()
