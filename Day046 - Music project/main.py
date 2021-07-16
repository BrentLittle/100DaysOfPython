from bs4 import BeautifulSoup
import requests

import spotipy
from spotipy.oauth2 import SpotifyOAuth

BASEURL = "https://www.billboard.com/charts/hot-100/"


date = input("Type in a date in the following format, YYY-MM-DD:")


response = requests.get(f"{BASEURL+date}")
webpage = response.text

soup = BeautifulSoup(webpage,"html.parser")

titles = [song.getText() for song in soup.find_all(name="span", class_="chart-element__information__song")]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="a6c89c87d3024b8c939aa26e5b4bc974",
        client_secret= "", #CLIENT SECRET CODE HERE
        show_dialog=True,
        cache_path="token.txt"
    )
)


userId = sp.current_user()["id"]


songURIs = []
year = date.split("-")[0]
for name in titles:
    result = sp.search(q=f"track:{name} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songURIs.append(uri)
    except IndexError:
        print(f"{name} doesn't exist in Spotify. Skipped.")



playlist = sp.user_playlist_create(user=userId, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=songURIs)