import django_filters
from .models import Horse

class HorseFilter(django_filters.FilterSet):
    class Meta:
        model = Horse
        fields = {
            'category': ['exact'],
            'sex': ['exact'],
            'age': ['exact'],
            'height': ['exact', 'lt', 'gt'],
            'colour': ['exact'],
            'breed': ['exact'],
            'location': ['exact'],
            'price': ['exact', 'lt', 'gt'],
            'auction_startdate': ['exact', 'gt'],
            'auction_enddate': ['exact', 'lt'],
        }
