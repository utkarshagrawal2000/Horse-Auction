from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Horse(models.Model):
    CATEGORY_CHOICES = [
        ('Horses & Ponies', 'Horses & Ponies'),
        ('All Rounders', 'All Rounders'),
        ('Broodmares', 'Broodmares'),
        ('Dressage', 'Dressage'),
        ('Driving', 'Driving'),
        ('Eventers', 'Eventers'),
        ('Ex Race Horses', 'Ex Race Horses'),
    ]
    AGE_CHOICES = [
        ('Foal', 'Foal'),
        ('Yearling', 'Yearling'),
        ('Adult', 'Adult'),
        ('Senior', 'Senior'),
        
    ]
    COLOUR_CHOICES = [
        ('Bay', 'Bay'),
        ('Chestnut', 'Chestnut'),
        ('Grey', 'Grey'),
        ('Black', 'Black'),
        
    ]
    BREED_CHOICES = [
        ('Thoroughbred', 'Thoroughbred'),
        ('Arabian', 'Arabian'),
        ('Quarter Horse', 'Quarter Horse'),
        ('Other', 'Other'),
        
    ]
    LOCATION_CHOICES = [
        ('USA', 'USA'),
        ('Canada', 'Canada'),
        ('Europe', 'Europe'),
        ('Other', 'Other'),
        
    ]
    SEX_CHOICES = [('Male', 'Male'), ('Female', 'Female')]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    age = models.CharField(max_length=20, choices=AGE_CHOICES)
    height = models.FloatField()
    colour = models.CharField(max_length=20,choices=COLOUR_CHOICES)
    breed = models.CharField(max_length=50,choices=BREED_CHOICES)
    description=models.CharField(max_length=800,null=True,blank=True)
    location = models.CharField(max_length=50,choices=LOCATION_CHOICES)
    contact = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    pic= models.ImageField(upload_to='products/', null=True, blank=True)
    auction_startdate = models.DateTimeField()
    auction_enddate = models.DateField()
    current_bid=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)

    def __str__(self):
        return f"{self.category} - {self.price}"

class Bid(models.Model):
    horse = models.ForeignKey(Horse, related_name='bids', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-bid_amount']

    def __str__(self):
        return f"{self.user.username} - {self.bid_amount}"

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    published_date = models.DateField()

    def __str__(self):
        return self.title