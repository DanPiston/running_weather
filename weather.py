import datetime
import requests
import config


# Variables used to generate data.
url = "https://api.darksky.net/forecast/"
key = config.key
telford = "/40.3251,-75.3282"
degree_sign = u'\N{DEGREE SIGN}'


# set up request
r = requests.get(f'{url}{key}{telford}')


# Take unix time from json and convert to a human readable format
def get_readable_time(start_time):
    human_time = datetime.datetime.fromtimestamp(start_time)
    new_time = human_time.strftime("%m-%d %H:%M")
    return new_time


def get_readable_date(start_date):
    human_date = datetime.datetime.fromtimestamp(start_date)
    new_date = human_date.strftime("%m/%d")
    return new_date


# Return what type of shirt to where based on temp.
def shirt(temp):
    if temp > 40:
        return 'T-shirt'

    elif temp < 40 and temp > 25:
        return 'Long Sleeved Shirt'

    else:
        return "Layers"


# Return what type of pants to where based on temp.
def pants(temp):
    if temp > 40:
        return 'Shorts'

    elif temp < 40 and temp > 25:
        return 'Leggings and Shorts'

    else:
        return "Layers"


# Daily Data
daily = r.json()['daily']['data']


def get_forcast(set_of_data):
    for x in set_of_data:
        date = get_readable_date(x['time'])
        max_temp = x['temperatureMax']
        print(f"""
{date} - High of {max_temp}{degree_sign}. Wear:
         Upper: {shirt(max_temp)}
         Lowers: {pants(max_temp)}""")


get_forcast(daily)
