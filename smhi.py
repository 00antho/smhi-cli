#!/usr/bin/env python3
import requests
import json



def start():
    cities = {
        "Malmö":        (55.6049, 13.0038),
        "Öland":        (56.6659, 16.6393),
        "Lerum":        (57.7786, 12.3006),
        "Göteborg":     (57.7009, 11.7537)

    }




    pick = input("")

    if pick in cities: 
        
        try: 
            lat, lon = cities[pick]    
        
        except KeyError: 
            print("Sorry")
            
        response = requests.get(f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json')
        data = response.json()['timeSeries'][0]['parameters']
        print(f"Status: {response.status_code}")
            
        temp = data[10]['values'][0]
        wind = data[14]['values'][0]
        rain = data[3]['values'][0]
        
        print(f"{temp}°C {wind}m/s {rain}mm/h")
        
    else:
        start()


if __name__ == '__main__':
    start()    