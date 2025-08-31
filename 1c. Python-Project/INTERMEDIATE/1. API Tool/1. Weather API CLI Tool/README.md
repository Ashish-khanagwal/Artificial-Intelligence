<h1 align=center>API HANDLING</h1>

# Weather Info CLI Tool

### 1. Sign Up and Get API Key

- Go to OpenWeatherMap and create a free account.
- After signing up, get your API key from your account dashboard.

### 2. Install the Required Module

If you don’t have it, install the requests module:

```
pip install requests
```

### 3. Import the module

```
import requests
```

## Secure Ways to Handle API Keys

### 1. Use Environment Variables

- Store your API key in an environment variable on your computer.
  Access it in Python with:

```
import os
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
```

Set the environment variable in your OS or a .env file.

### 2. Use a Separate Config File

Store credentials in a file like config.py:

```
API_KEY = 'your-actual-api-key'
```

Import in your script:

```
from config import API_KEY
```

Add config.py to .gitignore to keep it out of source control.

### 3. Why This Matters

- Keeps your keys private and secure.
- Prevents accidental exposure on public repositories.
- Makes it easier to change keys without modifying source code.

## Make an API Request in Python

```
import requests
from config import API_KEY

BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"
city = input("Enter the city name: ")

params = {"q": city, "appid": API_KEY, "units": "metric"}

try:
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    main = data["main"]
    weather = data["weather"][0]
    print(
        f"Weather in {city}: {weather['description']},\n"
        f"Temperature: {main['temp']}°C,\n"
        f"Humidity: {main['humidity']}%"
    )
except requests.exceptions.HTTPError:
    print("City not found or API error occurred.")
except Exception as e:
    print("Error:", e)
```

## CODE EXPLANATION

### request handling

```
requests.get(url, params={key: value}, args)
```

- `url` : Required. The url of the request
- `params` : Optional. A dictionary, list of tuples or bytes to send as a query string.
  Default `None`

Example:

```
https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
```

#### `?q`

- Meaning:
  ?q= is a common query string parameter in URLs, often used in web APIs and search URLs.

Usage:

- The `?` marks the beginning of the query string in a URL.
- `q` typically stands for "query" (e.g., the search term or question being asked).

Example:

```
https://api.example.com/search?q=python
```

Here, the parameter `q` has the value "python" — meaning the user is searching for "python".

Common use cases:

- Web searches (e.g., Google: https://www.google.com/search?q=weather)
- API requests that require input or a search term

#### `&appid=`

Meaning:
`&appid=` is another query parameter in URLs, usually used to specify an application ID or API key for authentication.

Usage:

- The `&` is used to add additional parameters after the first one in the query string.
- `appid` stands for "application ID" or API key/token required by many APIs to identify who is making the request.

Example:

```
https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY
```

Here, `appid` is set to YOUR_API_KEY for authentication, after the `q` (query term) parameter.

Common use cases:

- Required by APIs like OpenWeatherMap, financial APIs, or any service where access must be controlled or tracked.

#### `"units": "metric"`

What does `'units': 'metric'` mean?

- This is a key-value pair used in API query parameters, often when requesting data from services like weather APIs.
- The key is 'units' and the value is 'metric'.

Why use `'units': 'metric'`?

- Many APIs (especially weather APIs like OpenWeatherMap) allow you to specify in which measurement system you want the data.
- `'metric'` means you want responses in metric units:
  - Temperature in Celsius (°C)
  - Wind speed in meters per second (m/s)
  - Precipitation in millimeters (mm)

- `'imperial'` gives you US units:
  - Temperature in Fahrenheit (°F)
  - Wind speed in miles per hour (mph)

## Getting and Processing a response from an API using Python’s `requests` library

```
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    main = data["main"]
    weather = data["weather"][0]
```

### 1. `response.raise_for_status()`

#### Purpose:

- Checks if the HTTP response was successful (status code 200–299).
- If there was an HTTP error (like 404 or 500), it raises an exception (requests.exceptions.HTTPError), which helps catch problems immediately instead of working with bad or incomplete data.

#### Use case:

- Ensures you only proceed if the request to the API was successful.

### 2. `data = response.json()`

#### Purpose:

- Converts the JSON content of the response into a Python dictionary.

#### Use case:

- API responses are commonly in JSON format; this line parses that JSON for further processing.

### 3. `main = data['main']`

#### Purpose:

- Retrieves the value associated with the key "main" in the dictionary data.

#### Use case:

- In many APIs (e.g., OpenWeatherMap), the "main" key contains important information—often a sub-dictionary with data like temperature, humidity, etc.

### 4. `weather = data['weather']`

#### Purpose:

- Accesses the first item in the list associated with the "weather" key in data.

#### Use case:

- "weather" is typically a list of weather conditions (even if there’s just one entry); `` selects the first condition to extract details like description, icon, etc.

Example of what the JSON structure might look like:

```
{
  "main": {"temp": 27.5, "humidity": 70},
  "weather": [
    {"description": "clear sky", "icon": "01d"}
  ]
}
```

- `main = data['main']` will be `{'temp': 27.5, 'humidity': 70}`
- `weather = data['weather']` will be `{'description': 'clear sky', 'icon': '01d'}`
