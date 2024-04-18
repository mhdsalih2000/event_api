import aiohttp
import asyncio
import time
from .models import Event
from datetime import datetime, timedelta


async def get_weather_async(lat, lon, date):
    api_key = "a498aecd4c446332949b3d2b168d3b4d"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&date={date}&appid={api_key}&units=metric"

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                weather_data = await response.json()
                weather_description = weather_data['weather'][0]['description']
                temperature = weather_data['main']['temp']
                weather_str = f"{weather_description} {temperature}°C"
                return weather_str
            else:
                return 'Weather data not available'

# Example list of events (latitude and longitude)

specified_date = datetime.now().date()
end_date = specified_date + timedelta(days=40)
events = Event.objects.filter(date__range=[specified_date, end_date]).values( 'latitude', 'longitude')

async def main():
    start_time = time.time()
    for event in events:
        weather = await get_weather_async(event['latitude'], event['longitude'], '2024-04-03')
        print(f"Event Latitude: {event['latitude']}, Longitude: {event['longitude']}, Weather: {weather}")
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time} seconds")

# Run the async main function
asyncio.run(main())