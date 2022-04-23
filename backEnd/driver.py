'''import time
from machine import Pin
import machine
import uasyncio as asyncio
import sys
sys.path.append('/WaterPumps')
from WaterPumps.flowMeters import flowMeter,flowRunData
import micropython
import gc
#-------------------------------------------------------------------------------------------------------------------------------------
# pins to controll each hardware device and defines if the pins are taking in or letting out signals

pump = Pin(0,Pin.OUT)
sol = Pin(1,Pin.OUT)
water = Pin(2,Pin.IN)
nut = Pin(3,Pin.OUT)
hall_sensor_flow = Pin(4,Pin.OUT)
hall_sensor_data = Pin(5,Pin.IN)
try:
    # timings and other stuff:
    how_many_nutrients = 5 # in mL
    time_for_nut_pump = how_many_nutrients # peristaltic pump dispenses 1 ml per second

    floodTime = 5 * 60 # 5 minutes (in seconds), time water stays on roots of plantsbefore draining
    floodWait =  3 * 60 * 60 # 3 Hours (in seconds), time between floods
    interval = 12 * 60 * 60 # 12 hours (in seconds), time between acvtive and inactive periods
    active_period = "yes" # to give the plant water or not
    there_is_power = True # to make the program allways run
    water_drain_time = 14 # seconds for the water to drain from the tank (maybe improve with another sensor?)

    mainFlowMeter = flowMeter(flowPin=5, rate=4.8) # to set up the hall efect flow sensor
    mainFlowData = flowRunData() # to do calculations on our data
    global flowCount # to make sure this variable can be accessed everythwere
    flowCount = 0 # initializing the pulses

    # turns off pumps and solinoid just to be safe
    pump.off()
    sol.off()

    # turns on and off nutrient pump for predefined amount of time
    nut.on()
    time.sleep(time_for_nut_pump)
    nut.off()

    time_last_checked = time.time() # time that the program started

    #--------------------------------------------------------------------------------------------------------------------------------------

    def callbackflow(p): # function to count how many times the hall effect flow sensor rotates completly
        global flowCount
        flowCount += 1 # raises the counter by one when this is ran

    #initialize flow sensor to calculate data
    mainFlowMeter.counterPin.irq(trigger=mainFlowMeter.counterPin.IRQ_RISING, handler=callbackflow) # when there is an interupt, run callbackflow
    main_loop = asyncio.get_event_loop()

    #--------------------------------------------------------------------------------------------------------------------------------------
    def addWater():
        # keeps filling the planet container
        try: # try to do this, but stop if there is an error
            global flowCount

            main_loop.create_task(mainFlowMeter.monitorFlowMeter()) # starts data collection on water flow

            #start pumping in water inot plant reservoir
            pump.on()
            sol.on()
            hall_sensor_flow.on()

            flow_time_start = time.time() #counting how long each fill takes


            while water.value() == 1: #keep looping this code untill water hits the water sensor
                #keep the pump on,the solenoid valve open, and the hall sensor reading data
                pass

            print("{} PIT".format(time.time()-flow_time_start)) #print the time it took to pump in water

            #calculating and sending flowrate per minute
            AFR = (450/time.time()-flow_time_start)/60
            print("{} AFR".format(AFR))

            main_loop.close() # stops reading from hall sensor
            mainFlowData.totalCount = flowCount # sets the total pulse count in a python class (for data analysis)

            print("{} GIT".format(mainFlowData.totalFlow())) # prints how many liters filled the tank
            #sys.stdout.write("%.3f Liters in tank\n" % mainFlowData.totalFlow())

            flowCount = 0 # resets back to 0 so we can get accurate measurements for every time the pump is on

            #turn the pump off and close the solenoid valve
            sol.off()
            pump.off()
            hall_sensor_flow.off()

            water_on_sensor_start = time.time()

            time.sleep(floodTime) #keeps roots wet for the time we defined earlier

            sol.on() #opens the solenoid valve to drain the water

            timer_start = time.time()
            while water.value() == 0: #if it over flows, keep draining
                sol.on()
                timer_end = time.time()
                if timer_end-timer_start >= 10: # error occured, drain for 4 minutes to return to normal flow
                    time.sleep(360)

            time.sleep(water_drain_time) # wait predefined amount of seconds for the water to completly drain (might need trial and error)

            #calculating and sending flowrate per minute
            AFR = (450/time.time()-water_on_sensor_start)/60
            print("{} AFR".format(AFR))

            print("{} WST".format(time.time()-water_on_sensor_start))

            sol.off() # close solenoid valve to stop draining

            time.sleep(floodWait) # waits for a certain amount of time till this code might run again

            gc.collect() #free up memory

        except: # if something does break, catch the error and turn everything off
            pump.off()
            nut.off()
            hall_sensor_flow.off()

            print("big error occured")

            # keeps the valve open to drain
            while water.value() == 0:
                sol.on()

            time.sleep(120) # wait predefined amount of seconds for the water to completly drain (might need trial and error)

            sol.off() # close solenoid valve to stop draining

    #--------------------------------------------------------------------------------------------------------------------------------------
    # always loop this code over and over again
    while there_is_power:
        time.sleep(1)
        current_time = time.time() # get current timer

        if active_period == "yes": # whether or not we are giving the plant water for 12 hours (day-night cycle)

            #--------------------------------------------------------------------------------------------
            if current_time - time_last_checked >= interval: # Stops the water cycling for 12 hours if its been running for 12 hours
                active_period = "no"
                time_last_checked = current_time # resets the time we are counting to

            else: #if it hasnt been 12 hours yet....
                addWater() # starts water cycle that goes every 3 hours (or whatever you change it to)
            #--------------------------------------------------------------------------------------------

        else:

            #--------------------------------------------------------------------------------------------
            if current_time - time_last_checked >= interval: # Stops the water cycling for 12 hours if its been running for 12 hours

                machine.reset() # resets the pico to start over again

            else: #if it hasnt been 12 hours yet....

                gc.collect() #do nothing and free up memory!!!!


except: # if something does break, catch the error and turn everything off
    pump.off()
    nut.off()
    hall_sensor_flow.off()

    print("big error occured")

    # keeps the valve open to drain
    while water.value() == 0:
        sol.on()

    time.sleep(120) # wait predefined amount of seconds for the water to completly drain (might need trial and error)

    sol.off() # close solenoid valve to stop draining
'''

