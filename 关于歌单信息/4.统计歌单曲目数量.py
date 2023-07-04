import json
import os

folder_path = '关于歌单信息/歌单json'

playlists = [jsonfile for jsonfile in os.listdir(folder_path) if jsonfile.endswith('.json') and '歌单内容获取失败' not in jsonfile]


total_trackcount = 0
for playlist in playlists:
    file_path = os.path.join(folder_path, playlist)
    with open(file_path, 'r') as f:
        data = json.load(f)

        trackcount = data['playlist_info']['trackcount']
        total_trackcount += trackcount


print(f'一共有: {total_trackcount} 首曲目')
print(f'一共有: {len(playlists)} 个歌单')
