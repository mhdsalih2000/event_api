from rest_framework import serializers
from .models import Event ,CSVfile





class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'event_name', 'city_name', 'date']



class csvSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVfile
        fields =['csv_file','file_name']
