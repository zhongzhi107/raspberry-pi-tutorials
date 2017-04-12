#!/usr/bin/env python
# encoding: utf-8

'''
接线图：
RPi    digital
7  <---> 10
11 <---> 5
13 <---> 3
15 <---> 9
29 <---> 8
31 <---> 6
33 <---> 7
35 <---> 4
37 <---> 1

'''

import RPi.GPIO as GPIO
import time
import os


# 数码管1-2正极分别使用的针脚
LED_POWER_1 = 7
LED_POWER_2 = 11

# A－G管分别使用的针脚
LED_A = 13
LED_B = 15
LED_C = 29
LED_D = 31
LED_E = 33
LED_F = 35
LED_G = 37

# 获取CPU温度
def get_cpu_temperature():
  return os.popen('vcgencmd measure_temp').read()[5:7]

# 重置数码管，熄灭所有数字
def reset():
  GPIO.output((LED_POWER_1, LED_POWER_2), GPIO.LOW)
  GPIO.output((LED_A, LED_B, LED_C, LED_D, LED_E, LED_F, LED_G), GPIO.HIGH)

# 设置第几个数码管亮起
def set_position(position):
  if position == 1:
    GPIO.output(LED_POWER_1, GPIO.HIGH)
  else:
    GPIO.output(LED_POWER_2, GPIO.HIGH)

# 显示数字0
def show0(p):
  reset()
  set_position(p)
  GPIO.output((LED_A, LED_B, LED_C, LED_D, LED_E, LED_F), GPIO.LOW)

# 显示数字1
def show1(p):
  reset()
  set_position(p)
  GPIO.output((LED_B, LED_C), GPIO.LOW)

# 显示数字2
def show2(p):
  reset()
  set_position(p)
  GPIO.output((LED_A, LED_B, LED_D, LED_E, LED_G), GPIO.LOW)

# 显示数字3
def show3(p):
  reset()
  set_position(p)
  GPIO.output((LED_A, LED_B, LED_C, LED_D, LED_G), GPIO.LOW)

# 显示数字4
def show4(p):
  reset()
  set_position(p)
  GPIO.output((LED_B, LED_C, LED_F, LED_G), GPIO.LOW)

# 显示数字5
def show5(p):
  reset()
  set_position(p)
  GPIO.output((LED_A, LED_C, LED_D, LED_F, LED_G), GPIO.LOW)

# 显示数字6
def show6(p):
  reset()
  set_position(p)
  GPIO.output((LED_A, LED_C, LED_D, LED_E, LED_F, LED_G), GPIO.LOW)

# 显示数字7
def show7(p):
  reset()
  set_position(p)
  GPIO.output((LED_A, LED_B, LED_C), GPIO.LOW)

# 显示数字8
def show8(p):
  reset()
  set_position(p)
  GPIO.output((LED_A, LED_B, LED_C, LED_D, LED_E, LED_F, LED_G), GPIO.LOW)

# 显示数字9
def show9(p):
  reset()
  set_position(p)
  GPIO.output((LED_A, LED_B, LED_C, LED_D, LED_F, LED_G), GPIO.LOW)

GPIO.setmode(GPIO.BOARD)

# 初始化引脚输出模式
GPIO.setup((LED_POWER_1, LED_POWER_2, LED_A, LED_B, LED_C, LED_D, LED_E, LED_F, LED_G), GPIO.OUT)

function_directory = locals()

try:
  while True:
    cpu_temperature = get_cpu_temperature()
    print 'CPU temperature = %s°C'%(cpu_temperature)

    loop = 0
    while loop < 200:
      loop += 1
      # 先显示高位
      position = 1
      for n in cpu_temperature:
        function_directory['show%s'%(n)](position)
        time.sleep(0.01)
        position += 1

except KeyboardInterrupt:
  GPIO.cleanup()
