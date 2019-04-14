import RPi.GPIO as gp
import time


sleep_time = 0.2
count = 5

gp.setmode(gp.BCM)

gp.setup(18, gp.OUT)
gp.setup(23, gp.OUT)
gp.setup(24, gp.OUT)

def light():
  gp.output(18, gp.HIGH)
  time.sleep(sleep_time)
  gp.output(18, gp.LOW)

  time.sleep(sleep_time)

  gp.output(23, gp.HIGH)
  time.sleep(sleep_time)
  gp.output(23, gp.LOW)

  time.sleep(sleep_time)

  gp.output(24, gp.HIGH)
  time.sleep(sleep_time)
  gp.output(24, gp.LOW)

  time.sleep(sleep_time)
  return;

while(count >= 0):
  light()
  count -= 1


gp.cleanup()
