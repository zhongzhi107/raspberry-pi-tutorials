#!/usr/bin/env python
# encoding: utf-8

'''
该程序每 1 秒测试一次空气污染，用ctrl+c停止。
http://blog.csdn.net/ling3ye/article/details/51472533

接线图:
VCC <---> 1  #3.5V
GND <---> 6
DO  <---> 7
'''

import RPi.GPIO as GPIO
import time

CHANNEL = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(pin):
  print 'Sensor detected action!'

GPIO.add_event_detect(CHANNEL, GPIO.RISING)
GPIO.add_event_callback(CHANNEL, action)

try:
  while True:
    print 'alive'
    time.sleep(0.5)
except KeyboardInterrupt:
  GPIO.cleanup()
