from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Horse,Bid,Blog



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
class HorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horse
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    pic = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    class Meta:
        model = Bid
        fields = ['pic','username','bid_amount', 'bid_time']

    def get_pic(self, obj):
        return obj.horse.pic.url
    def get_username(self, obj):
        return obj.user.username
    
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BiddetailSerializer(serializers.ModelSerializer):
    auction_startdate = serializers.SerializerMethodField()
    auction_enddate = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = Bid
        fields = ['auction_startdate', 'auction_enddate', 'username', 'bid_amount', 'bid_time']

    def get_auction_startdate(self, obj):
        return obj.horse.auction_startdate

    def get_auction_enddate(self, obj):
        return obj.horse.auction_enddate

    def get_username(self, obj):
        return obj.user.username