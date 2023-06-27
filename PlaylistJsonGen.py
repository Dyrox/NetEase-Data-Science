import requests
from toolkits import convert_timestamp_to_date
import json
import time
import os

API = 'https://netease-cloud-music-api-umber-six-57.vercel.app/'
test_link = 'https://music.163.com/playlist?id=7692308691&userid=440102611'

def playlist_id_extractor(url):
    return url.split('=')[1].split('&')[0]

def get_playlist_info(playlist_id):
    playlist_info = requests.get(API + 'playlist/detail?id=' + playlist_id).json()
    return playlist_info

def get_playlist_tracks(playlist_id):
    playlist_tracks = requests.get(f'{API}playlist/track/all?id={playlist_id}').json()
    return playlist_tracks


def generate_playlist_json(playlist_link):
    folder_name = 'playlist_songs_jsons'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    playlist_id = playlist_id_extractor(playlist_link)
    playlist_info = get_playlist_info(playlist_id)

    playlist_name = playlist_info['playlist']['name']

    file_name = f'{playlist_name} - {playlist_id}.json'
    file_name = file_name.replace('/', '')

    if os.path.exists(os.path.join(folder_name, file_name)):
        print(f'\033[92m {playlist_link}已存在\033[0m')
        return
    
    playlist_trackcount = playlist_info['playlist']['trackCount']
    playlist_playcount = playlist_info['playlist']['playCount']
    playlist_creator = playlist_info['playlist']['creator']['nickname']
    playlist_createTimeStamp = playlist_info['playlist']['createTime']
    playlist_age_days = (time.time() - playlist_createTimeStamp / 1000) / 86400
    playlist_heat = playlist_playcount // playlist_age_days
    playlist_createDate = convert_timestamp_to_date(playlist_createTimeStamp)

    
    

    playlist_json = {
        'playlist_info': {
            'name': playlist_name,
            'trackcount': playlist_trackcount,
            'playcount': playlist_playcount,
            'creator': playlist_creator,
            'createDate': playlist_createDate,
            'heat': playlist_heat,
        },
        'songs': []
    }

    try:
        playlist_tracks = get_playlist_tracks(playlist_id)

    except:
        print(f'\033[91m {playlist_link}无法获取歌单信息\033[0m')
        return
    for song in playlist_tracks['songs']:
        one_song = {
            'name': song['name'],
            'artist': song['ar'][0]['name'],
            'id': song['id']
        }
        playlist_json['songs'].append(one_song)

    file_path = os.path.join(folder_name, file_name)

    with open(file_path, 'w') as f:
        json.dump(playlist_json, f, indent=4, ensure_ascii=False)
