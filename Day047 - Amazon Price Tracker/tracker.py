from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.ca/Instant-Pot-Ultra-Electric-Stainless/dp/B06Y1MP2PY/ref=sr_1_1?dchild=1&keywords=Instant+Pot+10+in+1&qid=1626541261&sr=8-1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=header)
webpage = response.text

soup = BeautifulSoup(webpage,"html.parser")

price = soup.find(id="priceblock_ourprice").get_text()

price = float(price.split("$")[1])

print(price)