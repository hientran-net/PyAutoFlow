import random
import string
import os

first_names = ["Nguyen", "Tran", "Le", "Pham", "Hoang", "Phan", "Vu", "Dang", "Bui", "Do"]
last_names = ["Anh", "Hoa", "Nam", "Linh", "Minh", "Thuy", "Thanh", "Duc", "Hieu", "Huong"]
EMAIL_FILE = "function\emails.txt"

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

# Main logic
clean_email_file(EMAIL_FILE)
existing_emails = load_existing_emails(EMAIL_FILE)

try:
    new_email = generate_email(existing_emails)
    print(f"Email mới: {new_email}")
except ValueError as e:
    print(str(e))
