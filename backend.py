import requests
import json

ip_API_key="c27bf991417a54acc12dee95b7eb4a8912478af2aad2a7a779de9dd1"
ip_url="https://api.ipdata.co/?api-key="+ip_API_key
location_response=requests.get(ip_url)
loc_to_json=location_response.json()

def get_user_latitude():
    latitude=loc_to_json['latitude']
    return latitude

def get_user_longitude():
    longitude=loc_to_json['longitude']
    return longitude

API_KEY="ebbd521303ecc9a32317e8f713c1c8b1"
address_url="https://api.openweathermap.org/data/2.5/onecall?lat="+str(get_user_latitude())+"&lon="+str(get_user_longitude())+"&exclude=current&appid="+API_KEY
response=requests.get(address_url)
response_to_json=response.json()

def convert_to_celsius(kelvin):
    celsius=int(kelvin-273.15)
    return celsius

for x in range(8):
    json_min_temp=convert_to_celsius(response_to_json['daily'][x]['temp']['min'])
    json_max_temp=convert_to_celsius(response_to_json['daily'][x]['temp']['max'])
    json_humidity=response_to_json['daily'][x]['humidity']
    json_wind_speed=response_to_json['daily'][x]['wind_speed']
    json_weather_desc=response_to_json['daily'][x]['weather'][0]['description']

    print('day '+str(x+1)+":")
    print('min temp: '+str(json_min_temp)+"ºC")
    print('max temp: '+str(json_max_temp)+"ºC")
    print('humidity: '+str(json_humidity)+"%")
    print('wind speed: '+str(json_wind_speed)+" m/s")
    print('weather desc: '+str(json_weather_desc))
    print()