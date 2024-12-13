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

# =========================================================================================================================================================================================================================================== #

#Dữ liệu mẫu
    # Danh sách các tên và họ phổ biến tại Việt Nam
first_names = ["Nguyen", "Tran", "Le", "Pham", "Hoang", "Phan", "Vu", "Dang", "Bui", "Do"]
last_names = ["Anh", "Hoa", "Nam", "Linh", "Minh", "Thuy", "Thanh", "Duc", "Hieu", "Huong"]

    #Danh sách tên công ty
companyName = ["Công ty TNHH Cảnh Quan Việt", "Công ty TNHH Dịch Vụ Số Việt", "Công ty Cổ phần Đầu tư Vina", "Công ty TNHH Xây Dựng Minh Quang", "Công ty TNHH Việt Vận", "Công ty TNHH Ánh Dương", "Công ty Cổ phần Phát Triển VNX"]

    #Danh sách tên đường Việt Nam
streetAddress1 = ["Đường Nguyễn Văn Cừ", "Đường Lê Lợi", "Đường Trần Hưng Đạo", "Đường Nguyễn Thái Học", "Đường Phan Đình Phùng", "Đường Lý Thường Kiệt", "Đường Võ Văn Kiệt", "Đường Đường Láng", "Đường Tôn Đức Thắng", "Đường Lê Duẩn"]
streetAddress2 = ["Đường Nguyễn Xí", "Đường Hồ Tùng Mậu", "Đường Bạch Đằng", "Đường Phạm Văn Đồng", "Đường Nguyễn Đình Chiểu", "Đường Cộng Hòa", "Đường Trường Chinh", "Đường Hoàng Hoa Thám", "Đường Nguyễn Huệ", "Đường Kim Mã"]

    #Danh sách tên Thành phố
cityName = ["Hồ Chí Minh", "Hải Phòng", "Đà nẵng", "Bến tre", "Hà Nội", "Lạng sơn", "Cà Mau", "Ninh Bình", "Vũng tàu"]
stateName = ["Quận 1", "Quận 2", "Quận 3", "Quận 4", "Quận 5", "Quận 6", "Quận 7", "Quận 8", "Quận 9", "Quận 10", "Quận 11", "Quận 12", "Quận Gò Vấp", "Quận Bình Thạnh", "Quận Thủ Đức", "Quận Phú Nhuận"]

    #Danh sách postCode
postCode = ["100000", "700000", "500000", "400000", "900000", "880000", "790000", "220000", "240000", "820000", "750000"]

    #Danh sách sleep time
timesleep = [3, 5, 4]

# =========================================================================================================================================================================================================================================== #


#Đường dẫn file
    #Email file path:
EMAIL_FILE = "emails.txt"

    #Phone number file path:
PHONE_FILE = "phonenumber.txt"
    
    #Password file path:
PASSWORD_FILE = "password.txt"


# =========================================================================================================================================================================================================================================== #


#Các hàm bổ trợ:

    # EMAIL:
