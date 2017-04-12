#!/usr/bin/env python
# encoding: utf-8

'''
该程序通过传感器获取温度、湿度数据
接线图：
RPi     DHT11
1  <---> VCC
12 <---> DATA
-- <---> N/A
6  <---> GND
'''

import RPi.GPIO as GPIO
import time
from util import bin2dec

CHANNEL = 12
MAX_TIMES = 10

# 通过传感器获取温度、湿度数据
def get_data():
  # 建议连接线长度短于 20 米时用 5K 上拉电阻 , 大于 20 米时根据实际情况使用合适的上拉电阻
  GPIO.setmode(GPIO.BOARD)
  # 要等待 1s 以越过不稳定状态，在此期间无需发送任何指令
  time.sleep(1)

  # 用户MCU发送一次开始信号后,DHT11从低功耗模式转换到高速模式,等待主机开始信号结束后,DHT11发送响应信号,送出40bit的数据,并触发一次信号采集,用户可选择读取部分数据.从模式下,DHT11接收到开始信号触发一次温湿度采集,如果没有接收到主机发送开始信号,DHT11不会主动进行温湿度采集.采集数据后转换到低速模式。
  GPIO.setup(CHANNEL, GPIO.OUT)

  # 总线空闲状态为高电平,主机把总线拉低等待DHT11响应,
  # 主机把总线拉低必须大于18毫秒,保证DHT11能检测到起始信号。
  GPIO.output(CHANNEL, GPIO.LOW)
  time.sleep(0.02)
  # 给一个高电平，启动温度测量
  GPIO.output(CHANNEL, GPIO.HIGH)

  GPIO.setup(CHANNEL, GPIO.IN)
  while GPIO.input(CHANNEL) == GPIO.LOW:
    continue
  while GPIO.input(CHANNEL) == GPIO.HIGH:
    continue

  '''
  一次完整的数据传输为40bit，高位先出。 
  数据格式:
    8bit湿度整数数据 +
    8bit湿度小数数据 +
    8bi温度整数数据 +
    8bit温度小数数据 +
    8bit校验和
  '''
  j = 0
  data = []
  for j in range(0, 40):
    k = 0
    while GPIO.input(CHANNEL) == GPIO.LOW:
      continue
    while GPIO.input(CHANNEL) == GPIO.HIGH:
      # 每接收到一个高电压，计数器 +1
      k += 1
      # 持续高电压，表示当前字节信号传输完毕
      # 跳出计数，进入下一次信号接收等待中
      if k > 100:
        break

    # 不清楚这个地方数据转换为什么是以 8 为分界
    if k < 8:
      data.append(0)
    else:
      data.append(1)

  GPIO.cleanup()
  print 'Bit data: %s'%(data)

  # 数据组装
  values = []
  for i in range(0, 5):
    values.append(int(bin2dec(''.join(str(i) for i in data[i*8:(i+1)*8]))))

  # 数据有效性检查
  if values[4] == sum(values[0:3]):
    return {
      'success': True,
      'data': values
    }
  else:
    return {
      'success': False
    }


success = False
tried_times = 0


start_time = time.time()
# 启动程序，并在获取数据失败时重试
while not success and tried_times < MAX_TIMES:
  returnValues = get_data()
  success = returnValues['success']
  tried_times += 1
  time.sleep(0.5)

print 'Tried times: %d'%(tried_times)
print 'Use time: %d(s)'%(time.time() - start_time)

if success:
  v = returnValues['data']
  print 'Temperature: %d°C, Humidity: %d%%'%(v[2], v[0])
else:
  print 'Fail'
