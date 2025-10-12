import django_filters
from api.models import Listing


#filtration based on price range
class GuelphFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Listing
        fields = {
            'price': ['iexact', 'lt', 'gt', 'range'],
            'date_posted': ['range'],
            'bedroom_count': ['iexact', 'lt', 'gt', 'range'],
            'bathroom_count': ['iexact', 'lt', 'gt', 'range'],
            'utilities': ['exact']
        }

