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


#========================================================================================
#Tạo email

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


# Đường dẫn tệp để lưu email
EMAIL_FILE = "emails.txt"

def load_existing_emails(file_path):
    """Đọc các email đã tạo từ tệp."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return set(file.read().splitlines())
    return set()

def save_email_to_file(file_path, email):
    """Ghi email mới vào tệp."""
    with open(file_path, "a") as file:
        file.write(email + "\n")

def generate_email(existing_emails):
    while True:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        random_numbers = ''.join(random.choices(string.digits, k=4))
        email = f"{first_name}{last_name}{random_numbers}@gmail.com".lower()
        if email not in existing_emails:
            existing_emails.add(email)
            save_email_to_file(EMAIL_FILE, email)  # Lưu email vào tệp
            return email


PASSWORD_FILE = "password.txt"
#Lưu dữ liệu vào file
def save_password_to_file(file_path, value):
    with open(file_path, "a") as file:
        file.write(f"{value}                {datetime.now()}\n")


#Tạo số điện thoại

# Đường dẫn tệp để lưu các số điện thoại
PHONE_FILE = "vietnamesePhonenumber.txt"

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
#========================================================================================


# mảng lưu trữ các số giây chờ của chương trình
list1 = [5, 6, 7]

#Mở chrome
driver = uc.Chrome()

#mở link 
try:
    driver.get('https://billing.sparkedhost.com/store/free-trials/24-hour-trial-enterprise-4-gb')
    time.sleep(6)
except:
    print("Lỗi mục mở link");


#Chọn server location
try:
    serverLocation = driver.find_element(By.XPATH, "//*[@id=\"productConfigurableOptions\"]/div[1]/div[2]/div/div[7]/div/div/label/div[1]/ins")
    serverLocation.click()
    time.sleep(random.choice(list1))
except:
    print("Lỗi mục chọn server Location")

#Nhấn chọn continue
try:
    continueBtn = driver.find_element(By.ID, "btnCompleteProductConfig");
    continueBtn.click()
    time.sleep(random.choice(list1))
except:
    print("Lỗi ở mục nút continue")

#Nhấn chọn checkout
try:
    checkoutBtn = driver.find_element(By.ID, "checkout")
    checkoutBtn.click()
    time.sleep(random.choice(list1))
except:
    print("Lỗi ở mục checkout")

#Nhập văn bản
try:
    #nhập tên
    inputFirstName = driver.find_element(By.ID, 'inputFirstName')
    inputFirstName.send_keys("Hien")
    time.sleep(random.choice(list1))

    #nhập họ
    inputLastName = driver.find_element(By.ID, 'inputLastName')
    inputLastName.send_keys('Tran')
    time.sleep(random.choice(list1))

#Nhập email  
    # Tải email đã tạo từ tệp
    existing_emails = load_existing_emails(EMAIL_FILE)

    # Tạo email
    new_email = generate_email(existing_emails)
    print("Email mới:", new_email)
    #Nhập
    inputEmail = driver.find_element(By.ID, 'inputEmail')
    inputEmail.send_keys(new_email)
    time.sleep(random.choice(list1))

    #Chọn quốc gia
    pickNational = driver.find_element(By.XPATH, '//*[@id="personalInformation"]/div/div[4]/div/div/div/div/div[2]')
    pickNational.click()

    #Tìm Việt Nam
    pickNational = driver.find_element(By.XPATH, '//*[@id="personalInformation"]/div/div[4]/div/div/div/ul/li[240]')
    pickNational.click()

#Nhập số điện thoại
    #Tải các số điện thoại đã tạo trước đó từ tệp
    existing_phones = load_existing_phones(PHONE_FILE)
    
    #Tạo số điện thoại
    new_phone = generate_vietnam_phone(existing_phones)
    print("Số điện thoại mới:", new_phone)

    #Nhập
    inputPhone = driver.find_element(By.ID, 'inputPhone')
    inputPhone.send_keys(new_phone)
    time.sleep(random.choice(list1))
        
#Nhập thông tin bill
    #Nhập companyName:
    inputCompanyName = driver.find_element(By.ID, 'inputCompanyName')
    inputCompanyName.send_keys(random.choice(companyName))
    time.sleep(random.choice(list1))

    #Nhập Street Address 1
    inputAddress1 = driver.find_element(By.ID, 'inputAddress1')
    inputAddress1.send_keys(random.choice(streetAddress1))
    time.sleep(random.choice(list1))

    #Nhập Street Address 2
    inputAddress2 = driver.find_element(By.ID, 'inputAddress2')
    inputAddress2.send_keys(random.choice(streetAddress2))
    time.sleep(random.choice(list1))

    #Nhập tên Thành phố
    inputCity = driver.find_element(By.ID, 'inputCity')
    inputCity.send_keys(random.choice(cityName))
    time.sleep(random.choice(list1))

    #Nhập postCode
    inputPostcode = driver.find_element(By.ID, 'inputPostcode')
    inputPostcode.send_keys(random.choice(postCode))
    time.sleep(random.choice(list1))

    #Chọn Nước Việt Nam
    select_element = driver.find_element(By.ID, 'inputCountry')
    select = Select(select_element)
    select.select_by_value("VN")
    time.sleep(random.choice(list1))

    #Nhập quận / Tỉnh
    stateinput = driver.find_element(By.ID, 'stateinput')
    stateinput.send_keys(random.choice(stateName))
    time.sleep(random.choice(list1))

    #Tick chọn lớn hơn 13 tuổi
    TickOverAgeBtn = driver.find_element(By.XPATH, '//*[@id="iCheck-customfield279"]/ins')
    TickOverAgeBtn.click()
    time.sleep(random.choice(list1))


    #Generate password
    generatePass = driver.find_element(By.XPATH, '//*[@id="containerPassword"]/div[4]/div/button')
    generatePass.click()
    time.sleep(2)

    #Copy to clipboard and insert 
    CopyToClipboard = driver.find_element(By.ID, 'btnGeneratePasswordInsert')
    CopyToClipboard.click()
    CopyToClipboard = pyperclip.paste()
    save_password_to_file(PASSWORD_FILE, CopyToClipboard)
    print("Nội dung sao chép vào clipboard:", CopyToClipboard)
    time.sleep(random.choice(list1))

    #Chọn phương thức thanh toán
    listChoice = [1, 2, 3, 4, 5]
    choice = random.choice(listChoice)

    if choice == 1:
        clickChoice = driver.find_element(By.XPATH, '//*[@id="paymentGatewaysContainer"]/div/div[1]/div/div[2]/div/div/label')
        clickChoice.click()
    elif choice == 2:
        clickChoice = driver.find_element(By.XPATH, '//*[@id="paymentGatewaysContainer"]/div/div[1]/div/div[3]/div/div/label')
        clickChoice.click() 
    elif choice == 3:
        clickChoice = driver.find_element(By.XPATH, '//*[@id="paymentGatewaysContainer"]/div/div[1]/div/div[4]/div/div/label')
        clickChoice.click()
    elif choice == 4:
        clickChoice = driver.find_element(By.XPATH, '//*[@id="paymentGatewaysContainer"]/div/div[1]/div/div[5]/div/div/label')
        clickChoice.click()
    else:
        clickChoice = driver.find_element(By.XPATH, '//*[@id="paymentGatewaysContainer"]/div/div[1]/div/div[6]/div/div/label')
        clickChoice.click()
    time.sleep(random.choice(list1))


    #Tick i have read
    tickIHaveRead = driver.find_element(By.XPATH, '//*[@id="iCheck-accepttos"]/ins')
    tickIHaveRead.click()
    time.sleep(random.choice(list1))

    #Hoàn thành
    pressSuccess = driver.find_element(By.ID, 'btnCompleteOrder')
    pressSuccess.click()
    time.sleep(random.choice(list1))


    #Tick client area
    clickClient = driver.find_element(By.XPATH, '//*[@id="order-standard_cart"]/div/div[2]/div[5]/a')
    clickClient.click()
    time.sleep(random.choice(list1))

    #Click Service 
    clickClient = driver.find_element(By.XPATH, '//*[@id="main-body"]/div/div[1]/div[2]/div[1]/div/div[1]/a')
    clickClient.click()
    time.sleep(random.choice(list1))

    clickClient = driver.find_element(By.XPATH, '//*[@id="tableServicesList"]/tbody/tr')
    clickClient.click()
    time.sleep(random.choice(list1))

    clickClient = driver.find_element(By.XPATH, '//*[@id="manage"]/div/div[1]/div/a')
    clickClient.click()
    time.sleep(random.choice(list1))

    clickClient = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div[4]/button')
    clickClient.click()
    time.sleep(random.choice(list1))

    
    clickClient = driver.find_element(By.ID, 'userAuthorizationAccepted')
    clickClient.click()
    time.sleep(random.choice(list1))


except Exception as ex:
    print(f"Có lỗi ở mục nhập văn bản: {ex}")





#======================================================================================================================================#