import time
import datetime
import json
import serial
import multiprocessing
from ctypes import c_char_p, c_bool

# ser_barcode = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# ser_barcode_sensors = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# "1900-01-01 12:00:00.00"

def stop(kill_event):
    kill_event.value = True

    with open("./backEnd/system.json", "w") as f:
        json.dump({}, f)

def water_cycle_bin_1(success):

    #region loading variables from system.json and setting them
    with open('./backEnd/system.json', 'r') as f:
        json_temp = json.load(f)
    bin1Nutrient1 = json_temp["bin1Nutrient1"]
    bin1Nutrient1Amount = json_temp["binNutrient1Amount"]
    bin1Nutrient2 = json_temp["bin1Nutrient2"]
    bin1Nutrient2Amount = json_temp["binNutrient2Amount"]
    bin1Nutrient3 = json_temp["bin1Nutrient3"]
    bin1Nutrient3Amount = json_temp["binNutrient3Amount"]
    bin1Nutrient4 = json_temp["bin1Nutrient4"]
    bin1Nutrient4Amount = json_temp["binNutrient4Amount"]
    bin1Nutrient5 = json_temp["bin1Nutrient5"]
    bin1Nutrient5Amount = json_temp["binNutrient5Amount"]
    bin1Nutrient6 = json_temp["bin1Nutrient6"]
    bin1Nutrient6Amount = json_temp["binNutrient6Amount"]
    bin1Nutrient7 = json_temp["bin1Nutrient7"]
    bin1Nutrient7Amount = json_temp["binNutrient7Amount"]
    bin1Nutrient8 = json_temp["bin1Nutrient8"]
    bin1Nutrient8Amount = json_temp["binNutrient8Amount"]
    bin1lights = json_temp["bin1lights"]
    #endregion

    ser_barcode.write("openSol1")
    ser_barcode.write("openSol2")
    time.sleep(.25)
    ser_barcode.write("startPump")

    while True:
        response = ser_barcode_sensors.readline().decode("UTF-8")
        if response == "waterLevelHitBin1":
            ser_barcode.write("closeSol2")
            ser_barcode.write("stopPump")
            break

    ser_barcode.write("closeSol1")

    # region if statements for each individual setting
    if bin1Nutrient1 == True:
        ser_barcode.write("dispense1Nutrient1")
        time.sleep(bin1Nutrient1Amount)
        ser_barcode.write("stop1Nutrient1")

    if bin1Nutrient2 == True:
        ser_barcode.write("dispense1Nutrient2")
        time.sleep(bin1Nutrient2Amount)
        ser_barcode.write("stop1Nutrient2")


    if bin1Nutrient3 == True:
        ser_barcode.write("dispense1Nutrient3")
        time.sleep(bin1Nutrient3Amount)
        ser_barcode.write("stop1Nutrient3")


    if bin1Nutrient4 == True:
        ser_barcode.write("dispense1Nutrient4")
        time.sleep(bin1Nutrient4Amount)
        ser_barcode.write("stop1Nutrient4")


    if bin1Nutrient5 == True:
        ser_barcode.write("dispense1Nutrient5")
        time.sleep(bin1Nutrient5Amount)
        ser_barcode.write("stop1Nutrient5")


    if bin1Nutrient6 == True:
        ser_barcode.write("dispense1Nutrient6")
        time.sleep(bin1Nutrient6Amount)
        ser_barcode.write("stop1Nutrient6")


    if bin1Nutrient7 == True:
        ser_barcode.write("dispense1Nutrient7")
        time.sleep(bin1Nutrient7Amount)
        ser_barcode.write("stop1Nutrient7")


    if bin1Nutrient8 == True:
        ser_barcode.write("dispense1Nutrient8")
        time.sleep(bin1Nutrient8Amount)
        ser_barcode.write("stop1Nutrient8")


    if bin1lights == True:
        ser_barcode.write("turnOnLight1")


    #endregion

    ser_barcode.write("startAirstone")
    while True:
        response = ser_barcode.readline().decode("UTF-8")
        if response == "success":
            break

    success.value = True

