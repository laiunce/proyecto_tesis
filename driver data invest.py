#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:36:08 2018

@author: laiunce
"""

import pyautogui
pyautogui.position() 

from time import sleep
sleep(1)


pyautogui.click(x=411, y=487, clicks=1, interval=0.5, button='left')

sleep(2)

pyautogui.click(x=871, y=576, clicks=1, interval=0.5, button='left')

pyautogui.click(x=466, y=666, clicks=1, interval=0.5, button='left')

pyautogui.typewrite(['backspace','backspace', '0', '1','enter'], interval=1)