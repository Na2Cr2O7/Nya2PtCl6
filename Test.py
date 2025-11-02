def containsImageinReply():
    global wd
    try:
        imageLink=wd.find_element(By.CSS_SELECTOR,'.ql-image-box > img:nth-child(1)').get_attribute('src')
    except:
        return False
    r=requests.get(imageLink,stream=True)
    FileName='ImageinReply.jpg'
    if r.status_code == 200:
        a=open(FileName,'wb')
        a.write(r.content)
        a.close()
        return FileName

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
options=webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


import ollama
from threading import Thread
from threading import _start_new_thread
from random import randint,choice
import os
import sys
import requests
import shutil
from datetime import datetime
from tqdm import *
from pynput import keyboard

import CopyTest
import Util
import BatteryStatus
from RichText import *

try:
    import RAGUtil
    import DrawUtilsII as DrawUtils
except Exception as e:
    pass
import VisionUtil
from Constant import *
from CaptchaUtil import getSimiliarity

wd=webdriver.Firefox()
login=True
def Sleep(t):
    sleep(t)
if login:
    try:
        wd.get('https://www.miyoushe.com/ys/')
        Sleep(12)
        try:
            wd.find_element(By.CSS_SELECTOR,".header__avatar > img:nth-child(1)").click()
        except Exception as e:
            wd.find_element(By.CSS_SELECTOR,".header__avatarwrp").click()
        Sleep(12)
        r=wd.find_element(By.ID,"mihoyo-login-platform-iframe")
        Sleep(12)
        wd.switch_to.frame(r)
        wd.find_element(By.CSS_SELECTOR ,'#tab-password').click()
        wd.find_element(By.CSS_SELECTOR ,'#username').send_keys(ACCOUNT)
        wd.find_element(By.CSS_SELECTOR ,'#password').send_keys(PASSWORD)
        wd.find_element(By.CSS_SELECTOR ,'.el-checkbox__inner').click()
        wd.find_element(By.CSS_SELECTOR ,'button.el-button').click()
    except Exception as e:
        pass

