import json
import os

folder = 'playlistdataformatted'
json_files = [jsonfile for jsonfile in os.listdir(folder) if jsonfile.endswith('.json')]

for json_file in json_files:
    file_path = os.path.join(folder, json_file)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Filter playlists based on play count
    filtered_data = [playlist for playlist in data if int(playlist['播放量']) >= 500000]

    new_filename = f'筛选_{json_file}'
    new_filepath = os.path.join(folder, new_filename)
    with open(new_filepath, 'w', encoding='utf-8') as file:
        json.dump(filtered_data, file, ensure_ascii=False, indent=2)
