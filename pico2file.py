import time
from machine import Pin,ADC
sys.path.append('/WaterPumps')
from WaterPumps.flowMeters import flowMeter,flowRunData

hall_effect_bin_1 = Pin(0,Pin.IN)
hall_effect_bin_2 = Pin(1,Pin.IN)
water_sensor_storage = Pin(2,Pin.IN)
water_sensor_bin_2 = Pin(3,Pin.IN)
water_sensor_bin_1 = Pin(4,Pin.IN)
temperature_sensor_bin_1 = Pin(5, Pin.IN)
cs_bin_1 = Pin(6, Pin.OUT)
sck_bin_1= Pin(7, Pin.OUT)
temperature_sensor_bin_2 = Pin(8, Pin.IN)
cs_bin_2 = Pin(9, Pin.OUT)
sck_bin_2= Pin(10, Pin.OUT)
tcs_sensor_bin_1 = ADC(26)
tcs_sensor_bin_2 = ADC(27)
#ec_sensor = Pin(7,Pin.IN)
#ph_sensor = Pin(8,Pin.IN)


usb = USB()
input_msg = None
bufferSTDINthread = start_new_thread(usb
                                     .bufferSTDIN, ())

def callbackflow(p): # function to count how many times the hall effect flow sensor rotates completly
    global flowCount
    flowCount += 1 # raises the counter by one when this is ran

    #initialize flow sensor to calculate data
mainFlowMeter.counterPin.irq(trigger=mainFlowMeter.counterPin.IRQ_RISING, handler=callbackflow) # when there is an interupt, run callbackflow
main_loop = asyncio.get_event_loop()

while True:
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

    string+=("'tcsBin1': " + str(tcs_sensor_bin_1.read_u16()) + ",")
    string+=("'tcsBin2': " + str(tcs_sensor_bin_2.read_u16()) + ",")




    string+=("}")

    print(string)