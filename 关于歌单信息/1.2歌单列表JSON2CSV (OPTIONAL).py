import json
import csv
import os
#the json files are all in the folder playlistjsons folder
folder_path = '关于歌单信息/list_of_playlists'
json_files = [jsonfile for jsonfile in os.listdir(folder_path) if jsonfile.endswith('.json')]


NumberOfFiles = 0


for json_file in json_files:
    NumberOfFiles += 1
    playlist_name = json_file.split('.')[0]
    with open(os.path.join(folder_path, json_file), 'r') as f:
        data = json.load(f)

        fieldnames = data[0].keys()
        csvfilename = f'{playlist_name}.csv'
        if not os.path.exists(os.path.join(folder_path, 'tables')):
            os.mkdir(os.path.join(folder_path, 'tables'))
        csvfilepath = os.path.join(folder_path, 'tables',csvfilename)
        
        with open(csvfilepath, 'w', newline='',encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print('转换完成, CSV文件保存为 ', csvfilename)

print(f'共转换{NumberOfFiles}个文件')


