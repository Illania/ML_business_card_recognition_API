import re


def get_websites(text):
    """Finds all website pattern matches like:
    http://google.com https://google.com http://www.google.com https://www.google.com
    """
    url_extract_pattern = r"(?:(?:https?):\/\/)?(?![@])[\w/\-?=%.]+\.[\w/\-&?=%.]+"
    websites = re.findall(url_extract_pattern, text)
    return list(websites)
