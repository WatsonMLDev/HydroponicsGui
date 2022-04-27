import time
from machine import Pin

water_sensor_bin_1 = Pin(0,Pin.IN)
water_sensor_bin_2 = Pin(1,Pin.IN)
temp_sensor_bin_1 = Pin(2,Pin.IN)
temp_sensor_bin_2 = Pin(3,Pin.IN)
water_sensor_storage = Pin(4,Pin.IN)
humidity_sensor_bin_1 = Pin(5,Pin.IN)
humidity_sensor_bin_2 = Pin(6,Pin.IN)
ec_sensor = Pin(7,Pin.IN)
ph_sensor = Pin(8,Pin.IN)
hall_effect_bin_1 = Pin(9,Pin.IN)
hall_effect_bin_2 = Pin(10,Pin.IN)

usb = USB()
input_msg = None
bufferSTDINthread = start_new_thread(usb.bufferSTDIN, ())



while True:
    string = ""
    if water_sensor_bin_1.value() == 0:
        string += ("waterLevelHitBin1, ")
    if water_sensor_bin_2.value() == 0:
        print("waterLevelHitBin2")
    if water_sensor_storage.value() == 1:
        print("waterLevelStorageLow")


    print(string)