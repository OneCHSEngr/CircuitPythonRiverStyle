## Sahana Gupta 
## CircuitPython Motor Control
## Sahana Gupta 

import time
from time import sleep
import board
import simpleio
from analogio import AnalogIn 
import pwmio  

analog_in = AnalogIn(board.A0) #potentionmeter pin
pin_out = pwmio.PWMOut(board.D5)

while True:

  sensor_value = analog_in.value
  
  pin_out.duty_cycle =  sensor_value
  print("mapped sensor value: ", sensor_value)
  time.sleep(0.1)