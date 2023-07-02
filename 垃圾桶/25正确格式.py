import json
import os


folder = 'playlistdata'

json_files = [jsonfile for jsonfile in os.listdir(folder) if jsonfile.endswith('.json')]



for json_file in json_files:
    playlist_name = json_file.split('.')[0]
    file_name = f'{playlist_name}.json'
    file_path = os.path.join(folder, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Convert '万' to '0000' in the play count
    for playlist in data:
        play_count = playlist['播放量']
        if '万' in play_count:
            play_count = play_count.replace('万', '0000')
            playlist['播放量'] = play_count

    modified_file_name = f'格式化_{playlist_name}.json'
    modified_file_path = os.path.join(folder, modified_file_name)
    with open(modified_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
