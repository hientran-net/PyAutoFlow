import random
import os

# Đường dẫn tệp để lưu các số điện thoại
PHONE_FILE = "vietnamesePhonenumber.txt"

def load_existing_phones(file_path):
    """
    Đọc các số điện thoại đã tạo từ tệp.

    Args:
        file_path (str): Đường dẫn tới tệp lưu số điện thoại.

    Returns:
        set: Tập hợp các số điện thoại đã lưu.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return set(file.read().splitlines())
    return set()

def save_phone_to_file(file_path, phone):
    """
    Ghi số điện thoại mới vào tệp.

    Args:
        file_path (str): Đường dẫn tới tệp lưu số điện thoại.
        phone (str): Số điện thoại cần lưu.
    """
    with open(file_path, "a") as file:
        file.write(phone + "\n")

def generate_vietnam_phone(existing_phones):
    """
    Tạo số điện thoại ngẫu nhiên của Việt Nam.
    Đảm bảo số điện thoại không bị trùng với những số đã tạo trước đó.

    Args:
        existing_phones (set): Tập hợp các số điện thoại đã tạo trước đó.

    Returns:
        str: Số điện thoại hợp lệ và không trùng lặp.
    """
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

# Ví dụ sử dụng
existing_phones = load_existing_phones(PHONE_FILE)
new_phone = generate_vietnam_phone(existing_phones)
print("Số điện thoại mới:", new_phone)
