Binance Real-Time Price Scraper
This Python script retrieves real-time cryptocurrency prices from Binance.

Dependencies:

requests
beautifulsoup4
Setup:

Install the required libraries using pip:


pip install requests beautifulsoup4
Run the script and enter the cryptocurrency symbol (e.g., BTCUSDT) when prompted:


python binance_realtime_price.py
Script Overview:

The script prompts the user to enter a cryptocurrency symbol.
It sends a GET request to Binance's price page for the specified cryptocurrency.
The script parses the page content with BeautifulSoup.
It extracts and prints the current price, as well as daily, monthly, and bi-monthly price differences if available.

Note: Ensure you comply with Binance's scraping policies and terms of service.

---------------------------------------------
Binance Gerçek Zamanlı Fiyat Kazıyıcı
Bu Python betiği, Binance'den gerçek zamanlı kripto para birimi fiyatlarını alır.

Bağımlılıklar:

requests
beautifulsoup4
Kurulum:

Gerekli kütüphaneleri pip ile yükleyin
pip install requests beautifulsoup4
Betiği çalıştırın ve kripto para birimi sembolünü (örneğin, BTCUSDT) istendiğinde girin:
python binance_realtime_price.py
Betiğin Özeti:
Betik, kullanıcıdan bir kripto para birimi sembolü girmesini ister.
Girilen kripto para birimi için Binance'in fiyat sayfasına GET isteği gönderir.
Sayfa içeriğini BeautifulSoup ile analiz eder.
Mevcut fiyatı ve günlük, aylık ve iki aylık fiyat farklarını (varsa) çıkarır ve yazdırır.
Not: Binance'in kazıma politikalarına ve hizmet şartlarına uyduğunuzdan emin olun.

