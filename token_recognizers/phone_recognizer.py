import re


def get_phones(text):
    phone_numbers = re.findall(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]", text)
    return phone_numbers
