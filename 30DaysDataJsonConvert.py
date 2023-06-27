import os
import csv
import json
from toolkits import convert_timestamp_to_date



folder_path = '30daysdata'

json_files = [jsonfile for jsonfile in os.listdir(folder_path) if jsonfile.endswith('.json')]
date_added = False

selectedType = input('选择指标类型:\n1: 播放数\n2: 评论数\n3: 收藏数\n4: 开播数\n5: 粉丝播放占比\n6: 云贝推歌人数\n')

user_mapping = {
    '1': 'playIndexs',
    '2': 'cmtIndexs',
    '3': 'collectICountIndexs',
    '4': 'cloudShellPlayIndexs',
    '5': 'fansPlayRatio',
    '6': 'cloudShellPromoteIndexs'
}

index_json_mapping = {
    'playIndexs': 'number',
    'collectICountIndexs': 'number',
    'cmtIndexs': 'number',
    'cloudShellPlayIndexs': 'playCount',
    'fansPlayRatio': 'fansPlayRatio',
    'cloudShellPromoteIndexs': 'promoteCount'
}

desiredIndexType = user_mapping.get(selectedType)

if desiredIndexType is None:
    raise ValueError('Invalid input')


csvfilename = f'{desiredIndexType}.csv'
if not os.path.exists(os.path.join(folder_path, 'tables')):
    os.mkdir(os.path.join(folder_path, 'tables'))
csvfilepath = os.path.join(folder_path, 'tables',csvfilename)

with open(csvfilepath, 'w', newline='') as csvfile:
    for json_file in json_files:
        with open(os.path.join(folder_path, json_file), 'r') as f:
            json_data = json.load(f)
            Indexs = json_data['data'][desiredIndexType]
            
            print(f'\033[92m 正在处理{json_file}...\033[0m')
            
            data = []
            date_timestamps = []

            for Index in Indexs:
                
                date_timestamp = Index['date']
                date_timestamps.append(date_timestamp)

                if desiredIndexType in index_json_mapping:
                    key = index_json_mapping[desiredIndexType]
                    value = Index[key]
                    data.append(value)
                
    
            dates = [convert_timestamp_to_date(date_timestamp) for date_timestamp in date_timestamps]
            writer = csv.writer(csvfile)

            #只在第一行加入日期
            if not date_added:
                writer.writerow(["日期"] + dates)
                date_added = True
            
            song_name = json_file.split('.')[0]
            song_name = song_name.title()

            #write the number row on the file_count column
            writer.writerow([song_name] + data) 


print(f'\033[93m 处理完成\033[0m')
        
    
