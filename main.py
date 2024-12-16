import asyncio
import os
from colorama import Fore, Style, init
from function import regAccount, loginAndSetup
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import date, datetime
from colorama import Fore, Back, Style, init

from function.discord import read_last_line, send_ip_address, send_image, choose_channels, send_reset_schedule

# ============================================================================================================================================ #


init()

#clear screen console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_server_menu(browser):
    """Menu quản lý server"""
    while True:
        clear_screen()
        print(f"{Fore.CYAN}=== QUẢN LÝ SERVER ===")
        print(f"{Style.RESET_ALL}1. Vào phần SaveFileLocation")
        print("2. Vào phần PalWorldSetting.ini")
        print("3. Bật server")
        print("4. Reset server")
        print("5. Tắt server")
        print("0. Quay lại")
        
        choice = input(f"\n{Fore.YELLOW}Nhập lựa chọn của bạn: {Style.RESET_ALL}")
        
        try:
            if choice == "1":
                print(f"{Fore.GREEN}Đang mở SaveFileLocation...")
                #Nhấn vào file
                pressFile = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div[3]/a[2]')
                pressFile.click()  
                #Nhấn vào Pal
                pressPal = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[6]/a')
                pressPal.click()
                #Nhấn vào Save
                pressSave = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[4]/a')
                pressSave.click()
                #Nhấn vào SavedGame
                pressSavedGame = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[3]/a')
                pressSavedGame.click()
                #Nhấn vào 0
                press0 = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[1]/a')
                press0.click()
                print(f"{Fore.GREEN}Đã mở SaveFileLocation thành công!")

            elif choice == "2":
                print(f"{Fore.GREEN}Đang mở PalWorldSetting.ini...")
                #Nhấn vào file
                pressFile = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div[3]/a[2]')
                pressFile.click()  
                #Nhấn vào Pal
                pressPal = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[6]/a')
                pressPal.click()
                #Nhấn vào Save
                pressSave = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[4]/a')
                pressSave.click()
                #Nhấn vào Config
                pressConfig = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[1]/a')
                pressConfig.click()
                #Nhấn vào LinuxServer
                pressLinuxServer = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/a')
                pressLinuxServer.click()
                #Nhấn vào file PalWorldSetting.ini
                pressPalWorldSetting = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[26]/a')
                pressPalWorldSetting.click()
                print(f"{Fore.GREEN}Đã mở PalWorldSetting.ini thành công!")

            elif choice == "3":
                print(f"{Fore.GREEN}Đang bật server...")
                pressStart = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]')
                pressStart.click()
                print(f"{Fore.GREEN}Đã gửi lệnh bật server!")

            elif choice == "4":
                print(f"{Fore.GREEN}Đang reset server...")
                pressReset = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/button[2]')
                pressReset.click()
                print(f"{Fore.GREEN}Đã gửi lệnh reset server!")

            elif choice == "5":
                print(f"{Fore.GREEN}Đang tắt server...")
                pressStop = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/button[3]')
                pressStop.click()
                print(f"{Fore.GREEN}Đã gửi lệnh tắt server!")

            elif choice == "0":
                break

        except Exception as ex:
            print(f"{Fore.RED}Lỗi: {ex}")
        
        input("\nNhấn Enter để tiếp tục...")

def handle_discord_menu():
    """Menu tương tác với Discord"""
    while True:
        clear_screen()
        print(f"{Fore.CYAN}=== TƯƠNG TÁC DISCORD ===")
        print(f"{Style.RESET_ALL}1. Gửi IP server")
        print("2. Gửi thông báo kèm hình ảnh")
        print("3. Gửi thông báo lịch reset server")
        print("0. Quay lại")
        
        choice = input(f"\n{Fore.YELLOW}Nhập lựa chọn của bạn: {Style.RESET_ALL}")
        
        if choice == "1":
            print(f"{Fore.GREEN}Đang gửi IP mới nhất qua Discord...")
            latest_ip = read_last_line(loginAndSetup.IPADDRESS_FILE)
            if latest_ip:
                asyncio.run(send_ip_address(latest_ip))
                
        elif choice == "2":
            print(f"{Fore.GREEN}Gửi hình ảnh qua Discord...")
            image_path = input("Nhập đường dẫn đến file ảnh: ")
            message = input("Nhập tin nhắn kèm theo (Enter để bỏ qua): ")
            target_channels = choose_channels()
            asyncio.run(send_image(image_path, message if message else None, target_channels))
            
        elif choice == "3":
            print(f"{Fore.GREEN}Gửi thông báo lịch reset server...")
            off_time = input("Nhập thời gian TẮT server (VD: 22:30): ")
            on_time = input("Nhập thời gian BẬT server (VD: 22:50): ")
            asyncio.run(send_reset_schedule(off_time, on_time))
            
        elif choice == "0":
            break
            
        input("\nNhấn Enter để tiếp tục...")

def handle_login_menu(browser):
    while True:
        clear_screen()
        print(f"{Fore.CYAN}=== MENU SAU ĐĂNG NHẬP ===")
        print(f"{Style.RESET_ALL}1. Tương tác với server")
        print("2. Tương tác với Discord")
        print("0. Đăng xuất")
        
        choice = input(f"\n{Fore.YELLOW}Nhập lựa chọn của bạn: {Style.RESET_ALL}")
        
        if choice == "1":
            handle_server_menu(browser)
            
        elif choice == "2":
            handle_discord_menu()
            
        elif choice == "0":
            browser.quit()
            break

def main_menu():
    browser = None  # Khởi tạo biến browser
    
    while True:
        clear_screen()
        print(f"{Fore.CYAN}=== MENU CHÍNH ===")
        print(f"{Style.RESET_ALL}1. Đăng ký tài khoản")
        print("2. Đăng nhập")
        print("0. Thoát")
        
        choice = input(f"\n{Fore.YELLOW}Nhập lựa chọn của bạn: {Style.RESET_ALL}")
        
        if choice == "1":
            print(f"{Fore.GREEN}Đang khởi động đăng ký tài khoản...")
            regAccount.reg_account()
            
        elif choice == "2":
            print(f"{Fore.GREEN}Đang đăng nhập...")
            browser = loginAndSetup.login_and_setup()  # Lưu instance browser
            if browser:  # Kiểm tra đăng nhập thành công
                handle_login_menu(browser)
            
        elif choice == "0":
            if browser:
                browser.quit()  # Đảm bảo đóng browser khi thoát
            print(f"{Fore.CYAN}Cảm ơn bạn đã sử dụng chương trình!")
            break
            
        input("\nNhấn Enter để tiếp tục...")


if __name__ == "__main__":
    main_menu()


# ============================================================================================================================================ #


# regAccount.reg_account()
# loginAndSetup.login_and_setup()

