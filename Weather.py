import requests

#replace "API_KEY" with your own OpenWeatherMap API key.
API_KEY = "API_KEY"

#The base URL for the OpenWeatherMap current weather
base_url = "http://api.openweathermap.org/data/2.5/weather"

def weather_by_zip(zip_code):
    #fetches and displays weather for given zip code

    #constructs the full URL with zip code, country, and API key
    params = {
        'zip': f'{zip_code},us' , #adds the country code for US 
        'appid' : API_KEY, 
        'units' : 'imperial' #displays in Farenheit, change to metric for Celcius
    }

    try:
        response = requests.get(base_url, params=params)
        #Raise and excpetion for error, such as 404 Not Found
        response.raise_for_status()
        data =  response.json()

        #Checks if the API returns a 404 error
        if data["cod"] == 404:
            print(f'Error: Weather data for zip code {zip_code} not found.')
            return
        
        #extracts the relevant data from the JSON response
        city = data["name"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather_description = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]

        #displays the results
        print("\n--- Weather Report ---")
        print(f"City: {city}")           
        print(f"Temperature: {temp} °F")
        print(f"Feels Like: {feels_like} °F")
        print(f"Weather: {weather_description}")
        print(f"Humidity: {humidity}%")
        print("----------------------\n")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError:
        print("Error: Invalid API Response format.")


#Main Function

if __name__ == "__main__":
    while True:
        user_zip = input("Enter a US zip code or 'quit' to exit: ")
        if user_zip.lower() == 'quit':
            break

        #validation for a 5 digit zip code
        if user_zip.isdigit() and len(user_zip) == 5:
            weather_by_zip(user_zip)
        else:
            print("Invalid input. Please enter a 5 digit US zip code.")
            