from selenium import webdriver
from selenium.webdriver.common.by import By

# Mở trình duyệt (ví dụ với Chrome)
driver = webdriver.Chrome()

try:
    # Điều hướng đến trang có thẻ HTML
    driver.get("https://example.com")  # Thay bằng URL thật

    # Tìm element bằng class name
    element = driver.find_element(By.CLASS_NAME, "text-sm")  # Tên class "text-sm"

    # Lấy nội dung của thẻ
    ip_address = element.text

    # In địa chỉ IP
    print(f"Địa chỉ IP là: {ip_address}")

    # Lưu vào một biến
    saved_ip = ip_address

finally:
    # Đóng trình duyệt
    driver.quit()

# Xử lý hoặc sử dụng saved_ip sau đó
print(f"Lưu IP: {saved_ip}")
