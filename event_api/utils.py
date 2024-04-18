
from asgiref.sync import sync_to_async
from rest_framework.response import Response
import asyncio
import aiohttp
from .models import Event
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class Service:
    pagination_class = CustomPagination  


    async def get_weather_async(self,session, lat, lon, date):
        api_key = "a498aecd4c446332949b3d2b168d3b4d"
        api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&date={date}&appid={api_key}&units=metric"
        async with session.get(api_url) as response:
            if response.status == 200:
                weather_data = await response.json()
                weather_description = weather_data['weather'][0]['description']
                temperature = weather_data['main']['temp']
                weather_str = f"{weather_description} {temperature}°C"
                return weather_str
            else:
                return 'Weather data not available'

    async def fetch_all_weather(self, locations,date):
        async with aiohttp.ClientSession() as session:
            tasks = [self.get_weather_async(session, event['latitude'], event['longitude'],date ) for event in locations]
            results = await asyncio.gather(*tasks)
        return results
    
    
    
    async def get_distance_async(self,latitude1, longitude1, latitude2, longitude2):
        api_key = "IAKvV2EvJa6Z6dEIUqqd7yGAu7IZ8gaH-a0QO6btjRc1AzFu8Y3IcQ=="  # API key
        api_url = f"https://gg-backend-assignment.azurewebsites.net/api/Distance?code={api_key}&latitude1={latitude1}&longitude1={longitude1}&latitude2={latitude2}&longitude2={longitude2}"
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
            # Check if the request was successful (status code 200)
                if response.status == 200:
                    data = await response.json()
                    distance = data.get('distance')
                    return distance
                else:
                # Print an error message if the request was not successful
                    print(f"Error: {response.status} - {await response.text()}")
                    return None
    @sync_to_async            
    def get_total_events(self, start_date, end_date):
        return Event.objects.filter(date__range=(start_date, end_date)).count()

    @sync_to_async    
    def get_data(self, page_number, request,start_date, end_date):
        events = Event.objects.filter(date__range=(start_date, end_date)).values('event_name', 'city_name', 'date', 'latitude', 'longitude')
        
        paginator = self.pagination_class()
        paginated_events = paginator.paginate_queryset(events, request)

        

        return paginated_events
