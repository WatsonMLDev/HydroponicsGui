import time
from machine import Pin
import machine
from rusb import USB
from _thread import start_new_thread

water_sensor_storage = Pin(0,Pin.IN)
water_sensor_bin_1 = Pin(1,Pin.IN)
water_sensor_bin_2 = Pin(2,Pin.IN)
pump = Pin(3,Pin.OUT)
air_stone = Pin(4,Pin.OUT)
temp_sensor_bin_1 = Pin(5,Pin.IN)
temp_sensor_bin_2 = Pin(6,Pin.IN)
solenoid_bin_1 = Pin(7,Pin.OUT)
solenoid_bin_2 = Pin(8,Pin.OUT)
solenoid_pump = Pin(9,Pin.OUT)
solenoid_exit = Pin(10,Pin.OUT)
nutrient_pump_1_bin_1 = Pin(11,Pin.OUT)
nutrient_pump_2_bin_1 = Pin(12,Pin.OUT)
nutrient_pump_3_bin_1 = Pin(13,Pin.OUT)
nutrient_pump_4_bin_1 = Pin(14,Pin.OUT)
nutrient_pump_5_bin_1 = Pin(15,Pin.OUT)
nutrient_pump_6_bin_1 = Pin(16,Pin.OUT)
nutrient_pump_7_bin_1 = Pin(17,Pin.OUT)
nutrient_pump_8_bin_1 = Pin(18,Pin.OUT)
nutrient_pump_1_bin_2 = Pin(19,Pin.OUT)
nutrient_pump_2_bin_2 = Pin(20,Pin.OUT)
nutrient_pump_3_bin_2 = Pin(21,Pin.OUT)
nutrient_pump_4_bin_2 = Pin(22,Pin.OUT)
nutrient_pump_5_bin_2 = Pin(23,Pin.OUT)
nutrient_pump_6_bin_2 = Pin(24,Pin.OUT)
nutrient_pump_7_bin_2 = Pin(25,Pin.OUT)
nutrient_pump_8_bin_2 = Pin(26,Pin.OUT)

usb = USB()
input_msg = None
bufferSTDINthread = start_new_thread(usb.bufferSTDIN, ())
while True:
    input_msg = usb.getLineBuffer()

    if input_msg == "openSol1":
        solenoid_pump.on()
    if input_msg == "closeSol1":
        solenoid_pump.off()
    if input_msg == "openSol2":
        solenoid_bin_1.on()
    if input_msg == "closeSol2":
        solenoid_bin_1.off()
    if input_msg == "openSol3":
        solenoid_bin_2.on()
    if input_msg == "closeSol3":
        solenoid_bin_2.off()
    if input_msg == "openSol4":
        solenoid_exit.on()
    if input_msg == "closeSol4":
        solenoid_exit.off()
    if input_msg == "startPump":
        pump.on()

    if water_sensor_bin_1.value() == 0:
        print("waterLevelHitBin1")
    if water_sensor_bin_2.value() == 0:
        print("waterLevelHitBin2")
    if water_sensor_storage.value() == 1:
        print("waterLevelStorageLow")





