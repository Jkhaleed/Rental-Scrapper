# scrapers/places4students.py

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

BASE_URL = "https://www.places4students.com"
LISTINGS_URL = "https://www.places4students.com/schools/198/listings/properties"


def get_property_links():
    page = requests.get(LISTINGS_URL, headers=HEADERS)
    soup = BeautifulSoup(page.text, "html.parser")

    property_links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "/schools/198/listings/properties/" in href:
            full_url = urljoin(BASE_URL, href)
            property_links.append(full_url)

    return list(set(property_links))


def scrape_places4students():
    data = []

    property_urls = get_property_links()

    print(f"Found {len(property_urls)} Places4Students listings")

    for url in property_urls:
        print(f"Scraping Places4Students: {url}")

        page = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(page.text, "html.parser")

        title_tag = soup.find("meta", property="og:title")
        desc_tag = soup.find("meta", property="og:description")
        image_tag = soup.find("meta", property="og:image")

        title = title_tag["content"] if title_tag else "N/A"
        desc = desc_tag["content"] if desc_tag else "N/A"
        image = image_tag["content"] if image_tag else "N/A"

        price = re.search(r'\$[\d,]+', title + " " + desc)
        bedrooms = re.search(r'(\d+)\s*bed(room)?s?', desc, re.I)
        bathrooms = re.search(r'(\d+(\.\d+)?)\s*bath(room)?s?', desc, re.I)
        utilities = bool(
            re.search(
                r'(utilities included|all utilities paid|including utilities|utilities and internet)',
                desc,
                re.I
            )
        )

        item = {
            "Source": "Places4Students",
            "Title": title,
            "Link": url,
            "Price": price.group(0) if price else "N/A",
            "Posted": "N/A",
            "Description": desc,
            "Bedrooms": bedrooms.group(1) if bedrooms else "N/A",
            "Bathrooms": bathrooms.group(1) if bathrooms else "N/A",
            "Utilities Included": utilities,
            "Image": image
        }

        data.append(item)

    return data