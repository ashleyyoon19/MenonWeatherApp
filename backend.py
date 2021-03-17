import requests
import json
import pandas as pd

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

def convert_to_celsius(kelvin):
    celsius=int(kelvin-273.15)
    return celsius

API_KEY="ebbd521303ecc9a32317e8f713c1c8b1"
address_url="https://api.openweathermap.org/data/2.5/onecall?lat="+str(get_user_latitude())+"&lon="+str(get_user_longitude())+"&exclude=current&appid="+API_KEY
response=requests.get(address_url)
response_to_json=response.json()

#creating empty data frame
pd.set_option('display.max_columns', None)
weather_df=pd.DataFrame()

#creating empty lists to store JSON Data
day=0
list_of_day=[]
min_temp=[]
max_temp=[]
humidity=[]
wind_speed=[]
weather_desc=[]

#write + add json data to lists to DataFrame
for num in response_to_json['daily']:
    weather_df['Day']=day
    list_of_day.append(day)
    
    min_temp.append(convert_to_celsius(response_to_json['daily'][day]['temp']['min']))
    max_temp.append(convert_to_celsius(response_to_json['daily'][day]['temp']['max']))
    humidity.append(response_to_json['daily'][day]['humidity'])
    wind_speed.append(response_to_json['daily'][day]['wind_speed'])
    weather_desc.append(response_to_json['daily'][day]['weather'][0]['description'])
    
    day+=1

#putting data into dataframe
weather_df['Day']=list_of_day
weather_df['Min. Temp (ºC)']=min_temp
weather_df['Max. Temp (ºC)']=max_temp
weather_df['Humidity']=humidity
weather_df['Wind Speed']=wind_speed
weather_df['Description']=weather_desc

print(weather_df)

day_val = input("Enter the day number you want to filter the results by (0 - 7):")

'''
pd.set_option('display.max_columns', None)
weather_df_filtered=pd.DataFrame()


#putting data into dataframe
weather_df_filtered['Day']=day_val
weather_df_filtered['Min. Temp (ºC)']= min_temp[int(day_val)]
weather_df_filtered['Max. Temp (ºC)']= max_temp[int(day_val)]
weather_df_filtered['Humidity']= humidity[int(day_val)]
weather_df_filtered['Wind Speed']= wind_speed[int(day_val)]
weather_df_filtered['Description']= weather_desc[int(day_val)]
'''

filtered = {'Day' : [day_val],
        'Min. Temp (ºC)' : [min_temp[int(day_val)]],
        'Max. Temp (ºC)' : [max_temp[int(day_val)]],
        'Humidity' : [humidity[int(day_val)]],
        'Wind Speed' : [wind_speed[int(day_val)]],
        'Description' : [weather_desc[int(day_val)]]
        }

weather_df_filtered = pd.DataFrame(filtered, columns = ['Day', 'Min. Temp (ºC)', 'Max. Temp (ºC)', 'Humidity', 'Wind Speed', 'Description'])

print("Your filtered table is:")
print(weather_df_filtered)

