import requests

class RequestsApi:
    key = "key=c42eb3d5-0c68-4305-80db-3c7b76507a31"
    urlBase = "https://api.airvisual.com/v2/"    
    headers = {}

    @staticmethod
    def get_all_country_api():
        try:
            urlGetCountry = "countries?"
            response = requests.request("GET", RequestsApi.urlBase + urlGetCountry + RequestsApi.key)
            if response.status_code != 200:                
                return False
            else:       
                return response.json()
        except:
            return False

    @staticmethod
    def get_all_statesxcountry_api(country):
        try:
            urlGetStates = "states?country=" + country + "&"
            response = requests.request("GET", RequestsApi.urlBase + urlGetStates + RequestsApi.key)
            if response.status_code != 200:                
                return False
            else:   
                return response.json()
        except:
            return False



    @staticmethod
    def get_all_citiesxstatesxcountry_api(state, country):
        try:
            urlGetCities = "cities?state=" + state + "&country=" + country + "&"
            response = requests.request("GET", RequestsApi.urlBase + urlGetCities + RequestsApi.key)
            if response.status_code != 200:                
                return False
            else:   
                return response.json()
        except:
            return False


    @staticmethod
    def get_all_data_api(city, state, country):
        try:
            urlGetCityData = "city?city=" + city + "&state=" + state + "&country=" + country + "&"
            response = requests.request("GET", RequestsApi.urlBase + urlGetCityData + RequestsApi.key)
            if response.status_code != 200:                
                return False
            else:   
                return response.json()
        except:
            return False

