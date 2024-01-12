import requests
from bs4 import BeautifulSoup

def fetch_user_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    user_name = soup.select_one('.user-name').text
    other_socials = {
        'Twitter': soup.select_one('.twitter').text,
        'Facebook': soup.select_one('.facebook').text,
        'Instagram': soup.select_one('.instagram').text,
    }
    
    return {
        'user_name': user_name,
        'other_socials': other_socials,
    }

def get_ip_info(ip):
    url = f"https://www.ip-adress.com/{ip}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    ip_info = {
        'IP Address': soup.select_one('.input.value').text,
        'Continent': soup.select_one('.continent.value').text,
        'Country': soup.select_one('.country.value').text,
        'Region': soup.select_one('.region.value').text,
        'City': soup.select_one('.city.value').text,
        'Time Zone': soup.select_one('.timezone.value').text,
        'ZIP Code': soup.select_one('.zip.value').text,
        'ISP': soup.select_one('.isp.value').text,
    }
    
    # Additional data retrieval using BeautifulSoup
    user_info = fetch_user_info(url)
    ip_info.update(user_info)
    
    return ip_info

tiktok_url = input("Enter TikTok URL: ")
print(get_ip_info(tiktok_url))