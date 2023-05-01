import csv
from django.core.management.base import BaseCommand
from app_name.models import Phone


class Command(BaseCommand):
    help = 'Import phones from csv file'

    def handle(self, *args, **kwargs):
        with open('import_phone.csv', encoding='UTF8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                phone = Phone(
                    id=row['id'],
                    name=row['name'],
                    image=row['image'],
                    price=row['price'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists']
                )
                phone.save()