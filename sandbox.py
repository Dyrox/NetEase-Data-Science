

import requests
from toolkits import convert_timestamp_to_date
import json
import time
import os

API = 'https://netease-cloud-music-api-umber-six-57.vercel.app/'

def get_playlist_tracks(playlist_id):
    playlist_tracks = requests.get(f'{API}playlist/track/all?id={playlist_id}').json()
    return playlist_tracks


okokok = get_playlist_tracks(4861796976)

