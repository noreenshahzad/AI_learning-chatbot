import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

data_found = False

with open("training_data.txt", "w", encoding="utf-8") as f:
    for p in paragraphs:
        text = p.get_text().strip()
        if len(text) > 50:
            f.write(text + "\n")
            data_found = True

if data_found:
    print("✅ Data scraped successfully!")
else:
    print("❌ No data found, check scraping rules")