import random
from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        # Clear existing listings first
        Listing.objects.all().delete()

        # Get some existing users (hosts)
        hosts = User.objects.filter(role='host')
        if not hosts.exists():
            self.stdout.write(self.style.ERROR('No hosts found. Create users with role="host" first.'))
            return

        sample_listings = [
            {
                'title': 'Cozy Mountain Cabin',
                'description': 'A cozy cabin in the mountains with stunning views.',
                'location': 'Aspen, CO',
            },
            {
                'title': 'Downtown City Apartment',
                'description': 'Modern apartment located in the heart of the city.',
                'location': 'New York, NY',
            },
            {
                'title': 'Beachfront Bungalow',
                'description': 'Relaxing bungalow steps from the beach.',
                'location': 'Miami, FL',
            },
            {
                'title': 'Countryside Cottage',
                'description': 'Charming cottage surrounded by nature.',
                'location': 'Nashville, TN',
            },
            {
                'title': 'Luxury Penthouse Suite',
                'description': 'Experience luxury in this spacious penthouse.',
                'location': 'Los Angeles, CA',
            },
        ]

        created = 0
        for listing_data in sample_listings:
            owner = random.choice(hosts)
            Listing.objects.create(
                owner=owner,
                title=listing_data['title'],
                description=listing_data['description'],
                location=listing_data['location'],
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created} sample listings.'))
