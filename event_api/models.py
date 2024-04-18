from django.db import models

# Create your models here.

from django.db import models

class CSVfile(models.Model):
    file_name =models.CharField(max_length=255, db_index=True)
    csv_file = models.FileField() 

    def __str__(self):
        return self.file_name 
    
    indexes = [
            models.Index(fields=['file_name'])
        ]



class Event(models.Model):
    event_name = models.CharField(max_length=255, db_index=True)
    city_name = models.CharField(max_length=100, db_index=True)
    date = models.DateField(db_index=True)
    time = models.TimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6,db_index=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,db_index=True)

    def __str__(self):
        return self.event_name  
    
    class Meta:
        indexes = [
            models.Index(fields=['event_name']), 
            models.Index(fields=['city_name', 'date']), 
            models.Index(fields=['latitude', 'longitude']),  
        ]
