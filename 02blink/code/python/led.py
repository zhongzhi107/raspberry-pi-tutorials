#!/usr/bin/env python
# encoding: utf-8

# 导入模块RPI.GPIO，命名为别名为GPIO
import RPi.GPIO as GPIO
# 导入time模块
import time

# 声明 GPIO 使用物理编号方式，也就是11号口就是物理编号11号口
GPIO.setmode(GPIO.BOARD)

# 声明11号口是用于输出模式
GPIO.setup(11, GPIO.OUT)

# 设置11号口为高电压，也就是11号口变为3.3伏
# 这行代码执行之后，11号口变为高电压，
# 那么根据电路原理，led灯就会亮起来
GPIO.output(11, GPIO.HIGH)

# 程序休眠3秒钟，程序休眠期间，led灯会一直亮着
time.sleep(3)

# 设置11号口为低电压，也就是11号口变为0伏，和GND一样
# 这行代码执行之后，11号口变为低电压，那么根据电路原理，led灯就会熄灭
GPIO.output(11, GPIO.LOW)

# 将所有的GPIO口状态恢复为初始化，一般代码结束都执行此代码，这是一个好习惯
GPIO.cleanup()
