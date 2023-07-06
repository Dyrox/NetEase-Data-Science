import os
import csv

raw_csv_folder = '数据分析/estimated_plays_csv'

song_csvs = [f for f in os.listdir(raw_csv_folder) if f.endswith('.csv')]

playlist_contributing_factors = []
estimated_play_count = []

for song_csv in song_csvs:
    file_path = os.path.join(raw_csv_folder,song_csv)
    with open(file_path, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            playlist_contributing_factors.append(line[1])
            estimated_play_count.append(line[2])


destination_file_path = os.path.join('数据分析','training_data_csv.csv')

with open(destination_file_path,'w',encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['playlist_contributing_factors','estimated_play_count'])
    for i in range(len(playlist_contributing_factors)):
        csv_writer.writerow([playlist_contributing_factors[i],estimated_play_count[i]])

print('done')