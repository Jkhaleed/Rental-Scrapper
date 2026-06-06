import pandas as pd

from Scraper.the_cannon import scrape_the_cannon
# from Scraper.rentals_ca import scrape_rentals_ca
from Scraper.places4students import scrape_places4students
# from Scraper.solstice import scrape_solstice

def main():
    all_listings = []

    all_listings.extend(scrape_the_cannon())
    # all_listings.extend(scrape_rentals_ca())
    all_listings.extend(scrape_places4students())
    # all_listings.extend(scrape_solstice())

    df = pd.DataFrame(all_listings)
    df.drop_duplicates(subset=["Link"], inplace=True)

    df.to_csv("houses.csv", index=False)

    print(f"Saved {len(df)} listings")

if __name__ == "__main__":
    main()