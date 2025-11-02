from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    city = request.GET.get('city', 'New York')
    api_key = "5b5efdc438feedcfca776e51d57df214"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    weather_data = {}
    error_message = None

    # breakpoint()
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data.get('cod') != 200:
            raise Exception(f"City {city} not found")

        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'icon': data['weather'][0]['icon'],
        }
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors (404, 500, etc.) this way you can provide more specific messages based on status code
        if e.response.status_code == 404:
            error_message = f"City '{city}' not found. Please check the spelling."
        else:
            error_message = f"Error fetching weather data: {str(e)}"
    except requests.exceptions.RequestException as e:
        # Handle network errors this way you can inform the user about connectivity issues
        error_message = f"Network error: {str(e)}"
    except Exception as e:
        # Handle other errors
        error_message = f"An error occurred: {str(e)}" 

    return render(request, 'weather/index.html', {
        'weather_data': weather_data,
        'error_message': error_message})