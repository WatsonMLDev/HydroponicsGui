import time
from machine import Pin, ADC
import sys
import select

sys.path.append('/WaterPumps')
from WaterPumps.flowMeters import flowMeter, flowRunData
import uasyncio as asyncio
from max6675 import MAX6675

hall_effect_bin_1 = Pin(0, Pin.IN)
hall_effect_bin_2 = Pin(1, Pin.IN)
water_sensor_storage = Pin(2, Pin.IN)
water_sensor_bin_2 = Pin(3, Pin.IN)
water_sensor_bin_1 = Pin(4, Pin.IN)
temperature_sensor_bin_1 = Pin(5, Pin.IN)
cs_bin_1 = Pin(6, Pin.OUT)
sck_bin_1 = Pin(7, Pin.OUT)
temperature_sensor_bin_2 = Pin(8, Pin.IN)
cs_bin_2 = Pin(9, Pin.OUT)
sck_bin_2 = Pin(10, Pin.OUT)
tcs_sensor_bin_1 = ADC(26)
tcs_sensor_bin_2 = ADC(27)
# ec_sensor = Pin(7,Pin.IN)
# ph_sensor = Pin(8,Pin.IN)


global flowCount1, flowCount2
mainFlowMeter1 = flowMeter(flowPin=0, rate=7.5)  # to set up the hall effect flow sensor
mainFlowData1 = flowRunData()  # to do calculations on our data
flowCount1 = 0

mainFlowMeter2 = flowMeter(flowPin=1, rate=7.5)  # to set up the hall effect flow sensor
mainFlowData2 = flowRunData()  # to do calculations on our data
flowCount2 = 0

temp1 = MAX6675(sck_bin_1, cs_bin_1, temperature_sensor_bin_1)
temp2 = MAX6675(sck_bin_2, cs_bin_2, temperature_sensor_bin_2)


def callbackflow1(p):  # function to count how many times the hall effect flow sensor rotates completly
    global flowCount1
    flowCount1 += 1  # raises the counter by one when this is run


def callbackflow2(p):  # function to count how many times the hall effect flow sensor rotates completly
    global flowCount2
    flowCount2 += 1  # raises the counter by one when this is run


def read_input():
    word = ""
    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        ch = sys.stdin.read(1)
        word += ch
    return (str(word).strip())


# initialize flow sensor to calculate data
mainFlowMeter1.counterPin.irq(trigger=mainFlowMeter1.counterPin.IRQ_RISING,
                              handler=callbackflow1)  # when there is an interupt, run callbackflow
main_loop1 = asyncio.get_event_loop()

mainFlowMeter2.counterPin.irq(trigger=mainFlowMeter2.counterPin.IRQ_RISING,
                              handler=callbackflow2)  # when there is an interupt, run callbackflow
main_loop2 = asyncio.get_event_loop()

while True:
    global flowCount
    string = "{"
    if water_sensor_bin_1.value() == 1:
        string += ("'waterLevelHitBin1': True,")
    else:
        string += ("'waterLevelHitBin1': False,")

    if water_sensor_bin_2.value() == 1:
        print("waterLevelHitBin2': True,")
    else:
        string += ("'waterLevelHitBin2': False,")

    if water_sensor_storage.value() == 0:
        print("waterLevelStorageLow': True,")
    else:
        string += ("'waterLevelStorageLow': False,")

    string += ("'tcsBin1': " + str(tcs_sensor_bin_1.read_u16()) + ",")
    string += ("'tcsBin2': " + str(tcs_sensor_bin_2.read_u16()) + ",")
    string += ("'temp1': " + str(temp1.read()) + ",")
    string += ("'temp2': " + str(temp2.read()) + ",")

    command = read_input()
    flow1 = 0
    flow2 = 0
    if command == "flow1Start":
        main_loop1.create_task(mainFlowMeter1.monitorFlowMeter())  # starts data collection on water flow
    if command == "flow1Stop":
        main_loop1.close()  # stops reading from hall sensor
        mainFlowData1.totalCount = flowCount1  # sets the total pulse count in a python class (for data analysis)
    if command == "flow2Start":
        main_loop2.create_task(mainFlowMeter2.monitorFlowMeter())  # starts data collection on water flow
    if command == "flow2Stop":
        main_loop2.close()  # stops reading from hall sensor
        mainFlowData2.totalCount = flowCount2  # sets the total pulse count in a python class (for data analysis)
    string += ("'flowData1': " + str(mainFlowData1.totalFlow()) + ",")
    string += ("'flowData2': " + str(mainFlowData2.totalFlow()))
    string += ("}")

    print(string)
