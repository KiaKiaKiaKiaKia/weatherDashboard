import datetime as dt
import requests
import questionary

BASE_URL = 'https://api.weatherapi.com/v1/current.json?'
API_KEY = open('api_key.txt', 'r').read()
favouriteCities = ['London', 'Toronto']

def menu():
    run = True
    while run == True:
        menuChoice = questionary.select(
            'Weather Menu:',
            choices = [
                'Enter city and view weather',
                'Manage favourited cities',
                'Exit',
            ]
        ).ask()

        match menuChoice:
            case 'Enter city and view weather':
                CITY = input('Enter a city to check the weather: ')
                display(CITY)
            case 'Manage favourited cities':
                cityChoice = questionary.select(
                    'Choose a city to view the weather',
                    choices = [
                        'Add favourite city',
                        'Unfavourite a city',
                        *favouriteCities, # * unpacks the list
                        ]
                ).ask()
                match cityChoice:
                    case 'Add favourite city':
                        addFaveCity(input('Enter city to favourite: '))
                    case 'Unfavourite a city':
                        removeFaveCity()
                    case default:
                        display(cityChoice)
            case 'Exit':
                run = False
            case default:
                print('Menu error.')

def display(CITY):
    url = BASE_URL + 'key=' + API_KEY + '&q=' + CITY
    raw_response = requests.get(url)

    if raw_response.status_code == 200:
        response = raw_response.json()

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
            
    else:
        print('Error retrieving weather. Please check the spelling.')

    input('Press any key to return to menu.')

def addFaveCity(city):
    if city not in favouriteCities:
            favouriteCities.append(city)
    else:
        print('Error: City is already favourited! Are you obsessed?')

def removeFaveCity():
    cityChoice = questionary.select(
        'Choose a city to unfavourite:',
        choices = favouriteCities
    ).ask()
    favouriteCities.remove(cityChoice)
    print(f'Removed {cityChoice} from favourites.')


menu()
