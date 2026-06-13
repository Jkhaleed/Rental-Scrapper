from django.core.management.base import BaseCommand
from api.models import Listing
from collectors.the_cannon import scrape_the_cannon
from collectors.places4students import scrape_places4students
from datetime import date
import re


class Command(BaseCommand):
    help = "Scrape rental listings and save them to the database"

    def handle(self, *args, **kwargs):
        listings = []

        listings.extend(scrape_the_cannon())
        listings.extend(scrape_places4students())

        for item in listings:
            price_text = str(item.get("Price", "0")).replace(",", "")
            price_match = re.search(r"\d+", price_text)
            price = int(price_match.group()) if price_match else 0

            bedrooms = item.get("Bedrooms")
            bathrooms = item.get("Bathrooms")

            Listing.objects.update_or_create(
                link=item.get("Link"),
                defaults={
                    "scraper": item.get("Source", ""),
                    "address": item.get("Title", "Unknown Address"),
                    "price": price,
                    "description": item.get("Description", ""),
                    "date_posted": date.today(),
                    "date_available": date.today(),
                    "category_type": "",
                    "bedroom_count": int(bedrooms) if str(bedrooms).isdigit() else None,
                    "bathroom_count": int(float(bathrooms)) if bathrooms not in ["N/A", None, ""] else None,
                    "has_half_bedroom": False,
                    "utilities": item.get("Utilities Included", False),
                }
            )

        self.stdout.write(self.style.SUCCESS(f"Saved {len(listings)} listings"))