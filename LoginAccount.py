import os
import time
import random
import string
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyperclip
from datetime import date, datetime

list1 = [5, 6, 7]

#Mở chrome
driver = uc.Chrome()
driver.implicitly_wait(10)



try:
    driver.get('https://control.sparkedhost.us/auth/login')    
    
    #press login via billing
    driver.implicitly_wait(10)
    pressLoginViaBilling = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[4]/button')
    pressLoginViaBilling.click()
    
    #enter email
    enterEmail = driver.find_element(By.XPATH, '//*[@id="inputEmail"]')
    enterEmail.send_keys('trannam9320@gmail.com')

    #enter password 
    enterPassword = driver.find_element(By.XPATH, '//*[@id="inputPassword"]')
    enterPassword.send_keys('o(E,rGHPyuzH')

    #press Login
    pressLogin = driver.find_element(By.XPATH, '//*[@id="btnLogin"]')
    pressLogin.click()

    

    print("Chạy thành công")
    time.sleep(10000)
    driver.quit()
except Exception as ex:
    print(f"Có lỗi: {ex}")
