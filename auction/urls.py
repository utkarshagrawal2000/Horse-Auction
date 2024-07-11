from django.urls import path
from .views import HorseListView,horsedetail,HorseDetailView,BidListView,LiveAuctionListView,BlogListView,RegisterView,BidCreateView,listingview
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('horses/', HorseListView.as_view(), name='horse-list'),
    path('horses_detail/', horsedetail, name='horsedetail'),
    path('horse/<str:id>/', HorseDetailView.as_view(), name='horse'),
    path('bids/', BidListView.as_view(), name='bid-list'),
    path('bids_create/', BidCreateView.as_view(), name='bids_create'),
    path('bids_detail/<str:id>', BidCreateView.as_view(), name='bids_detail'),
    path('live-auctions/', LiveAuctionListView.as_view(), name='live-auctions'),
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('list/', listingview,name='listingview'),
]
