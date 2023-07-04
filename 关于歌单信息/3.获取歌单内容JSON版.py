import os
import json
from modules.GeneratePlaylistJson import generate_playlist_json

folder_path = '关于歌单信息/selected_playlists'
playlist_lists = [f for f in os.listdir(folder_path) if f.endswith('.json')]
playlist_links = []

def playlist_id_extractor(url):
    return url.split('=')[1].split('&')[0]

for playlist_list in playlist_lists:
    print(f'\033[92m 正在加载{playlist_list}...\033[0m')
    file_path = os.path.join(folder_path, playlist_list)
    with open(file_path, 'r', encoding='utf-8') as file:
        playlist_list_json = json.load(file)
        for playlist in playlist_list_json:
            playlist_link = playlist['歌单链接']
            playlist_links.append(playlist_link)

print(f'\033[93m 歌单链接获取完毕\033[0m')
playlist_num_count = 0


ALREADY_COLLECTED = str([f for f in os.listdir('关于歌单信息/歌单json') if f.endswith('.json')])

BLACKLIST = ['0','4862334130']
while playlist_num_count <100000:
    playlist_num_count += 1
    playlist_link = playlist_links[playlist_num_count]
    print(f'\033[92m 正在处理{playlist_link}...\033[0m')
    playlist_id = playlist_id_extractor(playlist_link)

    if playlist_id in BLACKLIST:
        print(f'\033[93m {playlist_id}被拉入黑名单, 跳过!\033[0m')
        continue

    if playlist_id in ALREADY_COLLECTED:
        print(f'\033[93m {playlist_id}已经存在, 跳过!\033[0m')
        continue

    
            
    generate_playlist_json(playlist_id)
    print(f'\033[93m {playlist_link}处理完毕\033[0m')
    print(f'\033[94m {playlist_num_count}个歌单已处理\033[0m')
    