def water_cycle_bin_2(success):

    #region loading variables from system.json and setting them
    with open('./backEnd/system.json', 'r') as f:
        json_temp = json.load(f)

    bin2Nutrient1 = json_temp["bin2Nutrient1"]
    bin2Nutrient1Amount = json_temp["binNutrient1Amount"]
    bin2Nutrient2 = json_temp["bin2Nutrient2"]
    bin2Nutrient2Amount = json_temp["binNutrient2Amount"]
    bin2Nutrient3 = json_temp["bin2Nutrient3"]
    bin2Nutrient3Amount = json_temp["binNutrient3Amount"]
    bin2Nutrient4 = json_temp["bin2Nutrient4"]
    bin2Nutrient4Amount = json_temp["binNutrient4Amount"]
    bin2Nutrient5 = json_temp["bin2Nutrient5"]
    bin2Nutrient5Amount = json_temp["binNutrient5Amount"]
    bin2Nutrient6 = json_temp["bin2Nutrient6"]
    bin2Nutrient6Amount = json_temp["binNutrient6Amount"]
    bin2Nutrient7 = json_temp["bin2Nutrient7"]
    bin2Nutrient7Amount = json_temp["binNutrient7Amount"]
    bin2Nutrient8 = json_temp["bin2Nutrient8"]
    bin2Nutrient8Amount = json_temp["binNutrient8Amount"]
    bin2lights = json_temp["bin2lights"]
    #endregion

    ser_barcode.write("openSol1")
    ser_barcode.write("openSol3")
    time.sleep(.25)
    ser_barcode.write("startPump")

    while True:
        response = ser_barcode_sensors.readline().decode("UTF-8")
        if response == "waterLevelHitBin2":
            ser_barcode.write("closeSol3")
            ser_barcode.write("stopPump")
            break

    ser_barcode.write("closeSol1")

    # region if statements for each individual setting

    if bin2Nutrient1 == True:
        ser_barcode.write("dispense2Nutrient1")
        time.sleep(bin2Nutrient1Amount)
        ser_barcode.write("stop2Nutrient1")


    if bin2Nutrient2 == True:
        ser_barcode.write("dispense2Nutrient2")
        time.sleep(bin2Nutrient2Amount)
        ser_barcode.write("stop2Nutrient2")


    if bin2Nutrient3 == True:
        ser_barcode.write("dispense2Nutrient3")
        time.sleep(bin2Nutrient3Amount)
        ser_barcode.write("stop2Nutrient3")


    if bin2Nutrient4 == True:
        ser_barcode.write("dispense2Nutrient4")
        time.sleep(bin2Nutrient4Amount)
        ser_barcode.write("stop2Nutrient4")


    if bin2Nutrient5 == True:
        ser_barcode.write("dispense2Nutrient5")
        time.sleep(bin2Nutrient5Amount)
        ser_barcode.write("stop2Nutrient5")


    if bin2Nutrient6 == True:
        ser_barcode.write("dispense2Nutrient6")
        time.sleep(bin2Nutrient6Amount)
        ser_barcode.write("stop2Nutrient6")


    if bin2Nutrient7 == True:
        ser_barcode.write("dispense2Nutrient7")
        time.sleep(bin2Nutrient7Amount)
        ser_barcode.write("stop2Nutrient7")


    if bin2Nutrient8 == True:
        ser_barcode.write("dispense2Nutrient8")
        time.sleep(bin2Nutrient8Amount)
        ser_barcode.write("stop2Nutrient8")


    if bin2lights == True:
        ser_barcode.write("turnOnLight2")

    #endregion

    ser_barcode.write("startAirstone")
    while True:
        response = ser_barcode.readline().decode("UTF-8")
        if response == "success":
            break

    success.value = True

