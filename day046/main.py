import os
import json
import spotipy
import requests
from bs4 import BeautifulSoup as soup
from spotipy.oauth2 import SpotifyOAuth

print("Create a Spotify playlist of the Hot 100 songs from any date!\n")
when = input("When? (YYYY-MM-DD): ")

print("\nDownloading list of songs from the billboard charts...", end="")
hot100 = f"https://www.billboard.com/charts/hot-100/{when}"
response = requests.get(hot100)
response.raise_for_status()
page = soup(response.text, "html.parser")
song_elements = page.select("li.chart-list__element")
songs = []
for song_element in song_elements:
    rank = int(song_element.select_one("span.chart-element__rank__number").string)
    title = song_element.select_one("span.chart-element__information__song").string
    artist = song_element.select_one("span.chart-element__information__artist").string
    songs.append({
        "rank": rank,
        "title": title,
        "artist": artist,
    })
print("Done!")

playlist_name_format = f"Hot 100 from {when}"
print(f"\nCreating your spotify playlist called {playlist_name_format}...", end="")
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user_id = sp.me()['id']

playlist = sp.user_playlist_create(user_id, playlist_name_format)

playlist_items = []
for song in songs:
    result = sp.search(f"{song['title']} {song['artist']}", limit=1)
    result_items = result["tracks"]["items"]
    if len(result_items):
        playlist_items.append(result_items[0]["id"])

sp.playlist_add_items(playlist["id"], playlist_items)
print("Done!")