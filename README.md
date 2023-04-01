# smhi-cli
Script to fetch weather data from SMHI (Swedish Meteorological and Hydrological Institute) in a CLI 
https://opendata.smhi.se/apidocs/metobs/index.html

Requirements: Python 3.10.6 or higher 

Start by adding the coordinates for the weather observation,
the name you assign in "city name" is the name you'll have to type in when running the script. 

```
 cities = {
        "City name":        (latitude, longitude),
}
```

Input is case-sensitve so make sure you spell it exactly as in the dictionary. 
Feel free to modify or improve!

Run script: 
```
./smhi.py 
```
Enter city and then press enter

```
> Malmö
8.2°C 4.8m/s 0.0mm/h
```
