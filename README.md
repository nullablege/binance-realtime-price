# 📈 Binance Gerçek Zamanlı Fiyat Kazıyıcı (Python Web Scraper)

![Python Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png)

![Binance Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Binance_Logo.png/800px-Binance_Logo.png)

Bu Python betiği, dünyanın en büyük kripto para borsalarından biri olan **Binance'in resmi web sitesinden (`binance.com/tr/price/`) anlık kripto para fiyatlarını ve çeşitli zaman dilimlerindeki fiyat değişimlerini** çekmek için tasarlanmıştır. Web scraping (web kazıma) için popüler `requests` kütüphanesi ile sayfanın HTML içeriğini alır ve `BeautifulSoup4` kütüphanesi ile bu içeriği ayrıştırarak (parsing) istenen verilere ulaşır.

Kullanıcıdan takip etmek istediği kripto para biriminin sembolünü (örn: "bitcoin", "ethereum", "bnb") girmesi istenir. Script, girilen sembole göre Binance'in ilgili fiyat sayfasına bir GET isteği gönderir, sayfa içeriğini analiz eder ve aşağıdaki bilgileri konsola yazdırır:

*   Kripto paranın **anlık fiyatı**.
*   **Günlük** fiyat farkı (eğer mevcutsa).
*   **Aylık (30 günlük)** fiyat farkı (eğer mevcutsa).
*   **İki aylık (60 günlük)** fiyat farkı (eğer mevcutsa).
*   **Üç aylık (90 günlük)** fiyat farkı (eğer mevcutsa).

Bu proje, kripto para piyasalarını takip etmek ve anlık fiyat bilgilerine hızlıca erişmek isteyenler için kullanışlı bir araçtır ve temel web scraping tekniklerini öğrenmek için iyi bir örnektir.

**Not:** Binance'in web kazıma politikalarına ve hizmet şartlarına uymaya özen gösterin.

---

## 🌟 Temel Özellikler

*   **Binance'ten Anlık Fiyat Çekme:** Kullanıcının belirttiği kripto para biriminin güncel piyasa fiyatını çeker.
*   **Periyodik Fiyat Değişimleri:** Aynı kripto para birimi için günlük, aylık, 2 aylık ve 3 aylık fiyat değişimlerini (yüzdesel veya mutlak fark olarak, sitenin sunduğu şekilde) gösterir (eğer ilgili veri sayfada mevcutsa).
*   **Dinamik URL Oluşturma:** Kullanıcının girdiği kripto para birimi sembolüne göre Binance fiyat sayfasına ait URL'i otomatik olarak oluşturur.
*   **Web Scraping ile Veri Toplama:**
    *   `requests` kütüphanesi ile hedeflenen Binance fiyat sayfasının HTML içeriğini indirir.
    *   `BeautifulSoup4` kütüphanesi ile indirilen HTML içeriğini ayrıştırarak spesifik fiyat ve değişim verilerine CSS seçicileri (`soup.select()`) aracılığıyla erişir.
*   **Sahte Kullanıcı Başlığı (User-Agent):** HTTP isteklerinde gerçek bir tarayıcıyı taklit etmek için standart bir `User-Agent` başlığı kullanır. Bu, web sitelerinin temel bot tespit mekanizmalarını aşmada yardımcı olabilir.
*   **Net ve Anlaşılır Çıktı:** Toplanan tüm fiyat ve değişim bilgilerini düzenli bir şekilde konsola yazdırır.
*   **Temel Hata Yönetimi:** Veri çekme sırasında belirli bir bilginin (örn: 90 günlük değişim) sayfada bulunmaması durumunda oluşabilecek hataları `try-except pass` blokları ile sessizce atlar ve programın çalışmaya devam etmesini sağlar.
*   **Kolay Kurulum ve Kullanım:** Minimal bağımlılıkları (sadece `requests` ve `beautifulsoup4`) sayesinde hızlıca kurulup kullanılabilir.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

*   **Programlama Dili:** Python 3.x
*   **HTTP İstekleri:**
    *   `requests`: Web sayfalarından HTTP GET istekleri yapmak ve HTML içeriğini almak için.
*   **HTML Ayrıştırma (Parsing):**
    *   `BeautifulSoup4` (bs4): HTML (ve XML) dosyalarını ayrıştırmak ve içindeki verilere CSS seçicileri veya diğer yöntemlerle kolayca erişmek için.

---

## ⚙️ Kurulum ve Gereksinimler

Bu script'i çalıştırmadan önce aşağıdaki adımları takip etmeniz gerekmektedir:

