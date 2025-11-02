from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import json
def saveCookie(driver,filename='cookie.json'):
    cookies = driver.get_cookies()
    with open(filename, 'w') as f:
        json.dump(cookies, f)
def loadCookie(driver,filename='cookie.json'):
    with open(filename, 'r') as f:
        cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
def cookieExists(filename='cookie.json'):
    return os.path.exists(filename)
if __name__ == '__main__':
    wd=webdriver.Edge()
    wd.get('https://www.miyoushe.com/ys/')
    loadCookie(wd)
    input('请登录并输入任意字符以继续...')

    # input('请登录并输入任意字符以继续...')
    # saveCookie(wd)
    # input('登录成功，请按任意键退出...')
    # wd.quit()