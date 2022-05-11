import time
from machine import Pin
import machine
import select
import sys

def read_input():
    word = ""
    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        ch = sys.stdin.read(1)
        word+=ch
    return (str(word).strip())


nutrient_pump_1_bin_1 = Pin(0,Pin.OUT)
nutrient_pump_2_bin_1 = Pin(1,Pin.OUT)
nutrient_pump_3_bin_1 = Pin(2,Pin.OUT)
nutrient_pump_4_bin_1 = Pin(3,Pin.OUT)
nutrient_pump_5_bin_1 = Pin(4,Pin.OUT)
nutrient_pump_6_bin_1 = Pin(5,Pin.OUT)
nutrient_pump_7_bin_1 = Pin(6,Pin.OUT)
nutrient_pump_8_bin_1 = Pin(7,Pin.OUT)
nutrient_pump_1_bin_2 = Pin(8,Pin.OUT)
nutrient_pump_2_bin_2 = Pin(9,Pin.OUT)
nutrient_pump_3_bin_2 = Pin(10,Pin.OUT)
nutrient_pump_4_bin_2 = Pin(11,Pin.OUT)
nutrient_pump_5_bin_2 = Pin(12,Pin.OUT)
nutrient_pump_6_bin_2 = Pin(13,Pin.OUT)
nutrient_pump_7_bin_2 = Pin(14,Pin.OUT)
nutrient_pump_8_bin_2 = Pin(15,Pin.OUT)
pump = Pin(16,Pin.OUT)
solenoid_bin_1 = Pin(17,Pin.OUT)
solenoid_exit = Pin(18,Pin.OUT)
solenoid_bin_2 = Pin(19,Pin.OUT)
air_stone = Pin(21,Pin.OUT)
light_bin_1 = Pin(22,Pin.OUT)
light_bin_2 = Pin(26,Pin.OUT)


nutrient_pump_1_bin_1.value(1)
nutrient_pump_2_bin_1.value(1)
nutrient_pump_3_bin_1.value(1)
nutrient_pump_4_bin_1.value(1)
nutrient_pump_5_bin_1.value(1)
nutrient_pump_6_bin_1.value(1)
nutrient_pump_7_bin_1.value(1)
nutrient_pump_8_bin_1.value(1)
nutrient_pump_1_bin_2.value(1)
nutrient_pump_2_bin_2.value(1)
nutrient_pump_3_bin_2.value(1)
nutrient_pump_4_bin_2.value(1)
nutrient_pump_5_bin_2.value(1)
nutrient_pump_6_bin_2.value(1)
nutrient_pump_7_bin_2.value(1)
nutrient_pump_8_bin_2.value(1)
pump.value(1)
solenoid_bin_1.value(0)
solenoid_exit.value(0)
solenoid_bin_2.value(0)


input_msg = None

