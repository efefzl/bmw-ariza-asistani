import anthropic
import base64
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

def analyze_image(image_path: str) -> str:
    """Fotoğrafı analiz et ve arıza tespiti yap."""
    
    with open(image_path, "rb") as f:
        image_data = base64.standard_b64encode(f.read()).decode("utf-8")
    
    # Dosya uzantısından media type belirle
    ext = image_path.lower().split(".")[-1]
    media_types = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg", 
        "png": "image/png",
        "gif": "image/gif",
        "webp": "image/webp"
    }
    media_type = media_types.get(ext, "image/jpeg")
    
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": """Bu fotoğraf bir 2016 BMW X1 sDrive18i aracına ait.
                        
Lütfen şunları analiz et:
1. Fotoğrafta ne görüyorsun? (parça, bölge, durum)
2. Görünür bir arıza, hasar veya anormallik var mı?
3. Renk değişikliği, sızıntı, aşınma, kırık veya deformasyon var mı?
4. Bu görüntüye dayanarak olası arıza kaynağı ne olabilir?
5. Daha iyi teşhis için başka hangi açıdan fotoğraf çekilmeli?

Türkçe ve teknik bir dille yanıtla."""
                    }
                ],
            }
        ],
    )
    
    return response.content[0].text