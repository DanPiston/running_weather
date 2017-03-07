from pprint import pprint
import os
import webbrowser
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
        return '<img class="clothing-img" src="images/tshirt.png">'

    else:
        return '<img class="clothing-img" src="images/longsleeve.png">'


# Return what type of pants to where based on temp.
def pants(temp):
    if temp > 40:
        return '<img class="clothing-img" src="images/shorts.png">'

    else:
        return '<img class="clothing-img" src="images/sweatpants.png">'


# Daily Data
daily = r.json()['daily']['data']
pprint(daily[0])


def get_forcast(set_of_data):
    for x in set_of_data:
        date = get_readable_date(x['time'])
        max_temp = x['temperatureMax']
        print(f"""
{date} - High of {max_temp}{degree_sign}. Wear:
         Upper: {shirt(max_temp)}
         Lowers: {pants(max_temp)}""")

today = daily[0]['apparentTemperatureMax']
tomorrow = daily[1]['apparentTemperatureMax']
tomorrow_one = daily[2]['apparentTemperatureMax']
print(today)

# The main page layout and title bar
main_page_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Run Wear Suggester</title>
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/main.css">
</head>

  <body>
      <div class="container">
        <div class="row text-center">
            <div class="col-md-12">
                <h1>Clothing Suggestions</h1>
            </div>
        </div>

        <div class="row text-center">
            <div class="col-md-4">
                <h2>Today</h2>
                <h4>{today}{degree_sign}</h4>
                {shirt(today)}
                {pants(today)}
            </div>  
            <div class="col-md-4">
                <h2>Tomorrow</h2>
                <h4>{tomorrow}{degree_sign}</h4>
                {shirt(tomorrow)}
                {pants(tomorrow)}
            </div>  
            <div class="col-md-4">
                <h2>Tomorrow + 1</h2>
                <h4>{tomorrow_one}{degree_sign}</h4>
                {shirt(tomorrow_one)}
                {pants(tomorrow_one)}
            </div>  
      </div>
  </body>
</html>
'''

def write_html():
    output_file = open('clothing.html', 'w')
    output_file.write(main_page_content)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

write_html()
