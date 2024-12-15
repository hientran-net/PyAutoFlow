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

from function.discord import read_last_line, send_ip_address

# ============================================================================================================================================ #


init()

#clear screen console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_file_operations(browser):
    while True:
        clear_screen()
        print(f"{Fore.CYAN}=== QUẢN LÝ FILE SAVE ===")
        print(f"{Style.RESET_ALL}2.1.1. Upload file save")
        print("2.1.2. Download file save")
        print("0. Quay lại")
        
        choice = input(f"\n{Fore.YELLOW}Nhập lựa chọn của bạn: {Style.RESET_ALL}")
        
        if choice == "2.1.1":
            file_path = input("\nNhập đường dẫn file cần upload: ")
            if os.path.exists(file_path):
                # Thêm code upload file ở đây
                print(f"{Fore.GREEN}Đang upload file...")
                time.sleep(2)  # Giả lập thời gian upload
                print("Upload thành công!")
            else:
                print(f"{Fore.RED}Đường dẫn file không tồn tại!")
                
        elif choice == "2.1.2":
            save_path = input("\nNhập vị trí lưu file download: ")
            if os.path.isdir(save_path):
                # Thêm code download file ở đây
                print(f"{Fore.GREEN}Đang download file...")
                time.sleep(2)  # Giả lập thời gian download
                print("Download thành công!")
            else:
                print(f"{Fore.RED}Thư mục lưu file không tồn tại!")
                
        elif choice == "0":
            break
        
        input("\nNhấn Enter để tiếp tục...")

def handle_login_menu(browser):  # Thêm tham số browser
    while True:
        clear_screen()
        print(f"{Fore.CYAN}=== MENU SAU ĐĂNG NHẬP ===")
        print(f"{Style.RESET_ALL}2.1. Vào phần SaveFileLocation.")
        print("2.2. Vào phần PalWorldSetting.ini.")
        print("2.3. Reset server.")
        print("2.4. Gửi IP qua Discord.")
        print("0. Đăng xuất - Đóng trình duyệt.")
        
        choice = input(f"\n{Fore.YELLOW}Nhập lựa chọn của bạn: {Style.RESET_ALL}")
        
        if choice == "2.1":
            print(f"{Fore.GREEN}Đang mở SaveFileLocation...")
            # Sử dụng browser đã đăng nhập để điều hướng
            try:
                # Điều hướng đến trang SaveFileLocation
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


                # Đợi load trang
                time.sleep(2)
                handle_file_operations(browser)
            except Exception as ex:
                print(f"{Fore.RED}Lỗi khi mở SaveFileLocation: {ex}")
            
        elif choice == "2.2":
            print(f"{Fore.GREEN}Đang mở PalWorldSetting.ini...")
            try:
                # Điều hướng đến trang settings
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

                # Thêm code xử lý settings
            except Exception as ex:
                print(f"{Fore.RED}Lỗi khi mở Settings: {ex}")
#Chưa test
        elif choice == "2.3":
            print(f"{Fore.GREEN}Đang reset server...")
            try:
                pressReset = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/button[2]')
                pressReset.click()
                while True:
                    textStatus = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div[2]/div[1]/div[2]/p[2]')
                    print(textStatus.text)
                    if textStatus.text == 'RUNNING (0h 0m 10s)':
                        print("Reset server thành công!")
                        break
                    time.sleep(1)
            except Exception as ex:
                print(f"{Fore.RED}Lỗi khi reset server: {ex}")

        elif choice == "2.4":
            print(f"{Fore.GREEN}Đang gửi IP mới nhất qua Discord...")
            # Đọc IP mới nhất và gửi
            latest_ip = read_last_line(loginAndSetup.IPADDRESS_FILE)
            if latest_ip:
                asyncio.run(send_ip_address(latest_ip))

        elif choice == "0":
            browser.quit()  # Đóng browser khi đăng xuất
            break
            #tesst ttt
        input("\nNhấn Enter để tiếp tục...")

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

