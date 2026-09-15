import datetime as dt
import requests
import questionary

BASE_URL = 'https://api.weatherapi.com/v1/current.json?'
API_KEY = open('api_key.txt', 'r').read()
favouriteCities = []

def menu():
    run = True
    while run == True:
        menuChoice = questionary.select(
            'Weather Menu:',
            choices = [
                'Enter city and view weather',
                'Favourited cities',
                'Edit preferences',
                'Exit',
            ]
        ).ask()
        match menuChoice:
            case 'Enter city and view weather':
                CITY = input('Enter a city to check the weather: ')
                display(CITY)
                pass
            case 'Favourited cities':
                pass
            case 'Edit preferences':
                pass
            case 'Exit':
                run = False
            case default:
                print('Menu error.')

def display(CITY):
    url = BASE_URL + 'key=' + API_KEY + '&q=' + CITY
    response = requests.get(url).json()

    location = response['location']['name']
    local_datetime = response['location']['localtime']
    temp_c = response['current']['temp_c']
    temp_f = response['current']['temp_f']
    feels_temp_c = response['current']['feelslike_c']
    feels_temp_f = response['current']['feelslike_f']
    condition = response['current']['condition']['text']
    wind_mph = response['current']['gust_mph']
    wind_kph = response['current']['gust_kph']
    rain_chance = response['current']['chance_of_rain']
    snow_chance = response['current']['chance_of_snow']

    print(f'Location: {location}')
    print(f'Local date & time: {local_datetime}')
    print(f'Temp: {temp_c}°C / {temp_f}°F')
    print(f'Feels like: {feels_temp_c}°C / {feels_temp_f}°F')
    print(f'Weather: {condition}')
    print(f'Wind: {wind_mph}mph / {wind_kph}kph')
    print(f'Chance of rain: {rain_chance}%')
    print(f'Chance of snow: {snow_chance}%')

    favouriteChoice = questionary.select(
        'Favourite this city?',
        choices = [
            'Yes',
            'No',
        ]
    ).ask()
    if favouriteChoice == 'Yes':
        favouriteCities.append(CITY)

    input('Press any key to return to menu.')

menu()
