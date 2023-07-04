import csv
import json
import os

folder_path = '关于歌单信息/歌单json'
output_folder = '关于歌单信息/contained_playlist_csv'

MYSONGS_DICT = {
    1467985762: 'Standing Still',
    1469549176: 'The Whisper Of Galaxy',
    1471802235: 'Everything Flows',
    1474891634: 'The Breeze Of Dusk',
    1482032199: 'As Time Goes By',
    1490735020: 'The Other Side Of Us',
    1834969578: 'Forest And Sunset',
    1872745825: 'Summer Story',
    1882181042: 'Fading Memories',
    1922523191: 'Chilly Nights',
    1936650330: 'My Guiding Star',
    2013630617: 'Moving On'
}

playlists = [jsonfile for jsonfile in os.listdir(folder_path) if jsonfile.endswith('.json') and '歌单内容获取失败' not in jsonfile]

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for MYSONGID, MYSONGNAME in MYSONGS_DICT.items():
    # Create a new CSV file for each song
    filename = f'{MYSONGNAME}.csv'
    file_path = os.path.join(output_folder, filename)

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["playlist_name", "playlist_contributing_factor", "song_ranking", "playlist_heat", "trackcount", "playlist_playcount"])

        for playlist in playlists:
            file_path = os.path.join(folder_path, playlist)

            with open(file_path, 'r') as f:
                playlist_data = json.load(f)

                for song in playlist_data['songs']:
                    if song['id'] == MYSONGID:
                        playlist_name = playlist_data['playlist_info']['name']
                        song_ranking = playlist_data['songs'].index(song) + 1
                        playlist_heat = playlist_data['playlist_info']['heat']
                        trackcount = playlist_data['playlist_info']['trackcount']
                        playlist_playcount = playlist_data['playlist_info']['playcount']
                        playlist_contributing_factor = round((1 - song_ranking / trackcount) * playlist_heat)
                        writer.writerow([playlist_name, playlist_contributing_factor, song_ranking, playlist_heat, trackcount, playlist_playcount])
                        break


print(f'\033[92m歌单处理完毕\033[0m')


contained_playlists = []
ARTIST = 'Polaranica'
for playlist in playlists:
    file_path = os.path.join(folder_path,playlist)
    
    with open(file_path,'r') as f:
        fileStr = f.read()
        if ARTIST in fileStr:
            contained_playlists.append(playlist)

print(f'\033[92m{ARTIST}创作的歌曲被包含在{len(contained_playlists)}个歌单内\033[0m')



