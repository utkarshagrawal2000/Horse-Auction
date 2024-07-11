from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Horse,Bid,Blog
from .serializers import HorseSerializer,BidSerializer,RegisterSerializer,BlogSerializer,BiddetailSerializer
from .filters import HorseFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


def listingview(request):
    return render(request,'auction/listing.html')
def loginview(request):
    return render(request,'auction/login.html')
def registerview(request):
    return render(request,'auction/register.html')


class HorseListView(generics.ListAPIView):
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HorseFilter

class HorseDetailView(APIView):
    def get(self, request, id):
        print(id)
        try:
            horse = Horse.objects.get(id=id)
        except Horse.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = HorseSerializer(horse)
        return Response(serializer.data)
    
def horsedetail(request):
    return render(request,'auction/horse_detail.html')

class BidListView(generics.ListAPIView):
    serializer_class = BidSerializer

    def get_queryset(self):
        horse_id = self.request.query_params.get('horse_id')
        if horse_id is not None:
            bids = Bid.objects.filter(horse_id=horse_id)
            return bids
        return Bid.objects.none()
    
class LiveAuctionListView(generics.ListAPIView):
    serializer_class = HorseSerializer
    def get_queryset(self):
        horse_id = self.request.query_params.get('horse_id')
        if horse_id is not None:
            horse = Horse.objects.filter(Q(auction_enddate__gte=timezone.now())&Q(auction_startdate__lte=timezone.now())).exclude(id=horse_id)[:3]
            return horse
        return Bid.objects.none()

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BidCreateView(APIView):
    
    def post(self,request,format=None):
        horse_id = request.data.get('horse')
        print(horse_id)
        bid_amount = float(request.data.get('amount'))
        user = request.user
        try:
            horse = Horse.objects.get(id=horse_id)
        except Horse.DoesNotExist:
            return Response({"error": "Horse not found."}, status=status.HTTP_404_NOT_FOUND)

        if  bid_amount < horse.current_bid:
            return Response({"error": "Bid must be higher than the current bid."}, status=status.HTTP_400_BAD_REQUEST)

        if bid_amount < horse.price:
            return Response({"error": "Bid must be higher than the starting Price."}, status=status.HTTP_400_BAD_REQUEST)
        if horse.auction_enddate< timezone.now().date():
            return Response({"error": "Auction is Ended"}, status=status.HTTP_400_BAD_REQUEST)
        bid = Bid(horse=horse, user=user, bid_amount=bid_amount)
        bid.save()

        # Update the current bid on the horse
        horse.current_bid = bid_amount
        horse.save()
        return Response({"msg": "Bid placed"}, status=status.HTTP_201_CREATED)

    def get(self,request,id,format=None):
        obj=Bid.objects.filter(horse_id=id).first()
        serializers=BiddetailSerializer(obj)
        return Response(serializers.data)