while True:
    time.sleep(1)
    input_msg = read_input()

    if input_msg == "openSol3":
        solenoid_exit.value(1)
    if input_msg == "closeSol3":
        solenoid_exit.value(0)
    if input_msg == "openSol1":
        solenoid_bin_1.value(1)
    if input_msg == "closeSol1":
        solenoid_bin_1.value(0)
    if input_msg == "openSol2":
        solenoid_bin_2.value(1)
    if input_msg == "closeSol2":
        solenoid_bin_2.value(0)
    if input_msg == "startPump":
        pump.value(0)
    if input_msg == "stopPump":
        pump.value(1)
    if input_msg == "startAirStone":
        air_stone.value(1)
    if input_msg == "stopAirStone":
        air_stone.value(0)
    if input_msg == "startLight1":
        light_bin_1.value(1)
    if input_msg == "stopLight1":
        light_bin_1.value(0)
    if input_msg == "startLight2":
        light_bin_2.value(1)
    if input_msg == "stopLight2":
        light_bin_2.value(0)

    if input_msg == "dispense1Nutrient1":
        nutrient_pump_1_bin_1.value(0)
    if input_msg == "stop1Nutrient1":
        nutrient_pump_1_bin_1.value(1)
    if input_msg == "dispense1Nutrient2":
        nutrient_pump_2_bin_1.value(0)
    if input_msg == "stop1Nutrient2":
        nutrient_pump_2_bin_1.value(1)
    if input_msg == "dispense1Nutrient3":
        nutrient_pump_3_bin_1.value(0)
    if input_msg == "stop1Nutrient3":
        nutrient_pump_3_bin_1.value(1)
    if input_msg == "dispense1Nutrient4":
        nutrient_pump_4_bin_1.value(0)
    if input_msg == "stop1Nutrient4":
        nutrient_pump_4_bin_1.value(1)
    if input_msg == "dispense1Nutrient5":
        nutrient_pump_5_bin_1.value(0)
    if input_msg == "stop1Nutrient5":
        nutrient_pump_5_bin_1.value(1)
    if input_msg == "dispense1Nutrient6":
        nutrient_pump_6_bin_1.value(0)
    if input_msg == "stop1Nutrient6":
        nutrient_pump_6_bin_1.value(1)
    if input_msg == "dispense1Nutrient7":
        nutrient_pump_7_bin_1.value(0)
    if input_msg == "stop1Nutrient7":
        nutrient_pump_7_bin_1.value(1)
    if input_msg == "dispense1Nutrient8":
        nutrient_pump_8_bin_1.value(0)
    if input_msg == "stop1Nutrient8":
        nutrient_pump_8_bin_1.value(1)

    if input_msg == "dispense2Nutrient1":
        nutrient_pump_1_bin_2.value(0)
    if input_msg == "stop2Nutrient1":
        nutrient_pump_1_bin_2.value(1)
    if input_msg == "dispense2Nutrient2":
        nutrient_pump_2_bin_2.value(0)
    if input_msg == "stop2Nutrient2":
        nutrient_pump_2_bin_2.value(1)
    if input_msg == "dispense2Nutrient3":
        nutrient_pump_3_bin_2.value(0)
    if input_msg == "stop2Nutrient3":
        nutrient_pump_3_bin_2.value(1)
    if input_msg == "dispense2Nutrient4":
        nutrient_pump_4_bin_2.value(0)
    if input_msg == "stop2Nutrient4":
        nutrient_pump_4_bin_2.value(1)
    if input_msg == "dispense2Nutrient5":
        nutrient_pump_5_bin_2.value(0)
    if input_msg == "stop2Nutrient5":
        nutrient_pump_5_bin_2.value(1)
    if input_msg == "dispense2Nutrient6":
        nutrient_pump_6_bin_2.value(0)
    if input_msg == "stop2Nutrient6":
        nutrient_pump_6_bin_2.value(1)
    if input_msg == "dispense2Nutrient7":
        nutrient_pump_7_bin_2.value(0)
    if input_msg == "stop2Nutrient7":
        nutrient_pump_7_bin_2.value(1)
    if input_msg == "dispense2Nutrient8":
        nutrient_pump_8_bin_2.value(0)
    if input_msg == "stop2Nutrient8":
        nutrient_pump_8_bin_2.value(1)

    if input_msg == "stopAll":
        nutrient_pump_1_bin_1.value(1)
        nutrient_pump_2_bin_1.value(1)
        nutrient_pump_3_bin_1.value(1)
        nutrient_pump_4_bin_1.value(1)
        nutrient_pump_5_bin_1.value(1)
        nutrient_pump_6_bin_1.value(1)
        nutrient_pump_7_bin_1.value(1)
        nutrient_pump_8_bin_1.value(1)
        nutrient_pump_1_bin_2.value(1)
        nutrient_pump_2_bin_2.value(1)
        nutrient_pump_3_bin_2.value(1)
        nutrient_pump_4_bin_2.value(1)
        nutrient_pump_5_bin_2.value(1)
        nutrient_pump_6_bin_2.value(1)
        nutrient_pump_7_bin_2.value(1)
        nutrient_pump_8_bin_2.value(1)
        pump.value(1)
        solenoid_bin_1.value(0)
        solenoid_exit.value(0)
        solenoid_bin_2.value(0)









