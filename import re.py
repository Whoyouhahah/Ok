import re
import requests
from urllib.parse import urlparse

def extract_ip_address(url):
    ip_regex = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    response = requests.get(url)
    ip_address = re.search(ip_regex, response.text)
    return ip_address.group() if ip_address else None

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except ValueError:
        return False

def fetch_ip_info(url):
    if not validate_url(url):
        return "Invalid URL. Please enter a valid URL."

    if "tiktok.com" in url:
        url = extract_ip_address(url)
        if not url:
            return "Failed to extract IP address from TikTok URL."

    try:
        ip_info = requests.get(f"https://ipinfo.io/{url}").json()
        
        return ip_info
    except requests.exceptions.RequestException as e:
        return f"Error fetching IP information: {e}"

if __name__ == "__main__":
    url = input("Enter a URL to fetch IP information: ")
    print(fetch_ip_info(url))