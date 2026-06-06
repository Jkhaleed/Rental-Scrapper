import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

BASE_URL = "https://rentals.ca"

def scrape_rentals_ca():
    data = []

    url = "https://rentals.ca/guelph"
    page = requests.get(url, headers=HEADERS)

    print(page.status_code)

    soup = BeautifulSoup(page.text, "html.parser")

    # TEMP: find all links that look like rental listings
    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "/guelph/" in href:
            links.append(urljoin(BASE_URL, href))

    links = list(set(links))

    print(f"Found {len(links)} possible Rentals.ca links")

    for link in links:
        print(link)

    return data