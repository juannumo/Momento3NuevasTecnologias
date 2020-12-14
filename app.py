import requests
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
from api.requests_api import RequestsApi


app = Flask(__name__)
app.secret_key = "key123"


@app.route('/')
def index():
    res = RequestsApi.get_all_country_api()  
    count = len(res['data'])
    valInit = 1
    return render_template('layouts/index.html', countries = res['data'], countCountries = count, valInit = valInit)


@app.route('/viewStates/<country>')
def view(country):
    res = RequestsApi.get_all_statesxcountry_api(country)    
    return render_template('layouts/supportedStates.html', states = res['data'], country = country)



@app.route('/cities/<state>/<country>')
def viewCity(state, country):
    res = RequestsApi.get_all_citiesxstatesxcountry_api(state, country)      
    return render_template('layouts/supportedCities.html', cities = res['data'], state = state, country = country)


@app.route('/data/<city>/<state>/<country>')
def viewData(city, state, country):
    res = RequestsApi.get_all_data_api(city, state, country) 
    Datetime = res['data']['current']['weather']['ts']
    Temperature = res['data']['current']['weather']['tp']
    Atmospheric = res['data']['current']['weather']['pr']
    Humidity = res['data']['current']['weather']['hu']
    WindS = res['data']['current']['weather']['ws']
    WindD = res['data']['current']['weather']['wd']
    return render_template('layouts/data.html', datos = res['data'], city = city, state = state, country= country, coodinates = str(res['data']['location']['coordinates']), Datetime=Datetime, Temperature=Temperature, Atmospheric=Atmospheric, Humidity=Humidity, WindS=WindS, WindD=WindD, pollution=res['data']['current']['pollution'])


@app.route('/about')
def about():    
    return render_template('layouts/about.html')

@app.route('/health')
def health():    
    return render_template('layouts/countryHealth.html')




if __name__ == '__main__':
    app.run(debug=True)



