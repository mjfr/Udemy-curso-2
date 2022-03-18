from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import datetime as dt

target_date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/"
SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = "http://127.0.0.1:9090"
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.current_user()["id"]
PLAYLIST_ID = ""
hot_100 = []
song_list = []

try:
    response = requests.get(url=f"{URL}{target_date}")
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("Something went wrong with the date. Using a random date.")
    today = dt.date(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day)
    starting_date = dt.date(1958, 8, 1)  # +/- a data limite do Billboard
    time_between_dates = starting_date - today
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(abs(days_between_dates))
    target_date = str(starting_date + dt.timedelta(days=random_number_of_days))
    print(target_date)
    response = requests.get(url=f"{URL}{target_date}")
    response.raise_for_status()

markup = response.text
soup = BeautifulSoup(markup=markup, parser="html.parser")
PLAYLIST_NAME = f"{target_date} Billboard top 100"

for item in soup.select(selector="div ul li ul li", class_="c-title"):
    try:
        track = item.select_one("h3").getText().strip()
        artist = item.select_one("span").getText().strip()
    except AttributeError:
        continue
    hot_100.append({"track": track, "artist": artist, "year": target_date.split("-")[0]})

playlist = sp.user_playlist_create(user_id, PLAYLIST_NAME, public=False, collaborative=False,
                                   description=f"A playlist created using Python to web scrape Billboard to get all top"
                                               f" 100 songs from {target_date}. It is just a test and a learning"
                                               " experience.")

for search in hot_100:
    result = sp.search(q=f"track:{search['track']} artist:{search['artist']} year:{search['year']}",
                       type="track,artist", market=None)
    try:
        song_list.append(result['tracks']['items'][0]['external_urls']['spotify'])
    except IndexError:
        print(f"Track: '{search['track']}' is probably not on Spotify")

if len(song_list) > 0:
    try:
        sp.playlist_add_items(playlist_id=playlist["id"], items=song_list, position=None)
    except Exception as message_error:
        print(message_error)
else:
    print("No songs were added.")
