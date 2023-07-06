import requests

API = 'https://netease-cloud-music-api-umber-six-57.vercel.app/'

def get_musician_info(musician_id):
    playlist_info = requests.get(API + 'artist/songs?id=' + musician_id).json()
    return playlist_info

def musician_id_extrator(musican_link):
    if 'home' in musican_link:
        raise Exception('输入的链接是主页链接')
    return musican_link.split('=')[1].split('&')[0]


musician_id = musician_id_extrator(input('输入音乐人链接: '))

data = get_musician_info(musician_id)


my_songs = {}
for song in data['songs']:
    song_id = song['id']
    song_name = song['name']
    my_songs[song_id] = song_name


print(my_songs)