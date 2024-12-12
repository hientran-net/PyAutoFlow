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


# mảng lưu trữ các số giây chờ của chương trình
list1 = [5, 6, 7]

# #Đăng nhập
driver = uc.Chrome()

try:
    driver.get('https://control.sparkedhost.us/auth/login')
except Exception as ex:
    print(f"Mở url thất bại - {ex}")


#Đọc File

#Lấy thong tin email
EMAIL_FILE = "emails.txt"
try:
    with open(EMAIL_FILE, 'r') as f:
        lines = f.readlines()
    email =  lines[-1] if lines else None 

    print(f"email: {email}")
except Exception as ex:
    print(f"Đọc file không thành công - {ex}")
#Lấy thông tin password
PASSWORD_FILE = "password.txt"
passwords = []
with open(PASSWORD_FILE, 'r') as f:
    for line in f:
        password = line.split()[0]
        passwords.append(password)



    

#Điền thông tin đăng nhập
try:
    # enter_email = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[1]/input')
    # enter_email.send_keys(email)
    # time.sleep(random.choice(list1))

    # enter_password = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/input')
    # for value in passwords:
    #     enter_password.send_keys(password)
    # time.sleep(random.choice(list1))

    pressLogin = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[4]/button')
    pressLogin.click()
    time.sleep(random.choice(list1))
except Exception as ex:
    print(f"Điền thông tin thất bại: {ex}")

time.sleep(1000000)