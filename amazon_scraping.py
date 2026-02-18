import requests
from base64 import BeautifulSoup
import pandas as pd
import re
import time
import numpy as np

# Empty list
all_laptops = []

# Headers (important)
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Scraping 5 pages (100+ laptops)
for page in range(1,6):

    print(f"Scraping page {page}")

    url = f"https://www.amazon.in/s?k=laptop&page={page}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    products = soup.select(".s-result-item")

    for product in products:

        text = product.get_text(" ", strip=True)

        # Title
        title_tag = product.find("h2")
        title = title_tag.get_text(strip=True) if title_tag else None

        # Brand
        brand = re.match(r"^\w+", title).group() if title else None

        # Price
        price = re.search(r"₹\s?([\d,]+)", text)
        price = price.group(1).replace(",", "") if price else None

        # Rating
        rating = re.search(r"(\d+(\.\d+)?)\s?out of 5", text)
        rating = rating.group(1) if rating else None

        # Processor
        processor = re.search(r"(i[3579]|Ryzen\s?\d)", text)
        processor = processor.group() if processor else None

        # RAM
        ram = re.search(r"(\d+)\s?GB", text)
        ram = ram.group(1)+"GB" if ram else None

        # Storage
        storage = re.search(r"(\d+)\s?(GB|TB)\s?(SSD|HDD)?", text)
        storage = storage.group() if storage else None

        # Screen
        screen = re.search(r"(\d+(\.\d+)?)\s?(Inch|Inches)", text)
        screen = screen.group(1) if screen else None

        # Windows
        windows = re.search(r'(?:Windows\s*|Win\s*)(\d+)', text, re.IGNORECASE)
        windows = "Windows " + windows.group(1) if windows else None

        # Color
        color = re.search(r"(?:Colour|Color)\s*[:-]?\s*([A-Za-z ]+)", text)
        color = color.group(1).strip() if color else None

        all_laptops.append([
            title, brand, price, rating,
            processor, ram, storage,
            screen, windows, color
        ])

    time.sleep(2)

# Create DataFrame
columns = [
    "Title","Brand","Price","Rating",
    "Processor","RAM","Storage",
    "Screen","Windows","Color"
]

df = pd.DataFrame(all_laptops, columns=columns)

# Save RAW
df.to_csv("amazon_laptop_raw.csv", index=False)

# Cleaning
df.drop_duplicates(inplace=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df.dropna(subset=["Price","Rating","Brand"], inplace=True)

# Save CLEANED
df.to_csv("amazon_laptop_cleaned.csv", index=False)

print("Scraping Completed Successfully!")