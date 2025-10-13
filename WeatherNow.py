import requests

# --- API CONFIGURATION ---
API_KEY = "35e4afc4ee31a5903eff497df13d828b" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY_NAME = "Kanpur,IN" 

def get_weather_data(query, speak):

    final_url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY_NAME + "&units=metric"
    try:
        response = requests.get(final_url)
        response.raise_for_status() 
        data = response.json()
        
        if data.get("cod") == 200:
            temp_celsius = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            city = CITY_NAME.split(',')[0]

            if "temperature" in query:
                speak(f"The current temperature in {city} is {temp_celsius} degrees Celsius.")
            elif "weather" in query:
                speak(f"The weather in {city} is currently {weather_desc}, with a temperature of {temp_celsius} degrees Celsius.")
        else:
            speak(f"Sorry sir, I couldn't get the weather data. The service returned a status code {data.get('cod')}.")
            
    except requests.exceptions.RequestException:
        speak("I'm sorry sir, I can't connect to the weather service right now.")
    except KeyError:
        speak("I retrieved the data, sir, but it seems to be in an unexpected format.")