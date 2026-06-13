from django.db import models
import uuid


# Base listing class
class Listing(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'Active'
        INACTIVE = 'Inactive'

    # Metadata
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField()
    scraper = models.CharField(max_length=50)
    status = models.CharField(
        max_length=10, 
        choices=StatusChoices, 
        default=StatusChoices.ACTIVE
    )
    
    # Core data
    address = models.CharField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=3000)
    date_posted = models.DateField()
    date_available = models.DateField()

    # Optional data (based on the listing website)
    category_type = models.CharField(max_length=100, blank=True)
    bedroom_count = models.IntegerField(null=True, blank=True)
    bathroom_count = models.IntegerField(null=True, blank=True)
    has_half_bedroom = models.BooleanField(null=True, blank=True)
    utilities = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"Listing {self.id} at address: {self.address}"
    