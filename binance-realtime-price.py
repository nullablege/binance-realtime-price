import requests
from bs4 import BeautifulSoup

url = "https://www.binance.com/tr/price/"
birim = input("Enter CryptoCurrency :")
url = url + birim
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,"html.parser")
section = soup.select('#__APP > section > div > div.css-1sybtvp > div.css-d9qi8n > div.css-1267ixm > div.css-1bwgsh3')
gunluk = soup.select('#__APP > section > div > div.css-1sybtvp > div.css-d9qi8n > div.css-i0y2du > div.css-1pxm4lx > table > tbody > tr:nth-child(1) > td.css-6kgnun')
gunluk30 = soup.select('#__APP > section > div > div.css-1sybtvp > div.css-d9qi8n > div.css-i0y2du > div.css-1pxm4lx > table > tbody > tr:nth-child(2) > td.css-6kgnun')
gunluk60 = soup.select('#__APP > section > div > div.css-1sybtvp > div.css-d9qi8n > div.css-i0y2du > div.css-1pxm4lx > table > tbody > tr:nth-child(3) > td.css-1604ved')
gunluk90 = soup.select('#__APP > section > div > div.css-1sybtvp > div.css-d9qi8n > div.css-i0y2du > div.css-1pxm4lx > table > tbody > tr:nth-child(4) > td.css-1604ved')

print("Current Price : ",section[0].text)
try:
    print("Daily difference",gunluk[0].text)
except:
    pass
try:
    print("Monthly difference",gunluk30[0].text)
except:
    pass
try:
    print("2 Monthly difference",gunluk60[0].text)
except:
    pass
try:
    print("2 Monthly difference",gunluk90[0].text)
except:
    pass
print("Prices are taken from Binance in real time.")