#opens sol2 and sol3, and opens sol4
def drain_cycle(success):
    ser_barcode.write("openSol2")
    ser_barcode.write("openSol3")
    ser_barcode.write("openSol4")
    ser_barcode.write("drainWait")
    time.sleep(60)
    ser_barcode.write("closeSol2")
    ser_barcode.write("closeSol3")
    ser_barcode.write("closeSol4")


def main(kill_event):
    with open('./backEnd/config.json', 'r') as json_file:
        config = json.load(json_file)

    # always loop this code over and over again
    while True:
        if kill_event.value:
            break

        time.sleep(1)
        current_time = datetime.datetime.now()  # get current timer

        with open('./backEnd/system.json', 'r') as f:
            json_temp = json.load(f)

        if json_temp != "{}":
            time_water_cycle_Bin_1 = int(json_temp["timeWaterCycleBin1"])
            time_start_Bin_1 = int(json_temp["timeStartBin1"])
            time_stop_Bin_1 = int(json_temp["timeStopBin1"])
            time_water_cycle_Bin_2 = int(json_temp["timeWaterCycleBin2"])
            time_start_Bin_2 = int(json_temp["timeStartBin2"])
            time_stop_Bin_2 = int(json_temp["timeStopBin2"])
        else:
            time_water_cycle_Bin_1 = -1
            time_start_Bin_1 = -1
            time_stop_Bin_1 = -1
            time_water_cycle_Bin_2 = -1
            time_start_Bin_2 = -1
            time_stop_Bin_2 = -1

        success_water_cycle_bin_1 = multiprocessing.Manager().Value(c_bool, False)
        success_drain_cycle_bin_1 = multiprocessing.Manager().Value(c_bool, False)

        success_water_cycle_bin_2 = multiprocessing.Manager().Value(c_bool, False)
        success_drain_cycle_bin_2 = multiprocessing.Manager().Value(c_bool, False)

        if time_start_Bin_1 <= current_time.hour < time_stop_Bin_1:

            last_water_cycle = datetime.datetime.strptime(config["lastWaterCycleBin1"], "%Y-%m-%d %H:%M:%S.%f")
            if (last_water_cycle + datetime.timedelta(seconds=time_water_cycle_Bin_1)) < current_time:
                multiprocessing.Process(target=water_cycle_bin_1, args=(success_water_cycle_bin_1,)).start()
                config["lastWaterCycleBin1"] = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

        if time_start_Bin_2 < current_time.hour < time_stop_Bin_2:

            last_water_cycle = datetime.datetime.strptime(config["lastWaterCycleBin2"], "%Y-%m-%d %H:%M:%S.%f")
            if (last_water_cycle + datetime.timedelta(seconds=time_water_cycle_Bin_2)) < current_time:

                multiprocessing.Process(target=water_cycle_bin_2, args=(success_water_cycle_bin_2,)).start()
                config["lastWaterCycleBin2"] = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

        if success_water_cycle_bin_1.value == True:
            success_water_cycle_bin_1.value = False
            multiprocessing.Process(target=drain_cycle, args=(success_drain_cycle_bin_1,)).start()
        if success_water_cycle_bin_2.value == True:
            success_water_cycle_bin_2.value = False
            multiprocessing.Process(target=drain_cycle, args=(success_drain_cycle_bin_2,)).start()

        with open('./backEnd/system.json', 'w') as f:
            json.dump(json_temp, f)
        with open('./backEnd/config.json', 'w') as f:
            json.dump(config, f)
