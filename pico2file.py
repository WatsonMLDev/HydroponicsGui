import time
from machine import Pin

humidity_sensor_bin_1 = Pin(1,Pin.IN)
humidity_sensor_bin_2 = Pin(2,Pin.IN)
ec_sensor = Pin(3,Pin.IN)
ph_sensor = Pin(4,Pin.IN)
hall_effect_bin_1 = Pin(5,Pin.IN)
hall_effect_bin_2 = Pin(6,Pin.IN)


