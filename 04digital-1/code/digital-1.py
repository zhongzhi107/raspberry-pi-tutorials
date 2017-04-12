#!/usr/bin/env python
# encoding: utf-8

'''
该程序实现 9 --> 0 倒计时效果
接线图：
RPi    digital
7  <---> 3
11 <---> 7
13 <---> 6
15 <---> 4
29 <---> 2
31 <---> 1
33 <---> 9
35 <---> 10
37 <---> 5
'''

import RPi.GPIO as GPIO
import time

# 正极使用的针脚
LED_POWER = 7
# A－G管分别使用的针脚
LED_A = 11
LED_B = 13
LED_C = 15
LED_D = 29
LED_E = 31
LED_F = 33
LED_G = 35
LED_DP = 37

# 重置数码管，熄灭所有数字
def reset():
  GPIO.output(LED_POWER, GPIO.LOW)
  GPIO.output((LED_A, LED_B, LED_C, LED_D, LED_E, LED_F, LED_G, LED_DP), GPIO.HIGH)

# 显示数字0
def show0():
  reset()
  GPIO.output(LED_POWER, GPIO.HIGH)
  GPIO.output((LED_A, LED_B, LED_C, LED_D, LED_E, LED_F), GPIO.LOW)

# 显示数字1
def show1():
  reset()
  GPIO.output(LED_POWER, GPIO.HIGH)
  GPIO.output((LED_B, LED_C), GPIO.LOW)

# 显示数字2
def show2():
  reset()
  GPIO.output(LED_POWER, GPIO.HIGH)
  GPIO.output((LED_A, LED_B, LED_D, LED_E, LED_G), GPIO.LOW)

# 显示数字3
def show3():
  reset()
  GPIO.output(LED_POWER, GPIO.HIGH)
  GPIO.output((LED_A, LED_B, LED_C, LED_D, LED_G), GPIO.LOW)

# 显示数字4
def show4():
  reset()
  GPIO.output(LED_POWER, GPIO.HIGH)
  GPIO.output((LED_B, LED_C, LED_F, LED_G), GPIO.LOW)

# 显示数字5
def show5():
  reset()
  GPIO.output(LED_POWER, GPIO.HIGH)
  GPIO.output((LED_A, LED_C, LED_D, LED_F, LED_G), GPIO.LOW)

# 显示数字6
def show6():
  reset()
  GPIO.output(LED_POWER, GPIO.HIGH)
  GPIO.output((LED_A, LED_C, LED_D, LED_E, LED_F, LED_G), GPIO.LOW)

# 显示数字7
def show7():
  reset()
  GPIO.output(LED_POWER, GPIO.HIGH)
  GPIO.output((LED_A, LED_B, LED_C), GPIO.LOW)

# 显示数字8
def show8():
  reset()
  GPIO.output(LED_POWER, GPIO.HIGH)
  GPIO.output((LED_A, LED_B, LED_C, LED_D, LED_E, LED_F, LED_G), GPIO.LOW)

# 显示数字9
def show9():
  reset()
  GPIO.output(LED_POWER, GPIO.HIGH)
  GPIO.output((LED_A, LED_B, LED_C, LED_D, LED_F, LED_G), GPIO.LOW)

GPIO.setmode(GPIO.BOARD)

# 初始化引脚输出模式
GPIO.setup((LED_POWER, LED_A, LED_B, LED_C, LED_D, LED_E, LED_F, LED_G, LED_DP), GPIO.OUT)

# 倒计时程序
function_directory = locals()
for i in range(0, 10)[::-1]:
  function_directory['show%s'%(i)]()
  time.sleep(1)

GPIO.cleanup()
