from rest_framework import status
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .models import CSVfile, Event
from .serializers import csvSerializer
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache
import csv
from io import TextIOWrapper
from datetime import datetime, timedelta
from .models import Event
from adrf.viewsets import ViewSet
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework import status
import asyncio
from .utils import Service
import math


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class create_csv(CreateAPIView):
    queryset = CSVfile.objects.all()
    serializer_class = csvSerializer

    def post(self, request, *args, **kwargs):
        if 'csv_file' not in request.FILES:
            return Response({'error': 'No CSV file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        csv_file = request.FILES['csv_file']
        file_name = csv_file.name

        data = {'csv_file': csv_file, 'file_name': file_name}
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            import_result = self.import_csv_to_database()
            return Response({'message': 'CSV file uploaded and processed successfully', 'import_result': import_result}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def import_csv_to_database(self, *args, **kwargs):
        csv_file_obj = CSVfile.objects.first()
        if not csv_file_obj:
            return "No CSV file found"
        
        file_field = csv_file_obj.csv_file
        try:
            with file_field.open('rb') as csv_file:
                csv_reader = csv.DictReader(TextIOWrapper(csv_file, 'utf-8'))
                for row in csv_reader:
                    Event.objects.create(
                        event_name=row.get('event_name'),
                        city_name=row.get('city_name'),
                        date=row.get('date'),
                        time=row.get('time'),
                        latitude=row.get('latitude'),
                        longitude=row.get('longitude')
                    )
                return "CSV data imported successfully"
        except Exception as e:
            return f"Error importing CSV data: {str(e)}"



class AsyncView(ViewSet):
    async def get(self, request):
        user_latitude = request.query_params.get("latitude")
        user_longitude = request.query_params.get("longitude")
        requested_date_str = request.query_params.get("date")

        if not requested_date_str:
            specified_date = datetime.now().date()
        else:
            try:
                specified_date = datetime.strptime(requested_date_str, '%Y-%m-%d').date()
            except ValueError:
                return Response({'error': 'Invalid date format. Please provide date in YYYY-MM-DD format.'}, status=status.HTTP_400_BAD_REQUEST)

        if not (user_latitude and user_longitude):
            return Response({'error': 'User Latitude and Longitude are required.'}, status=status.HTTP_400_BAD_REQUEST)

        end_date = specified_date + timedelta(days=14)

        # Instantiate the Service class
        service = Service()

        async def fetch_distance_async(event):
            return await service.get_distance_async(event['latitude'], event['longitude'], user_latitude, user_longitude)

        # Call the get_data method with page_number
        page_number = request.query_params.get('page', 1)
        if not page_number:
            page_number =1    
        
        locations = await service.get_data(page_number, request, specified_date, end_date)
        distances = await asyncio.gather(*[fetch_distance_async(event) for event in locations])
        weather_results = await service.fetch_all_weather(locations, specified_date)

        # Integrate weather data and distances into event objects and create data_list
        data_list = []
        for i, event in enumerate(locations):
            data_list.append({
                'event_name': event['event_name'],
                'city_name': event['city_name'],
                'date': event['date'],
                'weather': weather_results[i],
                'distance': distances[i]
            })

        total_events = await service.get_total_events(specified_date, end_date)
        page_size = len(locations)
        total_pages = math.ceil(total_events / page_size)

        pagination_info = {
            'page': int(page_number),
            'pageSize': page_size,
            'totalEvents': total_events,
            'totalPages': total_pages
        }

        return Response({'events': data_list, 'pagination': pagination_info})
