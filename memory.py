import json
import os
from datetime import datetime

MEMORY_FILE = "ariza_gecmisi.json"

def load_memory(user_id: int) -> list:
    """Kullanıcının geçmiş konuşmalarını yükle."""
    if not os.path.exists(MEMORY_FILE):
        return []
    
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    return data.get(str(user_id), [])

def save_memory(user_id: int, ariza: str, rapor: str):
    """Yeni arızayı kaydet."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}
    
    user_key = str(user_id)
    if user_key not in data:
        data[user_key] = []
    
    data[user_key].append({
        "tarih": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "ariza": ariza,
        "rapor_ozeti": rapor[:500]  # İlk 500 karakter
    })
    
    # Son 10 arızayı tut
    data[user_key] = data[user_key][-10:]
    
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_memory_summary(user_id: int) -> str:
    """Geçmiş arızaların özetini döndür."""
    gecmis = load_memory(user_id)
    
    if not gecmis:
        return ""
    
    ozet = "KULLANICININ GEÇMİŞ ARIZALARI:\n"
    for kayit in gecmis[-3:]:  # Son 3 arıza
        ozet += f"- {kayit['tarih']}: {kayit['ariza']}\n"
    
    return ozet