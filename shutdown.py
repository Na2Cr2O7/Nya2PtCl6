import os
import time
from datetime import datetime
import psutil
import shutil
import csv
def writeCSV(data:list,heading=None):
    now=datetime.now()
    data=[now.strftime("%Y-%m-%d %H:%M:%S")]+data
    if heading:
        data=['Time']+heading+data
    def backup():
        shutil.copyfile('sysstat.csv','sysstat.csv.bak')
    try:
        backup()
    except FileNotFoundError:
        pass
        with open('sysstat.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data)
    except PermissionError:
        print("Permission denied, please close the csv file and try again.")
    except FileNotFoundError:
        pass
def getBatteryStatus():
    battery = psutil.sensors_battery()
    
    if battery:
        percent=battery.percent
        plugged=battery.power_plugged
        return percent, plugged
    return None, None
def getCPUStatus():
    cpu_percent = psutil.cpu_percent(interval=0.1)
    return cpu_percent
def getMemoryStatus():
    memory_percent = psutil.virtual_memory().percent
    return memory_percent
numberString=[r''' 
 ________     
|\   __  \    
\ \  \|\  \   
 \ \  \\\  \  
  \ \  \\\  \ 
   \ \_______\
    \|_______|
              ''',r'''  
  _____     
 / __  \    
|\/_|\  \   
\|/ \ \  \  
     \ \  \ 
      \ \__\
       \|__| 
''',r'''  
  _______     
 /  ___  \    
/__/|_/  /|   
|__|//  / /   
    /  /_/__  
   |\________\
    \|_______|
''',r'''
 ________     
|\_____  \    
\|____|\ /_   
      \|\  \  
     __\_\  \ 
    |\_______\
    \|_______|
              ''',r'''
 ___   ___     
|\  \ |\  \    
\ \  \\_\  \   
 \ \______  \  
  \|_____|\  \ 
         \ \__\
          \|__|
               ''',r''' 
 ________      
|\   ____\     
\ \  \___|_    
 \ \_____  \   
    _____\  \ 
   |\________\
   \|________|
''',r'''
 ________     
|\   ____\    
\ \  \___|    
 \ \  \____   
  \ \  ___  \ 
   \ \_______\
    \|_______|
    ''',r'''
 ________     
|\  ___  \    
 \|___/  /|
     /  / /
    /  / / 
   /__/ /  
   |__|/   
           ''',r''' 
________     
|\   __  \    
\ \  \|\  \   
 \ \   __  \  
  \ \  \|\  \ 
   \ \_______\
    \|_______|
    ''',r''' 
________     
|\  ___  \    
\ \____   \   
 \|____|\  \    
     __\_\  \ 
    |\_______\
    \|_______|
              ''']
splitStr=r'''        
 ___    
|\__\   
\|__|   
    ___ 
   |\__\
   \|__|
        
        '''
def print4numbers(h1, h2, m1, m2):
    # 获取每个数字对应的艺术字
    digit_h1 = numberString[h1].split('\n')
    digit_h2 = numberString[h2].split('\n')
    digit_m1 = numberString[m1].split('\n')
    digit_m2 = numberString[m2].split('\n')
    splitLst=splitStr.split('\n')
    # 横向打印艺术字
    for i in range(9):  # 跳过第一个空行
        
        print(digit_h1[i] + ' ' + digit_h2[i] + ' '+' '+ splitLst[i] +' '+ digit_m1[i] + ' ' + digit_m2[i])

def should_shutdown():
    now = datetime.now()
    return now.hour >= 22 and now.minute >= 30
def shutdownCommand():
    os.system("shutdown /a")
    os.system("shutdown /s /t 3")
def drawProcessBar(percent,length=20,end='\n'):
    bar_length = length
    filled_length = int(bar_length * percent // 100)
    bar = '0' * filled_length + ' ' * (bar_length - filled_length)
    print('['+bar+']',end=end)
def main():
    os.system("cls")
    while True:
        percent , plugged = getBatteryStatus()
        if plugged:
            print('⚡',end='')
        
        if percent:
            print(f'🔋 {percent}%',end='\t')
            drawProcessBar(percent,70)
        if not plugged and plugged!= None:
            shutdownCommand()
        CPUStat=getCPUStatus()
        cpuFreq=psutil.cpu_freq()
        print(f'CPU {CPUStat}%',end='\t')
        drawProcessBar(CPUStat,70,end='')
        print(f' {cpuFreq.current/1000:.2f}GHz')
        MemoryStat=getMemoryStatus()
        
        print(f'RAM {MemoryStat}%',end='\t')
        drawProcessBar(MemoryStat,70)
        dskusage=psutil.disk_usage('C:')
        print(f'硬盘 {dskusage.percent}%',end='\t')
        drawProcessBar(dskusage.percent,70)
        writeCSV([CPUStat,MemoryStat,cpuFreq.current/1000,dskusage.percent])

        now = datetime.now()
        h1=now.hour//10
        h2=now.hour%10
        m1=now.minute//10
        m2=now.minute%10
        print4numbers(h1, h2, m1, m2)
        if should_shutdown():
            shutdownCommand()
        time.sleep(10)
        os.system("cls")
        


if __name__ == "__main__":
    main()
