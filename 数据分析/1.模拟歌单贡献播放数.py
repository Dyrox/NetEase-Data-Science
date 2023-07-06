import os
import csv

playlist_song_data = '关于歌单信息/contained_playlist_csv'
csv_file = '关于30天后台信息/30daysdata/tables/cloudShellPlayIndexs.csv'
output_folder = '数据分析/estimated_plays_csv'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


song_contained_playlist_csvs = [f for f in os.listdir(playlist_song_data) if f.endswith('.csv') and not 'estimated' in f]

song_avgs_plays = {}
song_estimated_play = {}
song_playlist_names = {}
song_contribution_factors = {}

with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)
    for song in song_contained_playlist_csvs:
        songname = song.replace('.csv', '')

        for i, row in enumerate(data):
            if row[0] == songname:
                row_index = i
                break

        # Extract the average play count from the last column of the row
        average_play_count = data[row_index][-1]
        song_avgs_plays[songname] = int(average_play_count)

for song_playlist_csv in song_contained_playlist_csvs:
    file_path = os.path.join(playlist_song_data, song_playlist_csv)
    songname = song_playlist_csv.replace('.csv','')
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row

        total_playlist_contributing_factor = 0
        for row in reader:
            playlist_contributing_factor = int(row[1])
            total_playlist_contributing_factor += playlist_contributing_factor
        
        f.seek(0)  # Move the reader position back to the beginning
        next(reader)  # Skip the header row
        
        estimated_plays = [round(int(row[1])/total_playlist_contributing_factor*song_avgs_plays[songname]) for row in reader]
        f.seek(0)  # Move the reader position back to the beginning
        next(reader) 
        playlist_names = [row[0] for row in reader]
        f.seek(0)  # Move the reader position back to the beginning
        next(reader) 
        contribution_factors = [int(row[1]) for row in reader]

        song_estimated_play[songname] = estimated_plays
        song_playlist_names[songname] = playlist_names
        song_contribution_factors[songname] = contribution_factors





#create various new csv files, so songname.csv with format playlist_name,playlist_contributing_factor, estimated_play_count


for song in song_contained_playlist_csvs:
    songname = song.replace('.csv', '')
    new_file_name = song.replace('.csv', '_estimated_plays.csv')
    file_path = os.path.join(output_folder, new_file_name)
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['playlist_name', 'playlist_contributing_factor', 'estimated_play_count'])
        for i, playlist_name in enumerate(song_playlist_names[songname]):
            writer.writerow([playlist_name, song_contribution_factors[songname][i], song_estimated_play[songname][i]])

print('\033[91mDone!\033[0m')
