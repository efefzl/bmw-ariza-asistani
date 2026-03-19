import json
import os

DB_FILE = "ariza_veritabani.json"

def load_db() -> dict:
    if not os.path.exists(DB_FILE):
        return {"arizalar": []}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_to_db(ariza: str, rapor: str, obd_kodlari: list = []):
    """Her arızayı veritabanına ekle — agent zamanla öğrenir."""
    db = load_db()
    
    db["arizalar"].append({
        "ariza": ariza,
        "rapor": rapor[:1000],
        "obd_kodlari": obd_kodlari,
        "anahtar_kelimeler": ariza.lower().split()
    })
    
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def search_db(ariza: str) -> str:
    """Benzer geçmiş arızaları bul."""
    db = load_db()
    kelimeler = set(ariza.lower().split())
    
    benzer = []
    for kayit in db["arizalar"]:
        kayit_kelimeler = set(kayit.get("anahtar_kelimeler", []))
        eslesme = len(kelimeler & kayit_kelimeler)
        if eslesme >= 2:
            benzer.append((eslesme, kayit))
    
    if not benzer:
        return ""
    
    benzer.sort(reverse=True)
    en_benzer = benzer[0][1]
    
    return f"\nBENZER GEÇMİŞ ARIZA: {en_benzer['ariza']}\nÖnceki rapor özeti: {en_benzer['rapor'][:300]}\n"