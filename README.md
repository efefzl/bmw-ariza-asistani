# 🚗 BMW X1 Arıza Tanı Asistanı

> 2016 model BMW X1 sDrive18i sahipleri için AI destekli arıza tanı asistanı.  
> Telegram üzerinden çalışır — arızanı yaz veya fotoğraf gönder, detaylı rapor al.

---

## 🎯 Ne Yapar?

- 🔍 **Web araştırması** — BMW forumları ve teknik dokümanları otomatik tarar
- 🔧 **OBD-II kodları** — Olası hata kodlarını listeler
- 🔩 **Parça numaraları** — BMW OEM parça numaralarını verir
- 💰 **Maliyet tahmini** — Türkiye piyasası için TL ve EUR cinsinden
- 📸 **Fotoğraf analizi** — Arızalı bölgenin fotoğrafını gönder, AI analiz etsin
- 🧠 **Hafıza** — Geçmiş arızalarını hatırlar, bağlantı kurar
- ⚠️ **Aciliyet seviyesi** — Hemen git / Yakında git / Rutin bakımda bak

---

## 📱 Nasıl Görünür?
```
Sen → "Soğuk havada motor titriyor"

Bot → 🔍 Araştırılıyor...
      🔎 web_search: '2016 BMW X1 F48 B38 cold start rough idle'
      🔎 web_search: 'BMW X1 B38 motor titreşim Türkiye'

Bot → 📄 RAPOR:
      1. 🔍 Olası Sebepler: Ateşleme bujisi (%80), ...
      2. 🔧 OBD Kodları: P0300, P0301...
      3. 🔩 Parça No: 12 12 2 158 252 (Buji Seti)
      4. 💰 Maliyet: 800-1200 TL (parça) + 300 TL işçilik
      5. ⚠️ Aciliyet: 🟡 Bu hafta içinde git
```

---

## 🛠️ Kurulum

### Gereksinimler
- Python 3.10+
- Anthropic API anahtarı → [console.anthropic.com](https://console.anthropic.com)
- Tavily API anahtarı → [tavily.com](https://tavily.com)
- Telegram Bot Token → [@BotFather](https://t.me/botfather)

### Adımlar
```bash
# 1. Repoyu klonla
git clone https://github.com/efefzl/bmw-ariza-asistani.git
cd bmw-ariza-asistani

# 2. Sanal ortam oluştur
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3. Kütüphaneleri kur
pip install -r requirements.txt

# 4. API anahtarlarını ayarla
cp .env.example .env
# .env dosyasını aç ve anahtarları gir
```

### `.env` Dosyası
```
ANTHROPIC_API_KEY=sk-ant-...
TAVILY_API_KEY=tvly-...
TELEGRAM_BOT_TOKEN=...
```

### Çalıştır
```bash
python telegram_bot.py
```

---

## 📁 Proje Yapısı
```
bmw-ariza-asistani/
├── agent.py          # Ana agent mantığı (web araştırma döngüsü)
├── tools.py          # Web arama ve sayfa okuma araçları
├── prompts.py        # BMW'ye özel sistem promptu
├── memory.py         # Kullanıcı bazlı konuşma geçmişi
├── database.py       # Arıza veritabanı (zamanla öğrenme)
├── vision.py         # Fotoğraf analizi (Claude Vision)
├── telegram_bot.py   # Telegram bot arayüzü
├── .env.example      # API anahtarı şablonu
└── requirements.txt  # Bağımlılıklar
```

---

## 🤖 Kullanılan Teknolojiler

| Teknoloji | Kullanım |
|---|---|
| [Claude (Anthropic)](https://anthropic.com) | AI analiz motoru |
| [Tavily](https://tavily.com) | Web araştırma API'si |
| [python-telegram-bot](https://python-telegram-bot.org) | Telegram entegrasyonu |

---

## 📋 Telegram Komutları

| Komut | Açıklama |
|---|---|
| `/start` | Asistanı başlat |
| `/gecmis` | Geçmiş arızaları gör |
| Metin | Arızayı tarif et |
| Fotoğraf | Arızalı bölgeyi gönder |

---

## ⚠️ Yasal Uyarı

Bu asistan bir **ön tanı aracıdır**. Ürettiği raporlar bilgi amaçlıdır.  
Kesin teşhis ve tamir için yetkili BMW servisi veya uzman bir tamirciye başvurun.

---

## 🌟 Destek

Bu projeyi faydalı buluyorsan:
- ⭐ **Yıldız ver** — Projenin büyümesine yardımcı olur
- 🐛 **Issue aç** — Hata veya öneri bildir
- 💝 **[Sponsor ol](https://github.com/sponsors/efefzl)** — Geliştirmeye destek ol

---

## 📄 Lisans

MIT License — Serbestçe kullanabilir, geliştirebilir ve dağıtabilirsin.