def clean_email_file(file_path):
    """Xóa các email trùng lặp và dòng trống trong tệp."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            emails = {email.strip() for email in file if email.strip()}
        with open(file_path, "w") as file:
            for email in sorted(emails):  # Ghi lại các email đã làm sạch
                file.write(email + "\n")

def load_existing_emails(file_path):
    """Đọc các email đã tạo từ tệp."""
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass
    with open(file_path, "r") as file:
        return {email.strip() for email in file if email.strip()}

def save_email_to_file(file_path, email):
    """Ghi email mới vào tệp."""
    with open(file_path, "a") as file:
        file.write(email + "\n")

def generate_email(existing_emails, max_attempts=10000):
    """Tạo email ngẫu nhiên và đảm bảo không trùng."""
    for _ in range(max_attempts):  # Giới hạn số lần thử
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        random_numbers = ''.join(random.choices(string.digits, k=4))
        email = f"{first_name}{last_name}{random_numbers}@gmail.com".lower()
        if email not in existing_emails:
            existing_emails.add(email)
            save_email_to_file(EMAIL_FILE, email)  # Lưu email vào tệp
            return email
    raise ValueError("Không thể tạo email mới: đã đạt giới hạn số lần thử.")
        
        

    # PASSWORD:
def save_password_to_file(file_path, value):
    with open(file_path, "a") as file:
        file.write(f"{value}\n")

    #PHONE NUMBER:
def load_existing_phones(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return set(file.read().splitlines())
    return set()

def save_phone_to_file(file_path, phone):
    with open(file_path, "a") as file:
        file.write(phone + "\n")

def generate_vietnam_phone(existing_phones):
    prefixes = [
        "086", "096", "097", "098",       # Viettel
        "032", "033", "034", "035", "036", "037", "038", "039",  # Viettel
        "090", "093",                    # Mobifone
        "070", "079", "077", "076", "078",  # Mobifone
        "091", "094",                    # Vinaphone
        "081", "082", "083", "084", "085",  # Vinaphone
        "092",                           # Vietnamobile
        "056", "058"                     # Vietnamobile
    ]

    while True:
        prefix = random.choice(prefixes)
        random_numbers = ''.join(random.choices("0123456789", k=7))
        phone_number = f"{prefix}{random_numbers}"
        if phone_number not in existing_phones:
            existing_phones.add(phone_number)
            save_phone_to_file(PHONE_FILE, phone_number)  # Lưu số điện thoại vào tệp
            return phone_number   


# =========================================================================================================================================================================================================================================== #


#Source code chính
    
def reg_account():
        #Khởi tạo chrome:
    browser = uc.Chrome()

        #Trình thử lại sau khi thử tìm element ( default 20 times )
    browser.implicitly_wait(20)

        #Mở chrome:
    try:
        browser.get('https://billing.sparkedhost.com/store/free-trials/24-hour-trial-palworld')

        #Set thời gian chờ mở load đường link
        for i in range(1, 7):
            print(f"Đang load link - {i}\n")
            time.sleep(1)
        
        #Tick chọn server location
        tickServerLocation = browser.find_element(By.XPATH, '//*[@id="productConfigurableOptions"]/div/div[2]/div/div[7]/div/div/label/div[1]/ins')
        tickServerLocation.click()
        time.sleep(random.choice(timesleep))

        #Nhấn continue
        pressContinue = browser.find_element(By.XPATH, '//*[@id="btnCompleteProductConfig"]')
        pressContinue.click()

        #Nhấn checkout
        pressCheckout = browser.find_element(By.XPATH, '//*[@id="checkout"]')
        pressCheckout.click()

    #Điền thông tin
        #Nhập tên:
        enterFirstName = browser.find_element(By.XPATH, '//*[@id="inputFirstName"]')
        temp_firstName = random.choice(last_names)
        print(f"{Fore.GREEN}Nhập \"TÊN\" thành công - {temp_firstName}")
        enterFirstName.send_keys(temp_firstName)

        #Nhập họ:
        enterLastName = browser.find_element(By.XPATH, '//*[@id="inputLastName"]')
        temp_lastName = random.choice(last_names)
        print(f"{Fore.GREEN}Nhập \"HỌ\" thành công - {temp_lastName}")
        enterLastName.send_keys(temp_lastName)
        
        #Nhập email:
        existing_emails = load_existing_emails(EMAIL_FILE)
        new_email = generate_email(existing_emails)
        print(f"{Fore.GREEN}Tạo email thành công")
        Style.RESET_ALL
        print(f"{Style.RESET_ALL}Email vừa tạo: {new_email}")
        enterEmail = browser.find_element(By.XPATH, '//*[@id="inputEmail"]')
        enterEmail.send_keys(new_email)
        
        #Chọn quốc gia - sđt
        chooseTheCountry = browser.find_element(By.XPATH, '//*[@id="personalInformation"]/div/div[4]/div/div/div/div/div[2]')
        chooseTheCountry.click()

            #Tìm Việt Nam
        chooseTheCountry = browser.find_element(By.XPATH, '//*[@id="personalInformation"]/div/div[4]/div/div/div/ul/li[240]')
        chooseTheCountry.click()

        #Nhập số điện thoại
            #Load các số điện thoại đã tạo trước đó:
        existing_phonenumber = load_existing_phones(PHONE_FILE)
            #Tạo số điện thoại mới:
        new_phonenumber = generate_vietnam_phone(existing_phonenumber)
        print(f"{Fore.GREEN}Tạo số điện thoại mới thành công !")
        print(f"{Style.RESET_ALL}Số điện thoại vừa tạo: {new_phonenumber}")
        enterPhonenumber = browser.find_element(By.XPATH, '//*[@id="inputPhone"]')
        enterPhonenumber.send_keys(new_phonenumber)
        print(f"{Fore.GREEN}Nhập số điện thoại thành công !!")

        #Nhập thông tin bill
            #Tên công ty:
        enterCompanyname = browser.find_element(By.XPATH, '//*[@id="inputCompanyName"]')
        temp_Companyname = random.choice(companyName)
        enterCompanyname.send_keys(temp_Companyname)
        print(f"{Fore.GREEN}Nhập \"tên công ty\" thành công !!")
        print(f"{Style.RESET_ALL}Tên công ty vừa nhập: {temp_Companyname}")
            #Nhập địa chỉ đường thứ I:
        enterStreetAddress1 = browser.find_element(By.XPATH, '//*[@id="inputAddress1"]')
        temp_StreetAddress1 = random.choice(streetAddress1)
        print(f"{Fore.GREEN}Nhập \"địa chỉ đường thứ I\" thành công !!")
        print(f"{Style.RESET_ALL}Tên đường vừa nhập: {temp_StreetAddress1}")
        enterStreetAddress1.send_keys(temp_StreetAddress1)
            #Nhập địa chỉ đường thứ II:
        enterStreetAddress2 = browser.find_element(By.XPATH, '//*[@id="inputAddress2"]')
        temp_StreetAddress2 = random.choice(streetAddress2)
        print(f"{Fore.GREEN}Nhập \"địa chỉ đường thứ II\" thành công !!")
        print(f"{Style.RESET_ALL}Tên đường vừa nhập: {temp_StreetAddress2}")
        enterStreetAddress2.send_keys(temp_StreetAddress2)
            #Nhập tên Thành phố
        enterCityname = browser.find_element(By.XPATH, '//*[@id="inputCity"]')       
        temp_Cityname = random.choice(cityName)
        print(f"{Fore.GREEN}Nhập \"tên thành phố\" thành công !!")
        print(f"{Style.RESET_ALL}Tên thành phố vừa nhập: {temp_Cityname}")
        enterCityname.send_keys(temp_Cityname)
            #Nhập mã bưu điện
        enterPostcode = browser.find_element(By.XPATH, '//*[@id="inputPostcode"]')
        temp_Postcode = random.choice(postCode)
        print(f"{Fore.GREEN}Nhập \"mã bưu điện\" thành công !!")
        print(f"{Style.RESET_ALL}Mã bưu điện vừa nhập: {temp_Postcode}")
        enterPostcode.send_keys(temp_Postcode)
            #Chọn quốc gia - billing address
        selectCountry = browser.find_element(By.XPATH, '//*[@id="inputCountry"]')
        select = Select(selectCountry)
        select.select_by_value("VN")
                #Chờ load trường (tỉnh/thành phố)
        time.sleep(2)
            #Nhập quận/tỉnh
        enterState = browser.find_element(By.XPATH, '//*[@id="stateinput"]')
        temp_State = random.choice(stateName)
        print(f"{Fore.GREEN}Nhập \"quận/tỉnh\" thành công !!")
        print(f"{Style.RESET_ALL}Quận/tỉnh vừa nhập: {temp_State}")
        enterState.send_keys(temp_State)

            #Tick chọn lớn hơn 13 tuổi
        tickOverAge = browser.find_element(By.XPATH, '//*[@id="iCheck-customfield279"]/ins')
        print(f"{Fore.GREEN}Tick chọn lớn hơn 13 tuổi thành công !!")
        tickOverAge.click()
            #Tạo tự động mật khẩu mới
        generatePassword = browser.find_element(By.XPATH, '//*[@id="containerPassword"]/div[4]/div/button')
        generatePassword.click()
        time.sleep(2)
                #Copy to clipboard and insert:
        copyToClipboard = browser.find_element(By.XPATH, '//*[@id="btnGeneratePasswordInsert"]')
        copyToClipboard.click()
        time.sleep(2)
        temp_Password = pyperclip.paste()
        save_password_to_file(PASSWORD_FILE, temp_Password)
        print(f"{Fore.GREEN}Khởi tạo và insert mật khẩu thành công !!")
        print(f"{Fore.GREEN}Lưu mật khẩu thành công !!")
        print(f"{Style.RESET_ALL}Mật khẩu vừa tạo: {temp_Password}")
        #Chọn phương thức thanh toán:
        payment_methods = [
            '//*[@id="paymentGatewaysContainer"]/div/div[1]/div/div[2]/div/div/label',
            '//*[@id="paymentGatewaysContainer"]/div/div[1]/div/div[3]/div/div/label',
            '//*[@id="paymentGatewaysContainer"]/div/div[1]/div/div[4]/div/div/label',
            '//*[@id="paymentGatewaysContainer"]/div/div[1]/div/div[5]/div/div/label',
            '//*[@id="paymentGatewaysContainer"]/div/div[1]/div/div[6]/div/div/label'
        ]
        clickChoice = browser.find_element(By.XPATH, random.choice(payment_methods))
        print(f"{Fore.GREEN}Chọn phương thức thanh toán thành công !!")
        clickChoice.click()
        #Chọn i have read
        tickIHaveRead = browser.find_element(By.XPATH, '//*[@id="iCheck-accepttos"]/ins')
        print(f"{Fore.GREEN}Tick chọn \"i have read\" thành công !!")
        tickIHaveRead.click()
        #Complete Order
        completeOrder = browser.find_element(By.XPATH, '//*[@id="btnCompleteOrder"]')
        completeOrder.click()
        

        
    except Exception as ex:
        print(f"{Fore.RED}Có lỗi trong lúc mở link - {ex}")
    finally:
        print(f"{Fore.CYAN}HOÀN THÀNH !!")
        print(f"{Fore.LIGHTYELLOW_EX}Tài khoản: {new_email}")
        print(f"{Fore.LIGHTYELLOW_EX}Mật khẩu: {temp_Password}")
        browser.quit()

        


# =========================================================================================================================================================================================================================================== #