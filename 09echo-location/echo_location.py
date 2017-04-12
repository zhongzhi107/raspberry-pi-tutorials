#!/usr/bin/env python
# encoding: utf-8

'''
该程序每3秒测试一次距离，用ctrl+c停止。
原文：http://bbs.elecfans.com/forum.php?mod=viewthread&tid=451330

接线图:
Vcc  <---> 2  #5V
Trig <---> 14
Echo <---> 16
Gnd  <---> 6
'''

import RPi.GPIO as GPIO
import time

TRIG_CHANNEL = 14
ECHO_CHANNEL = 16

def detect_distance():
  # 发出触发信号
  GPIO.output(TRIG_CHANNEL, GPIO.HIGH)
  # 保持10us以上
  time.sleep(0.000015)
  GPIO.output(TRIG_CHANNEL, GPIO.LOW)

  while GPIO.input(ECHO_CHANNEL) == GPIO.LOW:
    pass
  # 发现高电压时，开始计时
  t1 = time.time()
  while GPIO.input(ECHO_CHANNEL) == GPIO.HIGH:
    pass
  # 高电压结束，停止计时
  t2 = time.time()
  # 返回距离，单位为米
  return (t2-t1)*340/2

GPIO.setmode(GPIO.BOARD)

GPIO.setup(TRIG_CHANNEL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO_CHANNEL, GPIO.IN)

time.sleep(2)

try:
  while True:
    print 'Distance: %0.2fm'%(detect_distance())
    time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()
