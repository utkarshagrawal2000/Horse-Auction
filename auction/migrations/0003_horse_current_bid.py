# Generated by Django 5.0.6 on 2024-07-10 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_horse_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='current_bid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
