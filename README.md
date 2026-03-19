# 🚗 BMW X1 AI Diagnostic Assistant

> An AI-powered fault diagnosis assistant for 2016 BMW X1 sDrive18i owners.  
> Works via Telegram — describe your issue or send a photo, get a detailed diagnostic report instantly.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Claude](https://img.shields.io/badge/AI-Claude%20Anthropic-orange)
![Telegram](https://img.shields.io/badge/Platform-Telegram-2CA5E0)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 What Does It Do?

- 🔍 **Automatic web research** — Scans BMW forums and technical documents
- 🔧 **OBD-II fault codes** — Lists likely error codes for your symptoms
- 🔩 **OEM part numbers** — Provides exact BMW part numbers
- 💰 **Cost estimation** — Parts and labor costs in USD and EUR
- 📸 **Photo analysis** — Send a photo of the faulty area, AI analyzes it
- 🧠 **Memory** — Remembers your past issues and finds connections
- ⚠️ **Urgency level** — Drive immediately / Visit soon / Check at next service

---

## 📱 How It Works
```
You  → "Engine shakes badly on cold start, rough idle"

Bot  → 🔍 Researching...
       🔎 Searching: '2016 BMW X1 F48 B38 cold start rough idle'
       🔎 Searching: 'BMW B38 misfire OBD codes part numbers'

Bot  → 📄 DIAGNOSTIC REPORT:
       1. 🔍 Likely Causes: Spark plugs (80%), Ignition coil (60%)...
       2. 🔧 OBD Codes: P0300, P0301, P0302
       3. 🔩 Part No: 12 12 2 158 252 (Spark Plug Set)
       4. 💰 Cost: $45-80 (parts) + $30 labor
       5. ⚠️ Urgency: 🟡 Visit a mechanic this week
```

---

## 🛠️ Installation

### Requirements
- Python 3.10+
- Anthropic API key → [console.anthropic.com](https://console.anthropic.com)
- Tavily API key → [tavily.com](https://tavily.com) *(free tier: 1000 searches/month)*
- Telegram Bot Token → [@BotFather](https://t.me/botfather)

### Steps
```bash
# 1. Clone the repository
git clone https://github.com/efefzl/bmw-ariza-asistani.git
cd bmw-ariza-asistani

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API keys
cp .env.example .env
# Open .env and add your keys
```

### `.env` Configuration
```
ANTHROPIC_API_KEY=sk-ant-...
TAVILY_API_KEY=tvly-...
TELEGRAM_BOT_TOKEN=...
```

### Run
```bash
python telegram_bot.py
```

---

## 📁 Project Structure
```
bmw-ariza-asistani/
├── agent.py          # Core agent logic (web research loop)
├── tools.py          # Web search and page reading tools
├── prompts.py        # BMW-specific system prompt
├── memory.py         # Per-user conversation history
├── database.py       # Fault database (learns over time)
├── vision.py         # Photo analysis (Claude Vision)
├── telegram_bot.py   # Telegram bot interface
├── .env.example      # API key template
└── requirements.txt  # Dependencies
```

---

## 🤖 Tech Stack

| Technology | Purpose |
|---|---|
| [Claude (Anthropic)](https://anthropic.com) | AI analysis engine |
| [Tavily](https://tavily.com) | Real-time web research API |
| [python-telegram-bot](https://python-telegram-bot.org) | Telegram integration |

---

## 📋 Telegram Commands

| Command | Description |
|---|---|
| `/start` | Start the assistant |
| `/history` | View your past diagnostic reports |
| Text message | Describe your car issue |
| Photo | Send a photo of the problem area |

---

## 🗺️ Roadmap

- [x] Web research agent
- [x] OBD code detection
- [x] OEM part number lookup
- [x] Photo analysis
- [x] Fault memory & learning
- [ ] Web interface (SaaS)
- [ ] Support for more BMW models
- [ ] Integration with OBD-II Bluetooth scanners
- [ ] Multilingual support

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Open an issue for bugs or feature requests
- 🔀 Submit a pull request
- ⭐ Star the repo if you find it useful

---

## ⚠️ Disclaimer

This assistant is a **preliminary diagnostic tool** for informational purposes only.  
Always consult a certified BMW technician or authorized service center for final diagnosis and repairs.

---

## 💝 Support

If this project helped you save money on BMW repairs:

- ⭐ **Star this repo** — helps others find it
- 💝 **[Sponsor this project](https://github.com/sponsors/efefzl)** — support ongoing development
- 🐛 **Open an issue** — report bugs or suggest features

---

## 📄 License

MIT License — Free to use, modify, and distribute.
