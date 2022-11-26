import re

def get_emails(text):
    emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
    return emails

