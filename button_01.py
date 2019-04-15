import RPi.GPIO as gp
import time


"""
3.3v + > ---------------------- 10k ohm
                                    |
                                    |
                                    |
                          button ---
                            |
RXD(in)(0v) -----------------

GPIO24 + > ---------------------- 220 ohm
                                    |
                                    |
                                    |
GND(0v) -------------------- -  led +
"""

gp.setmode(gp.BOARD)
gp.setup(10, gp.IN, pull_up_down=gp.PUD_DOWN)
gp.setup(18, gp.OUT)

def pushed(channel):
  while(gp.input(channel) == 1):
    gp.output(18, 1)
  if(gp.input(channel) == 0):
    gp.output(18, 0)

gp.add_event_detect(10, gp.RISING, callback=pushed, bouncetime = 100)

message = input("Press the button: \n")


gp.cleanup()
