"""
This script combines 2 APIs and allows you to receive an SMS notification for the nearest object passing our planet daily.
The data comes from NASA's Near-Earth Object Observations Program: https://www.nasa.gov/planetarydefense/neoo
The SMS API is from Messagebird: https://messagebird.com/en/
"""

import requests
from datetime import date
import messagebird


def findClosestEncounter(jd):
    # a simple function for discovering the nearest object for the day from all registered objects
    asteroids = []
    for i in range(0, len(jd)):
        asteroids.insert(i,jd[i]['close_approach_data'][0]['miss_distance']['kilometers'])
    return asteroids.index(min(asteroids))



#Settings and URL to conect to NASA API
#Get your free API key from here: https://api.nasa.gov/

ad_today = date.today().strftime("%Y-%m-%d")
url = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+ad_today+"&end_date="+ad_today+"&api_key=[your key]"


#Hadle the responce json
response = requests.request("GET", url)
response.encoding = 'utf-8'
jsn = response.json()


if "near_earth_objects" in jsn:
  

    base = jsn['near_earth_objects'][ad_today]
    i = findClosestEncounter(base)

    #extract the data we need to create the alert
    name = base[i]['name']
    to_appear = base[i]['close_approach_data'][0]['close_approach_date_full']
    how_close = base[i]['close_approach_data'][0]['miss_distance']['kilometers']
    dia_meter =  base[i]['estimated_diameter']['meters']['estimated_diameter_max']
   
   
    #format the data
    howclose = round(float(how_close))
    diameter = round(dia_meter)

    #build the message
    alert ="The nearest asteroid for today is "+ name+". It will be "+str(howclose)+" km away with a diameter of "+str(diameter)+" meters."
    
    #SMS client
    #Get your free API key from here: https://developers.messagebird.com/api/#api-endpoint
    sms = messagebird.Client("your API key here")

    #Prepare and send the message to a phone number of your choice.
    # Change the name "Asteroid" to something you want. It will appear as a sender
    message = sms.message_create(
        'Asteroid',
        '+yourphonenumner',
        alert,
        { 'reference' : 'Asteroid' }
    )
    
    #write to the console
    #print(alert)

else:
    #Some work is needed on this exception
    print("Something went wrong")
