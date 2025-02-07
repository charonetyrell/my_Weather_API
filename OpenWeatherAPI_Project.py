import requests

#Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
API_KEY = '4a4b0d67846fa5eb5362e8c6dd135d9c'

def test_retrieve_current_weather_by_city_name_positive():
    city = 'London' #Input valid city name
    expected_status_code = 200

    #Construct the API URL for the specified city
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    #Send a GET request to the API
    response = requests.get(url)

#Add a validation in a try/except block to handle our exceptions
    try:
        #Verify response status code
        assert response.status_code == expected_status_code, f"Expected status code: {expected_status_code}, Actual status code: {response.status_code}"

        #Parse the JSON reponse
        data = response.json()

        #Verify the city name in the response
        assert data['name'] == city, f"Expected city: {city}, Actual city: (data['name'])"

        #Verify presence of weather information
        assert 'weather' in data, "Weather information not found in response"

        #Verify presence of main temperature information
        assert 'main' in data, "Main temperature information not found in response"

        #Print weather data for verification
        print("Weather data for", city)
        print("Weather Description:", data['weather'][0]['description'])
        print("Temperature:", data['main']['temp'], "C") 

    except AssertionError as e:
        print("Assertion Error:", e)

def test_retrieve_current_weather_invalid_city_name_negative():
    city = 'Abcdefgh' #Input: Invalid city name
    expected_status_code = 404

    #Construct the API URL for the specified city
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    #Send a GET request to the API
    response = requests.get(url)

    try:
        #Verify response code
        assert response.status_code == expected_status_code, f"Expected status code: {expected_status_code}, Actual status code: {response.status_code}"

        #Parse the JSON response
        data = response.json()

        #Verify error message in the response
        assert data['message'] == 'city not found', f"Expected error message: 'city not found', Actual error message: {data['message']}"

        #Print error message for verification
        print("Error message:", data['message'])

    except AssertionError as e:
        print("Assertion Error:", e)

#Run the positive tests
print("Positive Test Scenarios:")
print("------------------------")
test_retrieve_current_weather_by_city_name_positive()

#Run the negative tests
print("\nNegative Test Scenarios:")
print("--------------------------")
test_retrieve_current_weather_invalid_city_name_negative()
