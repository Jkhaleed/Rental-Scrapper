from rest_framework import serializers
from api.models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = (
            'id',
            'link',
            'scraper',
            'status',
            'price',
            'address',
            'description',
            'date_posted',
            'date_available',
            'category_type',
            'bedroom_count',
            'bathroom_count',
            'utilities',
        )
    