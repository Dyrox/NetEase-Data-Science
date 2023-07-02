import csv
import os
from PlaylistJsonGen import generate_playlist_json

#the csv files are all here playlistdata/tables
folderpath = 'playlistdata/tables'
csv_files = [f for f in os.listdir(folderpath) if f.endswith('.csv')]
playlist_links = []

def playlist_id_extractor(url):
    return url.split('=')[1].split('&')[0]


for csv_file in csv_files:
    print(f'\033[92m 正在处理{csv_file}...\033[0m')
    file_path = os.path.join(folderpath, csv_file)
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            playlist_link = row['歌单链接']
            playlist_links.append(playlist_link)

count = 0
while count <100000:
    count += 1
    playlist_link = playlist_links[count]
    
    print(f'\033[92m 正在处理{playlist_link}...\033[0m')
    playlist_id = playlist_id_extractor(playlist_link)
    generate_playlist_json(playlist_id)
    print(f'\033[93m {playlist_link}处理完毕\033[0m')
    print(f'\033[94m {count}个歌单已处理\033[0m')
    
    

