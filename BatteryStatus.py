import psutil
from datetime import datetime
def getModelChoice():
    
    if datetime.now().hour in range(21,24) or datetime.now().hour in range(0,8):
        return False
    battery = psutil.sensors_battery()
    return battery.power_plugged
def isCharged():
    battery = psutil.sensors_battery()
    return battery.power_plugged
def runTime():
    return True
    if datetime.now().hour in range(23,24) or datetime.now().hour in range(0,6):
        return False
    else:
        return True
def restTime():
    return False
    # if datetime.now().hour in range(9,13):
    #     return False
    # elif datetime.now().hour in range(15,18):
    #     return False
    if datetime.now().hour in range(17,22):
        return False
    else:
        return True