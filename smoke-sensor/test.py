import RPi.GPIO as GPIO
import time

CHANNEL = 7

def action(pin):
  print 'Sensor detected action!'

GPIO.setmode(GPIO.BOARD)

# 设置下拉电阻
GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(CHANNEL, GPIO.RISING)
GPIO.add_event_callback(CHANNEL, action)

GPIO.setup(CHANNEL, GPIO.OUT, initial=GPIO.HIGH)
time.sleep(0.02)
GPIO.output(CHANNEL, GPIO.LOW)

GPIO.cleanup()
