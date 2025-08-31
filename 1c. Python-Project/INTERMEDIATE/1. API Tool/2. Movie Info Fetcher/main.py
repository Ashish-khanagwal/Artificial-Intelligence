import os

import requests
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env into environment

api_key = os.getenv("API_KEY")  # Fetch API_KEY from environment
base_url = "http://www.omdbapi.com"

title = input("Enter the title of the movie: ")

params = {"t": title, "apikey": api_key}

try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()

    if data.get("Response") == "True":
        name = data.get("Title")
        year = data.get("Year")
        genre = data.get("Genre")
        plot = data.get("Plot")
        ratings = data.get("Ratings", [])
        imdb_rating = None
        for rating in ratings:
            if rating.get("Source") == "Internet Movie Database":
                imdb_rating = rating.get("Value")
                break
        print(
            f"Title: {name}\nReleased in: {year}\nGenre: {genre}\nPlot: {plot}\nIMDB Ratings: {imdb_rating}"
        )
    else:
        print("Movie not found or API error occurred:", data.get("Error"))

except requests.exceptions.HTTPError:
    print("HTTP error occurred.")
except Exception as e:
    print("Some error occurred:", e)
