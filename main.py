import pandas as pd

from Scraper.the_cannon import scrape_the_cannon
from Scraper.places4students import scrape_places4students

all_listings = []

all_listings.extend(scrape_the_cannon())
all_listings.extend(scrape_places4students())

df = pd.DataFrame(all_listings)

df.drop_duplicates(subset=["Link"], inplace=True)

df.to_csv("houses.csv", index=False)

print(f"Saved {len(df)} listings")