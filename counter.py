import RPi.GPIO as gp
import time


gp.setmode(gp.BCM)

#Setup 13 pins
#12,16,18,22,32,36,38,40,37,35,33,31,29

gp.setup(18, gp.OUT) #1
gp.setup(23, gp.OUT) #2
gp.setup(24, gp.OUT) #3
gp.setup(25, gp.OUT) #4
gp.setup(12, gp.OUT) #5
gp.setup(16, gp.OUT) #6
gp.setup(20, gp.OUT) #7
gp.setup(21, gp.OUT) #8
gp.setup(26, gp.OUT) #13
gp.setup(19, gp.OUT) #12
gp.setup(13, gp.OUT) #11
gp.setup(6, gp.OUT)  #10
gp.setup(5, gp.OUT)  #9

list_of_pins = [18, 23, 24, 25, 12, 16, 20, 21, 26, 19, 13, 6, 5]
repeat_count = 10


def stop_pins():
  for p in list_of_pins:
    if gp.input(p) == 1:
      gp.output(p, False)

def display_number(led_list, sleep_time):
  stop_pins()
  for l in led_list:
    gp.output(l, True)

  time.sleep(sleep_time)


while repeat_count > 0:
  display_number([18, 24, 23,  25, 16, 20, 26, 21, 19, 13, 6, 5], 1)    #0
  display_number([20, 18, 23, 24, 19], 1)                               #1
  display_number([21, 16, 20, 18, 12, 13, 5, 6, 19, 23], 1)             #2
  display_number([21, 16, 20, 18, 23, 12, 5, 6, 19, 24], 1)             #3
  display_number([21, 25, 26, 12, 23, 24, 19], 1)                       #4
  display_number([21, 16, 20, 25, 12, 24, 19, 26, 6, 5], 1)             #5
  display_number([12, 25, 26, 13, 5, 12, 6, 23, 24, 19, 21], 1)         #6
  display_number([21, 16, 20, 18, 23, 24, 19], 1)                       #7
  display_number([18, 24, 25, 12, 16, 20, 21, 19, 13, 6, 5, 26, 23], 1) #8
  display_number([20, 18, 23, 24, 19, 16, 12, 21, 25, 26], 1)           #9
  repeat_count -= 1

stop_pins()
gp.cleanup()
