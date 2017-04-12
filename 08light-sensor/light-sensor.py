#!/usr/bin/env python
# encoding: utf-8

# http://www.cnblogs.com/wpf_gd/articles/4700789.html

import RPi.GPIO as GPIO
from time import sleep

CHANNEL = 7

GPIO.setmode(GPIO.BOARD)

GPIO.setup(CHANNEL, GPIO.OUT)
GPIO.output(CHANNEL, GPIO.LOW)
sleep(0.5)
GPIO.setup(CHANNEL, GPIO.IN)

try:
  while True:
    print GPIO.input(CHANNEL)
    if GPIO.input(CHANNEL) == GPIO.HIGH:
      print '暗'
    else:
      print '亮'
    sleep(1)

except KeyboardInterrupt:
  pass
