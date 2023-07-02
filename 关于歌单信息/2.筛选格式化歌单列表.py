import os
import json

folder_path = '关于歌单信息/list_of_playlists'
new_folder_path = '关于歌单信息/selected_playlists'
playlist_lists = [f for f in os.listdir(folder_path) if f.endswith('.json')]

def wan2int():
    for playlist_list in playlist_lists:
        file_path = os.path.join(folder_path, playlist_list)
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
            contents = contents.replace('万', '0000')
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(contents)

def delete_below_500000_play():
    
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)

    json_files = [jsonfile for jsonfile in os.listdir(folder_path) if jsonfile.endswith('.json')]

    for json_file in json_files:
        file_path = os.path.join(folder_path, json_file)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Filter playlists based on play count
        filtered_data = [playlist for playlist in data if int(playlist['播放量']) >= 500000]

        new_filename = f'筛选_{json_file}'
        new_filepath = os.path.join(new_folder_path, new_filename)
        with open(new_filepath, 'w', encoding='utf-8') as file:
            json.dump(filtered_data, file, ensure_ascii=False, indent=2)


wan2int()
delete_below_500000_play()
print(f'歌单筛选完毕, 文件保存于 "{new_folder_path}"')
