import json
import os
from modules.GeneratePlaylistJson import generate_playlist_json

# The JSON files are all located in the 'playlistdata/tables' folder
folder_path = '关于歌单信息/list_of_playlists'
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
playlist_links = []

def playlist_id_extractor(url):
    return url.split('=')[1].split('&')[0]

for json_file in json_files:
    print(f'\033[92m 正在处理{json_file}...\033[0m')
    file_path = os.path.join(folder_path, json_file)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for row in data:
            playlist_link = row['歌单链接']
            playlist_links.append(playlist_link)


print(playlist_links)
count = 0
while count < 100000:
    count += 1
    playlist_link = playlist_links[count]
    
    print(f'\033[92m 正在处理{playlist_link}...\033[0m')
    playlist_id = playlist_id_extractor(playlist_link)
    generate_playlist_json(playlist_id)
    print(f'\033[93m {playlist_link}处理完毕\033[0m')
    print(f'\033[94m {count}个歌单已处理\033[0m')
