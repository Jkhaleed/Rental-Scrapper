from django.urls import path
from .views import ListingListView

urlpatterns = [
    path("listings/", ListingListView.as_view(), name="listings"),
]