import csv
from django.core.management.base import BaseCommand
from ...models import Event
import os
from django.conf import settings

class Command(BaseCommand):
    
     
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):

        
        
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(base_dir)
        csv_file_path = os.path.join(base_dir, 'csv','data.csv')



        
        

        if os.path.exists(csv_file_path):
            with open(csv_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Event.objects.create(
                    event_name=row['event_name'],
                    city_name=row['city_name'],
                    date=row['date'],
                    time=row['time'],
                    latitude=row['latitude'],
                    longitude=row['longitude']
                )
            os.remove(csv_file_path)
            self.stdout.write(self.style.SUCCESS('Event Data imported successfully , CSV file Deleted SuccesFully'))
        else :
            self.stdout.write(self.style.ERROR('Events Data Imported Alredy , The file will Deleted Once the Data is Migrated in to DataBase'))
   
        
        
                
            
            