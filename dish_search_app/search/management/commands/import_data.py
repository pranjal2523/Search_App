import csv
from django.core.management.base import BaseCommand
from search.models import Dish

class Command(BaseCommand):
    help = 'Imports data from the CSV file into the SQLite database'

    def handle(self, *args, **options):
        with open('restaurants_small.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row['name']
                Dish.objects.create(name=dish_name)
        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))
