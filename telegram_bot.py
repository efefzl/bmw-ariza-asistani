import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
from agent import run_agent
from memory import save_memory, get_memory_summary
from database import save_to_db, search_db
from vision import analyze_image

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚗 BMW X1 2016 sDrive18i Arıza Asistanı\n\n"
        "Kullanım:\n"
        "• Arızayı yazarak tarif et\n"
        "• Arızalı bölgenin fotoğrafını gönder\n"
        "• İkisini birlikte yapabilirsin\n\n"
        "📋 Komutlar:\n"
        "/gecmis — Geçmiş arızalarını gör\n\n"
        "Örnek mesaj: 'Motor titriyor'\n"
        "Örnek fotoğraf: Motor bölmesi, egzoz, lastik vb."
    )

async def gecmis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    ozet = get_memory_summary(user_id)
    if ozet:
        await update.message.reply_text(f"📋 Geçmiş Arızaların:\n\n{ozet}")
    else:
        await update.message.reply_text("Henüz kayıtlı arıza yok.")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Fotoğraf mesajlarını işle."""
    user_id = update.effective_user.id
    
    await update.message.reply_text(
        "📸 Fotoğraf alındı, analiz ediliyor...\n"
        "(20-30 saniye sürebilir)"
    )
    
    try:
        # En yüksek çözünürlüklü fotoğrafı indir
        photo = update.message.photo[-1]
        file = await context.bot.get_file(photo.file_id)
        
        image_path = f"temp_{user_id}.jpg"
        await file.download_to_drive(image_path)
        
        # Fotoğrafı analiz et
        gorsel_analiz = analyze_image(image_path)
        
        # Geçici dosyayı sil
        os.remove(image_path)
        
        await update.message.reply_text(
            f"🔬 Görsel Analiz Sonucu:\n\n{gorsel_analiz}\n\n"
            "🔍 Şimdi detaylı araştırma yapılıyor..."
        )
        
        # Görsel analize dayanarak web araştırması yap
        gecmis_ozet = get_memory_summary(user_id)
        
        # Kullanıcı fotoğrafla birlikte metin de gönderdiyse ekle
        ek_metin = update.message.caption or ""
        
        tam_ariza = f"Fotoğraf analizi sonucu tespit edilen sorun:\n{gorsel_analiz}"
        if ek_metin:
            tam_ariza += f"\n\nKullanıcının notu: {ek_metin}"
        if gecmis_ozet:
            tam_ariza += f"\n\n{gecmis_ozet}"
        
        rapor = run_agent(tam_ariza)
        
        # Kaydet
        save_memory(user_id, tam_ariza[:200], rapor)
        save_to_db(tam_ariza[:200], rapor)
        
        # Raporu gönder
        if len(rapor) <= 4096:
            await update.message.reply_text(rapor)
        else:
            parcalar = [rapor[i:i+4096] for i in range(0, len(rapor), 4096)]
            for parca in parcalar:
                await update.message.reply_text(parca)
                
    except Exception as e:
        await update.message.reply_text(f"❌ Hata: {str(e)}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Metin mesajlarını işle."""
    user_id = update.effective_user.id
    ariza = update.message.text
    
    await update.message.reply_text(
        "🔍 Araştırılıyor...\n"
        "OBD kodları ve parça numaraları dahil detaylı rapor hazırlanıyor.\n"
        "(30-60 saniye sürebilir)"
    )
    
    try:
        gecmis_ozet = get_memory_summary(user_id)
        benzer_ariza = search_db(ariza)
        
        tam_ariza = ariza
        if gecmis_ozet:
            tam_ariza += f"\n\n{gecmis_ozet}"
        if benzer_ariza:
            tam_ariza += f"\n\n{benzer_ariza}"
        
        rapor = run_agent(tam_ariza)
        
        save_memory(user_id, ariza, rapor)
        save_to_db(ariza, rapor)
        
        if len(rapor) <= 4096:
            await update.message.reply_text(rapor)
        else:
            parcalar = [rapor[i:i+4096] for i in range(0, len(rapor), 4096)]
            for parca in parcalar:
                await update.message.reply_text(parca)
                
    except Exception as e:
        await update.message.reply_text(f"❌ Hata: {str(e)}")

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gecmis", gecmis))
    
    # Fotoğraf handler'ı
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    # Metin handler'ı
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 BMW Arıza Botu başlatıldı (fotoğraf analizi aktif)...")
    app.run_polling()

if __name__ == "__main__":
    main()