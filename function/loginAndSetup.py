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
from colorama import Fore, Back, Style, init

init()


# ============================================================================================================================================ #


#Đường dẫn file
    #Email file path:
EMAIL_FILE = "emails.txt"
    
    #Password file path:
PASSWORD_FILE = "password.txt"

    #IP ADDRESS file path:
IPADDRESS_FILE = "ipaddress.txt"


# ============================================================================================================================================ #

# ============================================================================================================================================ #


    #Các hàm bổ trợ
def read_last_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()  # Đọc tất cả dòng và loại bỏ ký tự xuống dòng
            for line in reversed(lines):
                if line.strip():  # Bỏ qua các dòng trống
                    return line.strip()
        return None  # Nếu file chỉ chứa dòng trống
    except FileNotFoundError:
        print(f"File '{file_path}' không tồn tại.")
        return None
    
def save_to_file(file_path, value):
    with open(file_path, "a") as file:
        file.write(value + "\n")


# ============================================================================================================================================ #


#Source code chính:

def login_and_setup():
    #Khởi tạo chrome:
    browser = uc.Chrome()

    #Giới hạn số lần thử lại ( default 20 times )
    browser.implicitly_wait(20)

    try:
    #Mở link:
        browser.get('https://control.sparkedhost.us/auth/login')
        print(f"{Fore.GREEN}Mở link thành công !!")
        time.sleep(6)
    #Bấm login via Billing
        pressLoginViaBilling = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[4]/button')
        pressLoginViaBilling.click()
        print(f"{Fore.GREEN}Bấm login via Billing thành công !!!")
        
        #Đọc file lưu vào biến
        temp_email = read_last_line(EMAIL_FILE)
        temp_password = read_last_line(PASSWORD_FILE)
        
        #Nhập email
        enterEmail = browser.find_element(By.XPATH, '//*[@id="inputEmail"]')
        enterEmail.send_keys(temp_email)
        print(f"{Fore.GREEN}Nhập email thành công !!!")
        print(f"{Style.RESET_ALL}Email vừa nhập: {temp_email}")

        #Nhập password
        enterPassword = browser.find_element(By.XPATH, '//*[@id="inputPassword"]')
        enterPassword.send_keys(temp_password)
        print(f"{Fore.GREEN}Nhập password thành công !!!")
        print(f"{Style.RESET_ALL}Password vừa nhập: {temp_password}")

        #Nhấn đăng nhập:
        pressLogin = browser.find_element(By.XPATH, '//*[@id="btnLogin"]')
        pressLogin.click()
        print(f"{Fore.GREEN}Nhấn đăng nhập thành công !!!")

        # #Nhấn authorise
        # pressAuthorise = browser.find_element(By.XPATH, '//*[@id="userAuthorizationAccepted"]')
        # pressAuthorise.click()
        # print(f"{Fore.GREEN}Nhấn authorise thành công !!!")

    #Setup
        #Nhấn chọn vào server
        pressServer = browser.find_element(By.XPATH, '//*[@id="list"]/div/div/div/div[2]')
        pressServer.click()

        #Copy ip mới và lưu vào file
        ipElement = browser.find_element(By.CSS_SELECTOR, "p.text-sm.cursor-pointer")
        ipAddress = ipElement.text
        print(f"{Style.RESET_ALL}Địa chỉ ip mới: {ipAddress}")
        save_to_file(IPADDRESS_FILE, ipAddress)
        print(f"{Fore.CYAN}Lưu ip vào file thành công !!!")

    #Download/Upload file save
        print("Chương trình đang chờ bạn thao tác. Nhấn phím bất kỳ rồi Enter để tiếp tục...")
        input()  # Chương trình sẽ chờ đến khi người dùng nhấn Enter
        print("Chương trình tiếp tục!\n")

        chooseFiles = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div[3]/a[2]')
        chooseFiles.click()
        print(f"{Fore.LIGHTYELLOW_EX}File => ", end="")

        choosePal = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[5]/a')
        choosePal.click()
        print(f"{Fore.LIGHTYELLOW_EX}Pal => ", end="")

        chooseSaved = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[4]/a')
        chooseSaved.click()
        print(f"{Fore.LIGHTYELLOW_EX}Saved => ", end="")

        chooseSaveGames = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[3]/a')
        chooseSaveGames.click()
        print(f"{Fore.LIGHTYELLOW_EX}SaveGames => ", end="")

        choose0 = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[1]/a')
        choose0.click()
        print(f"{Fore.LIGHTYELLOW_EX}0 ", end="")

        print("\nChương trình đang chờ bạn thao tác. Nhấn phím bất kỳ rồi Enter để tiếp tục...")
        input()  # Chương trình sẽ chờ đến khi người dùng nhấn Enter
        print("Chương trình tiếp tục!\n")

    #Quay về Main menu -> tiến vào PalWorldSettings.ini
        chooseFiles = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div[3]/a[2]')
        chooseFiles.click()
        print(f"{Fore.LIGHTYELLOW_EX}Files ", end="")

        choosePal = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[5]/a')
        choosePal.click()
        print(f"{Fore.LIGHTYELLOW_EX}Pal => ", end="")

        chooseSaved = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[4]/a')
        chooseSaved.click()
        print(f"{Fore.LIGHTYELLOW_EX}Saved => ", end="")

        chooseConfig = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[1]/a')
        chooseConfig.click()
        print(f"{Fore.LIGHTYELLOW_EX}Config => ", end="")

        chooseLinuxServer = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/a')
        chooseLinuxServer.click()
        print(f"{Fore.LIGHTYELLOW_EX}LinuxServer", end="")


        print("Chương trình đang tạm dừng. Nhấn phím bất kỳ rồi Enter để tiếp tục...")
        input()  # Chương trình sẽ chờ đến khi người dùng nhấn Enter
        print("Chương trình tiếp tục!\n")

    except Exception as ex:
        print(f"{Fore.RED}Có lỗi trong lúc mở link !!!")
    finally:
        browser.quit()









# ============================================================================================================================================ #    