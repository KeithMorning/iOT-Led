'''
Author: your name
Date: 2020-12-22 23:02:47
LastEditTime: 2020-12-23 00:01:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /led/src/Relay.py
'''

from machine import ADC
from machine import Pin

class Relay():

    def __init__(self, pin):
        self.relaypin = Pin(pin, Pin.OUT)

    def set_state(self, state):
        print("relay will be "+str(state))
        state = 0 if state else 1
        self.relaypin.value(state)

    def state(self):
        return self.relaypin.value()