1.  **Python 3 Kurulumu:**
    Eğer sisteminizde Python 3 yüklü değilse, [python.org](https://www.python.org/downloads/) adresinden indirip kurun. Kurulum sırasında "Add Python to PATH" seçeneğini işaretlemeyi unutmayın.

2.  **Gerekli Python Kütüphanelerinin Kurulumu:**
    Terminal veya komut istemcisini açın ve aşağıdaki komutları çalıştırarak `requests` ve `beautifulsoup4` kütüphanelerini yükleyin (eğer daha önce yüklemediyseniz):
    ```bash
    pip install requests beautifulsoup4
    ```

---

## 🚀 Nasıl Çalıştırılır?

1.  Yukarıdaki "Kurulum ve Gereksinimler" adımlarını tamamladığınızdan emin olun.
2.  Script dosyasını (`binance-realtime-price.py` veya verdiğiniz başka bir ad) bilgisayarınıza kaydedin.
3.  Bir terminal veya komut istemcisi açın.
4.  Script'in kaydedildiği dizine gidin (`cd path/to/your/script`).
5.  Script'i aşağıdaki komutla çalıştırın:
    ```bash
    python binance-realtime-price.py
    ```
6.  Program sizden "Enter CryptoCurrency :" şeklinde bir istemle kripto para biriminin sembolünü (örn: `bitcoin`, `ethereum`, `bnb`, `dogecoin` - Binance'in URL'de kullandığı küçük harfli semboller) girmenizi isteyecektir.
7.  Sembolü girip Enter'a bastıktan sonra script, Binance'ten verileri çekecek ve sonuçları konsola aşağıdaki gibi bir formatta yazdıracaktır:

    ```
    Current Price :  $30,500.75
    Daily difference +1.25%
    Monthly difference -5.60%
    2 Monthly difference +10.30%
    2 Monthly difference +15.80% 
    Prices are taken from Binance in real time.
    ```
    *(Yukarıdaki değerler ve değişim oranları tamamen örnektir. "2 Monthly difference" başlığının iki kez yazdırılması kodunuzdaki bir kopyala-yapıştır hatasından kaynaklanıyor olabilir, bunu düzeltebilirsiniz.)*

8.  Tüm bilgiler gösterildikten sonra script otomatik olarak sonlanacaktır.

---

## 🧠 Nasıl Çalışıyor? (Teknik Akış)

1.  **Kütüphane İçe Aktarımı:**
    *   `requests` ve `BeautifulSoup` (bs4'ten) kütüphaneleri import edilir.

2.  **Hedef URL ve Başlık (Headers) Tanımlama:**
    *   Binance'in temel fiyat sorgulama URL'i (`https://www.binance.com/tr/price/`) tanımlanır.
    *   Standart bir `User-Agent` içeren `headers` sözlüğü oluşturulur.

3.  **Kullanıcıdan Kripto Para Sembolü Alma:**
    *   `input()` fonksiyonu ile kullanıcıdan hangi kripto para biriminin fiyatını öğrenmek istediği sorulur. Girilen sembol, temel URL'in sonuna eklenerek tam sorgu URL'i oluşturulur.

4.  **Web Sayfasından Veri Çekme:**
    *   Oluşturulan URL'e `requests.get(url, headers=headers)` komutu ile bir HTTP GET isteği yapılır.
    *   Dönen yanıtın (`response`) içeriği (`response.content`) `BeautifulSoup` nesnesine verilerek HTML ayrıştırıcısı (`"html.parser"`) ile bir `soup` nesnesi oluşturulur.

5.  **Veri Ayrıştırma (Scraping):**
    *   **Anlık Fiyat:** `#__APP > section > div > div.css-1sybtvp > div.css-d9qi8n > div.css-1267ixm > div.css-1bwgsh3` CSS seçicisi kullanılarak anlık fiyatı içeren element bulunur ve metni (`.text`) alınır.
    *   **Fiyat Değişimleri (Günlük, Aylık vb.):** Benzer şekilde, günlük, 30 günlük, 60 günlük ve 90 günlük fiyat değişimlerini içeren elementler, çok spesifik CSS seçicileri (`#__APP > section ... > table > tbody > tr:nth-child(N) > td.css-...`) kullanılarak bulunur ve metinleri alınır.
    *   Her bir değişim verisi çekme işlemi ayrı bir `try-except pass` bloğu içine alınmıştır. Bu, eğer belirli bir zaman dilimi için (örn: yeni listelenmiş bir kripto için 90 günlük veri) bilgi mevcut değilse ve ilgili HTML elementi sayfada yoksa, script'in hata verip çökmesini engeller ve sessizce bir sonraki adıma geçer.

6.  **Sonuçların Konsola Yazdırılması:**
    *   Çekilen anlık fiyat ve mevcut olan fiyat değişimleri `print()` fonksiyonları ile formatlı bir şekilde konsola yazdırılır.

7.  **Program Sonu:**
    *   Tüm bilgiler yazdırıldıktan sonra script otomatik olarak sonlanır.

---

## ⚠️ Önemli Notlar ve Sınırlamalar

*   **Web Sitesi Bağımlılığı ve CSS Seçici Kırılganlığı (Çok Kritik):** Bu script'in doğru ve stabil çalışması, **Binance web sitesinin güncel HTML yapısına ve özellikle kullanılan CSS seçicilerine (ID'ler, class'lar, element hiyerarşisi) tamamen bağımlıdır.** Binance, sitesinin tasarımını veya altyapısını güncellerse (ki bu tür siteler sık sık güncellenir), script'in kullandığı CSS seçicileri (`soup.select()` içindeki stringler) geçersiz kalabilir. Bu durumda script hata verebilir, hiçbir veri çekemeyebilir veya yanlış verileri çekebilir. **Script'in seçicileri, Binance sitesi güncellendikçe periyodik olarak kontrol edilmeli ve gerekirse güncellenmelidir.** Dinamik olarak üretilen `css-xxxxx` gibi class adları özellikle kırılgandır.
*   **Resmi API Kullanımı Önerisi:** Binance gibi büyük platformlar genellikle geliştiriciler için resmi API'ler sunar. Web scraping yerine bu **resmi API'leri kullanmak çok daha güvenilir, stabil ve sitenin kullanım koşullarına uygun bir yöntemdir.** API'ler genellikle yapılandırılmış JSON veya XML verisi döndürür ve HTML ayrıştırma zahmetini ortadan kaldırır. Binance'in API'sini kontrol etmeniz şiddetle tavsiye edilir.
*   **Hata Yönetimi:** Mevcut `try-except pass` blokları hataları sessizce atlar. Bu, debugging (hata ayıklama) sürecini zorlaştırabilir. En azından hangi bilginin çekilemediğine dair bir log mesajı yazdırmak veya daha spesifik hata türlerini yakalamak daha iyi bir pratiktir.
*   **IP Engellemesi ve Hız Sınırlamaları:** Bir web sitesine çok sık ve yoğun otomatik istek göndermek, bot aktivitesi olarak algılanabilir ve IP adresinizin geçici veya kalıcı olarak engellenmesine yol açabilir.
*   **Yasal ve Etik Hususlar:** Web scraping yaparken daima hedef sitenin `robots.txt` dosyasına ve Kullanım Koşulları'na saygı gösterilmelidir. Binance'in scraping ile ilgili özel politikaları olabilir. Bu script sadece sorumlu bir şekilde ve sitenin politikalarına uygun olarak kullanılmalıdır.

---

## 🚀 Gelecekteki Geliştirmeler İçin Fikirler

*   **Binance Resmi API Entegrasyonu:** En önemli ve öncelikli geliştirme bu olmalıdır. Scraping yerine resmi API'yi kullanmak script'i çok daha stabil ve güvenilir hale getirecektir.
*   **Daha Robust Seçiciler:** Eğer API kullanımı mümkün değilse, HTML yapısındaki küçük değişikliklere daha dayanıklı olabilecek daha genel XPath seçicileri veya içeriğe dayalı arama yöntemleri denenebilir.
*   **Veri Kaydetme:** Çekilen fiyatları ve değişimleri periyodik olarak bir CSV dosyasına, JSON dosyasına veya bir veritabanına kaydetme.
*   **Fiyat Alarmı:** Belirli bir kripto paranın fiyatı hedeflenen bir seviyeye ulaştığında kullanıcıya bildirim (e-posta, masaüstü bildirimi vb.) gönderme.
*   **Çoklu Kripto Para Takibi:** Tek seferde birden fazla kripto paranın fiyatını çekebilme.
*   **Grafiksel Kullanıcı Arayüzü (GUI):** `Tkinter`, `PyQt` gibi kütüphanelerle veya Flask/Django gibi web framework'leri ile kullanıcı dostu bir arayüz oluşturma.
*   **Gelişmiş Hata Loglama:** Python'ın `logging` modülünü kullanarak detaylı hata ve işlem logları tutma.

---

Bu **Binance Gerçek Zamanlı Fiyat Kazıyıcı**, `requests` ve `BeautifulSoup4` kütüphaneleri ile web scraping'in temellerini ve dinamik sitelerden veri çekmenin zorluklarını gösteren **iyi bir eğitimsel projedir.** Özellikle CSS seçicileri ile karmaşık HTML yapılarından veri çıkarma pratiği sunar. Resmi API kullanımına geçilmesi, projenin güvenilirliğini ve sürdürülebilirliğini önemli ölçüde artıracaktır. **Başarılı bir çalışma!**
