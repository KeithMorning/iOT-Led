'''
Author: Keith
Date: 2020-12-22 21:40:51
LastEditTime: 2020-12-22 23:28:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /code/Button.py
'''
from machine import Pin

class Button():
    def __init__(self,pin):
        self.pin = Pin(pin,Pin.IN)
    
    def state(self):
        return self.pin.value()