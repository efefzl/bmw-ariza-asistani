import anthropic
import os
from dotenv import load_dotenv
from tools import web_search, fetch_page
from prompts import SYSTEM_PROMPT

load_dotenv()
client = anthropic.Anthropic()

TOOLS = [
    {
        "name": "web_search",
        "description": "BMW forumları, teknik belgeler ve Türkiye fiyatları için web araması yapar.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Arama sorgusu."
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "fetch_page",
        "description": "Bulunan bir sayfanın tam içeriğini okur.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "Okunacak sayfanın URL'si"
                }
            },
            "required": ["url"]
        }
    }
]

def run_agent(ariza_tanimi: str):
    print(f"\n🚗 BMW X1 Arıza Analizi Başlıyor...")
    print(f"📝 Tarif: {ariza_tanimi}\n")
    print("=" * 50)

    messages = [
        {
            "role": "user",
            "content": f"""Aracımda şu problemi yaşıyorum:

{ariza_tanimi}

Lütfen bu sorunu araştır ve detaylı bir tanı raporu hazırla."""
        }
    ]

    while True:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages
        )

        if response.stop_reason == "tool_use":
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    print(f"  🔎 {block.name}: '{block.input.get('query') or block.input.get('url', '')[:60]}'")

                    if block.name == "web_search":
                        result = web_search(block.input["query"])
                    elif block.name == "fetch_page":
                        result = fetch_page(block.input["url"])
                    else:
                        result = "Araç bulunamadı."

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})

        else:
            print("\n" + "=" * 50)
            rapor = response.content[0].text
            print(rapor)

            with open("ariza_raporu.txt", "w", encoding="utf-8") as f:
                f.write(f"ARIZA TANIMI:\n{ariza_tanimi}\n\n")
                f.write("=" * 50 + "\n\n")
                f.write(rapor)
            print(f"\n💾 Rapor 'ariza_raporu.txt' dosyasına kaydedildi.")
            return rapor


def main():
    print("🚗 BMW X1 2016 sDrive18i — Arıza Tanı Asistanı")
    print("=" * 50)
    print("Aracınızın problemini aşağıya detaylıca yazın.\n")

    ariza = input("Probleminiz: ")

    if ariza.strip():
        run_agent(ariza)
    else:
        print("Lütfen bir problem tanımı girin.")


if __name__ == "__main__":
    main()