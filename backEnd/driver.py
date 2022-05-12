import time
import datetime
import json
import serial
import multiprocessing
from ctypes import c_char_p, c_bool
import ast

global ser_barcode, ser_barcode_sensors
ser_barcode = serial.Serial('/dev/ttyACM0', 9600)
ser_barcode_sensors = serial.Serial('/dev/ttyACM1', 9600)

# "1900-01-01 12:00:00.00"

def sensors(sensor_data):
    global ser_barcode_sensors
    while True:
        time.sleep(.5)
        ser_barcode_sensors.close()
        ser_barcode_sensors.open()
        sensor_data.value = ser_barcode_sensors.readline().decode("UTF-8")


def ml_to_seconds(ml):
    return int(ml) / 1.6666666666666666666666666666667


def prime_pumps():
    global ser_barcode
    priming_time = 2
    
   
    ser_barcode.write("dispense1Nutrient1".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop1Nutrient1".encode("UTF-8"))

    ser_barcode.write("dispense1Nutrient2".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop1Nutrient2".encode("UTF-8"))

    ser_barcode.write("dispense1Nutrient3".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop1Nutrient3".encode("UTF-8"))

    ser_barcode.write("dispense1Nutrient4".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop1Nutrient4".encode("UTF-8"))

    ser_barcode.write("dispense1Nutrient5".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop1Nutrient5".encode("UTF-8"))

    ser_barcode.write("dispense1Nutrient6".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop1Nutrient6".encode("UTF-8"))

    ser_barcode.write("dispense1Nutrient7".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop1Nutrient7".encode("UTF-8"))

    ser_barcode.write("dispense1Nutrient8".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop1Nutrient8".encode("UTF-8"))

    ser_barcode.write("dispense2Nutrient1".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop2Nutrient1".encode("UTF-8"))

    ser_barcode.write("dispense2Nutrient2".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop2Nutrient2".encode("UTF-8"))

    ser_barcode.write("dispense2Nutrient3".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop2Nutrient3".encode("UTF-8"))

    ser_barcode.write("dispense2Nutrient4".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop2Nutrient4".encode("UTF-8"))

    ser_barcode.write("dispense2Nutrient5".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop2Nutrient5".encode("UTF-8"))

    ser_barcode.write("dispense2Nutrient6".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop2Nutrient6".encode("UTF-8"))

    ser_barcode.write("dispense2Nutrient7".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop2Nutrient7".encode("UTF-8"))

    ser_barcode.write("dispense2Nutrient8".encode("UTF-8"))
    time.sleep(priming_time)
    ser_barcode.write("stop2Nutrient8".encode("UTF-8"))
    

def water_cycle_bin_1(success):
    global sensor_data
    ser_barcode_sensors.close()
    ser_barcode_sensors.open()

    # region loading variables from system.json and setting them
    global sensor_data
    
    ser_barcode_sensors.close()
    ser_barcode_sensors.open()
    with open('./backEnd/system.json', 'r') as f:
        json_temp = json.load(f)
    bin1Nutrient1 = json_temp["bin1Nutrient1"]
    bin1Nutrient1Amount = ml_to_seconds(json_temp["bin1Nutrient1Amount"])
    bin1Nutrient2 = json_temp["bin1Nutrient2"]
    bin1Nutrient2Amount = ml_to_seconds(json_temp["bin1Nutrient2Amount"])
    bin1Nutrient3 = json_temp["bin1Nutrient3"]
    bin1Nutrient3Amount = ml_to_seconds(json_temp["bin1Nutrient3Amount"])
    bin1Nutrient4 = json_temp["bin1Nutrient4"]
    bin1Nutrient4Amount = ml_to_seconds(json_temp["bin1Nutrient4Amount"])
    bin1Nutrient5 = json_temp["bin1Nutrient5"]
    bin1Nutrient5Amount = ml_to_seconds(json_temp["bin1Nutrient5Amount"])
    bin1Nutrient6 = json_temp["bin1Nutrient6"]
    bin1Nutrient6Amount = ml_to_seconds(json_temp["bin1Nutrient6Amount"])
    bin1Nutrient7 = json_temp["bin1Nutrient7"]
    bin1Nutrient7Amount = ml_to_seconds(json_temp["bin1Nutrient7Amount"])
    bin1Nutrient8 = json_temp["bin1Nutrient8"]
    bin1Nutrient8Amount = ml_to_seconds(json_temp["bin1Nutrient8Amount"])
    bin1lights = json_temp["bin1lights"]
    # endregion

    ser_barcode.write("openSol1".encode("UTF-8"))
    time.sleep(.25)
    ser_barcode.write("startPump".encode("UTF-8"))
    ser_barcode_sensors.write("flow1Start".encode("UTF-8"))

    while True:
        time.sleep(.5)
        response = (sensor_data.value).strip("\r\n")
        if response != '\r\n' and isinstance(response, str) and response != "\n" and response != "\r" and response != '':
            response = json.loads(response)
            if response["waterLevelHitBin1"] == True:
                ser_barcode.write("stopPump".encode("UTF-8"))
                ser_barcode.write("closeSol1".encode("UTF-8"))
                ser_barcode_sensors.write("flow1Stop".encode("UTF-8"))
                break

    # region if statements for each individual setting
    if bin1Nutrient1 == True:
        ser_barcode.write("dispense1Nutrient1".encode("UTF-8"))
        time.sleep(bin1Nutrient1Amount)
        ser_barcode.write("stop1Nutrient1".encode("UTF-8"))

    if bin1Nutrient2 == True:
        ser_barcode.write("dispense1Nutrient2".encode("UTF-8"))
        time.sleep(bin1Nutrient2Amount)
        ser_barcode.write("stop1Nutrient2".encode("UTF-8"))

    if bin1Nutrient3 == True:
        ser_barcode.write("dispense1Nutrient3".encode("UTF-8"))
        time.sleep(bin1Nutrient3Amount)
        ser_barcode.write("stop1Nutrient3".encode("UTF-8"))

    if bin1Nutrient4 == True:
        ser_barcode.write("dispense1Nutrient4".encode("UTF-8"))
        time.sleep(bin1Nutrient4Amount)
        ser_barcode.write("stop1Nutrient4".encode("UTF-8"))

    if bin1Nutrient5 == True:
        ser_barcode.write("dispense1Nutrient5".encode("UTF-8"))
        time.sleep(bin1Nutrient5Amount)
        ser_barcode.write("stop1Nutrient5".encode("UTF-8"))

    if bin1Nutrient6 == True:
        ser_barcode.write("dispense1Nutrient6".encode("UTF-8"))
        time.sleep(bin1Nutrient6Amount)
        ser_barcode.write("stop1Nutrient6".encode("UTF-8"))

    if bin1Nutrient7 == True:
        ser_barcode.write("dispense1Nutrient7".encode("UTF-8"))
        time.sleep(bin1Nutrient7Amount)
        ser_barcode.write("stop1Nutrient7".encode("UTF-8"))

    if bin1Nutrient8 == True:
        ser_barcode.write("dispense1Nutrient8".encode("UTF-8"))
        time.sleep(bin1Nutrient8Amount)
        ser_barcode.write("stop1Nutrient8".encode("UTF-8"))

    if bin1lights == True:
        ser_barcode.write("startLight1".encode("UTF-8"))

    # endregion

    ser_barcode.write("startAirStone".encode("UTF-8"))
    time.sleep(5)
    ser_barcode.write("stopAirStone".encode("UTF-8"))

    success.value = True


def water_cycle_bin_2(success):
    global sensor_data
    ser_barcode_sensors.close()
    ser_barcode_sensors.open()
    
    # region loading variables from system.json and setting them
    with open('./backEnd/system.json', 'r') as f:
        json_temp = json.load(f)

    bin2Nutrient1 = json_temp["bin2Nutrient1"]
    bin2Nutrient1Amount = ml_to_seconds(json_temp["bin2Nutrient1Amount"])
    bin2Nutrient2 = json_temp["bin2Nutrient2"]
    bin2Nutrient2Amount = ml_to_seconds(json_temp["bin2Nutrient2Amount"])
    bin2Nutrient3 = json_temp["bin2Nutrient3"]
    bin2Nutrient3Amount = ml_to_seconds(json_temp["bin2Nutrient3Amount"])
    bin2Nutrient4 = json_temp["bin2Nutrient4"]
    bin2Nutrient4Amount = ml_to_seconds(json_temp["bin2Nutrient4Amount"])
    bin2Nutrient5 = json_temp["bin2Nutrient5"]
    bin2Nutrient5Amount = ml_to_seconds(json_temp["bin2Nutrient5Amount"])
    bin2Nutrient6 = json_temp["bin2Nutrient6"]
    bin2Nutrient6Amount = ml_to_seconds(json_temp["bin2Nutrient6Amount"])
    bin2Nutrient7 = json_temp["bin2Nutrient7"]
    bin2Nutrient7Amount = ml_to_seconds(json_temp["bin2Nutrient7Amount"])
    bin2Nutrient8 = json_temp["bin2Nutrient8"]
    bin2Nutrient8Amount = ml_to_seconds(json_temp["bin2Nutrient8Amount"])
    bin2lights = json_temp["bin2lights"]
    # endregion

    ser_barcode.write("openSol2".encode("UTF-8"))
    time.sleep(.25)
    ser_barcode.write("startPump".encode("UTF-8"))
    ser_barcode_sensors.write("flow2Start".encode("UTF-8"))

    while True:
        time.sleep(.5)
        response = (sensor_data.value).strip("\r\n")
        if response != '\r\n' and isinstance(response, str) and response != "\n" and response != "\r" and response != '':
            response = json.loads(response)
            if response["waterLevelHitBin2"] == True:
                ser_barcode.write("stopPump".encode("UTF-8"))
                ser_barcode.write("closeSol2".encode("UTF-8"))
                ser_barcode_sensors.write("flow2Stop".encode("UTF-8"))
                break

    # region if statements for each individual setting

    if bin2Nutrient1 == True:
        ser_barcode.write("dispense2Nutrient1".encode("UTF-8"))
        time.sleep(bin2Nutrient1Amount)
        ser_barcode.write("stop2Nutrient1".encode("UTF-8"))

    if bin2Nutrient2 == True:
        ser_barcode.write("dispense2Nutrient2".encode("UTF-8"))
        time.sleep(bin2Nutrient2Amount)
        ser_barcode.write("stop2Nutrient2".encode("UTF-8"))

    if bin2Nutrient3 == True:
        ser_barcode.write("dispense2Nutrient3".encode("UTF-8"))
        time.sleep(bin2Nutrient3Amount)
        ser_barcode.write("stop2Nutrient3".encode("UTF-8"))

    if bin2Nutrient4 == True:
        ser_barcode.write("dispense2Nutrient4".encode("UTF-8"))
        time.sleep(bin2Nutrient4Amount)
        ser_barcode.write("stop2Nutrient4".encode("UTF-8"))

    if bin2Nutrient5 == True:
        ser_barcode.write("dispense2Nutrient5".encode("UTF-8"))
        time.sleep(bin2Nutrient5Amount)
        ser_barcode.write("stop2Nutrient5".encode("UTF-8"))

    if bin2Nutrient6 == True:
        ser_barcode.write("dispense2Nutrient6".encode("UTF-8"))
        time.sleep(bin2Nutrient6Amount)
        ser_barcode.write("stop2Nutrient6".encode("UTF-8"))

    if bin2Nutrient7 == True:
        ser_barcode.write("dispense2Nutrient7".encode("UTF-8"))
        time.sleep(bin2Nutrient7Amount)
        ser_barcode.write("stop2Nutrient7".encode("UTF-8"))

    if bin2Nutrient8 == True:
        ser_barcode.write("dispense2Nutrient8".encode("UTF-8"))
        time.sleep(bin2Nutrient8Amount)
        ser_barcode.write("stop2Nutrient8".encode("UTF-8"))

    if bin2lights == True:
        ser_barcode.write("turnOnLight2")

    # endregion

    ser_barcode.write("startAirStone".encode("UTF-8"))
    time.sleep(5)
    ser_barcode.write("stopAirStone".encode("UTF-8"))

    success.value = True


def wait_cycle_bin_1(success):
    time.sleep(1 * 60)
    success.value = True


def wait_cycle_bin_2(success):
    time.sleep(1 * 60)
    success.value = True


def drain_cycle_bin_1(success):
    ser_barcode.write("openSol1".encode("UTF-8"))


def drain_cycle_bin_2(success):
    ser_barcode.write("openSol2".encode("UTF-8"))


def stop(kill_event):
    kill_event.value = True
    
    ser_barcode.write("stopAll".encode("UTF-8"))

    with open("./backEnd/system.json", "w") as f:
        json.dump({}, f)


def main(kill_event):
    with open('./backEnd/config.json', 'r') as json_file:
        config = json.load(json_file)

    success_water_cycle_bin_1 = multiprocessing.Manager().Value(c_bool, False)
    success_drain_cycle_bin_1 = multiprocessing.Manager().Value(c_bool, False)
    success_wait_cycle_bin_1 = multiprocessing.Manager().Value(c_bool, False)

    success_water_cycle_bin_2 = multiprocessing.Manager().Value(c_bool, False)
    success_drain_cycle_bin_2 = multiprocessing.Manager().Value(c_bool, False)
    success_wait_cycle_bin_2 = multiprocessing.Manager().Value(c_bool, False)

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
            run_cycle_Bin_1 = json_temp["bin1On"]
            run_cycle_Bin_2 = json_temp["bin2On"]
        else:
            time_water_cycle_Bin_1 = -1
            time_start_Bin_1 = -1
            time_stop_Bin_1 = -1
            time_water_cycle_Bin_2 = -1
            time_start_Bin_2 = -1
            time_stop_Bin_2 = -1
            run_cycle_Bin_1 = False
            run_cycle_Bin_2 = False

        if (time_start_Bin_1 <= current_time.hour < time_stop_Bin_1) and run_cycle_Bin_1:
            
            last_water_cycle = datetime.datetime.strptime(config["lastWaterCycleBin1"], "%Y-%m-%d %H:%M:%S.%f")
            if (last_water_cycle + datetime.timedelta(hours=time_water_cycle_Bin_1)) < current_time:
                multiprocessing.Process(target=water_cycle_bin_1, args=(success_water_cycle_bin_1,)).start()
                config["lastWaterCycleBin1"] = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

        if (time_start_Bin_2 < current_time.hour < time_stop_Bin_2) and run_cycle_Bin_2:
            
            last_water_cycle = datetime.datetime.strptime(config["lastWaterCycleBin2"], "%Y-%m-%d %H:%M:%S.%f")
            if (last_water_cycle + datetime.timedelta(hours=time_water_cycle_Bin_2)) < current_time:
                print("hit")
                multiprocessing.Process(target=water_cycle_bin_2, args=(success_water_cycle_bin_2,)).start()
                config["lastWaterCycleBin2"] = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")

        if success_water_cycle_bin_1.value == True:
            success_water_cycle_bin_1.value = False
            multiprocessing.Process(target=wait_cycle_bin_1, args=(success_wait_cycle_bin_1,)).start()
        if success_water_cycle_bin_2.value == True:
            success_water_cycle_bin_2.value = False
            multiprocessing.Process(target=wait_cycle_bin_2, args=(success_wait_cycle_bin_2,)).start()

        if success_wait_cycle_bin_1.value == True:
            success_wait_cycle_bin_1.value = False
            multiprocessing.Process(target=drain_cycle_bin_1, args=(success_drain_cycle_bin_1,)).start()
        if success_wait_cycle_bin_2.value == True:
            success_wait_cycle_bin_2.value = False
            multiprocessing.Process(target=drain_cycle_bin_2, args=(success_drain_cycle_bin_2,)).start()

        with open('./backEnd/system.json', 'w') as f:
            json.dump(json_temp, f)
        with open('./backEnd/config.json', 'w') as f:
            json.dump(config, f)

global sensor_data
manager = multiprocessing.Manager()
sensor_data = manager.Value(c_char_p, "")
multiprocessing.Process(target=sensors, args=(sensor_data,)).start()

