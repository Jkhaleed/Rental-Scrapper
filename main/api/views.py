from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer


class ListingListView(ListAPIView):
    queryset = Listing.objects.all().order_by("-date_posted")
    serializer_class = ListingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().order_by("-date_posted")
    serializer_class = ListingSerializer