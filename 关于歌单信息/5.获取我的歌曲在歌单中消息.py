import csv
import json
import os

folder_path = '关于歌单信息/歌单json'
output_folder = '关于歌单信息/contained_playlist_csv'

MYSONGS_DICT = {
    1467985762: 'Standing Still',
    1469549176: 'The Whisper Of Galaxy',
    1471802235: 'Everything Flows',
    1474891634: 'The Breeze Of Dusk',
    1482032199: 'As Time Goes By',
    1490735020: 'The Other Side Of Us',
    1834969578: 'Forest And Sunset',
    1872745825: 'Summer Story',
    1882181042: 'Fading Memories',
    1922523191: 'Chilly Nights',
    1936650330: 'My Guiding Star',
    2013630617: 'Moving On'
}

# SONGS8_DICT = {1986510161: 'shall we talk.', 1960123993: 'summer.', 2053935560: '洛希极限', 2012291672: 'pretend.', 2021350066: 'shall we talk.（acoustic）', 1904090991: 'goodbye.', 1968084132: "无眠夜（hey hey it's ok）", 1911573487: 'Memories', 2057318547: 'saturday.', 2004704870: 'white winter.', 1998984459: '8bite.', 1891674819: 'Going Home', 2016567786: '18', 1935783660: '不想', 2032502677: '末丽', 1869139533: 'date back.', 2045539018: 'destiny.', 1953388012: 'Stay Awake', 2037723384: 'circles.', 1971553872: '我们拥抱夏日的深海', 1930290451: 'Drunk', 2009591836: 'blue.', 1356691771: 'RIPPER', 1444803461: '星河揽月归.', 1985140633: 'Chasing Love', 2045541755: 'pardon.', 2046702255: "Never Thinkin' About (feat. 8bite)", 1416966548: 'Winter（冬）', 2055563084: '洛希极限（Instrumental）', 1461853772: 'Constellations', 1447076277: 'Windfall(8Bite REMAKE)（翻自 TheFatRat）', 1864405488: 'Tonight', 1878918032: 'Leavin', 2039799254: 'Shall We Talk. (Litchee Remix)', 1442800363: '茶弈', 1430296133: '失', 1420308917: 'When U Come Home', 1995658431: 'wake up.', 1867071799: '羁绊', 1969254256: '偷懒', 1473310775: 'Echoes', 1444802934: '路遥星亦辞.', 528976592: '剑津(Original\xa0Mix)', 1489558301: 'Give And Take', 1937186741: 'I Like Me Better(8bite Cover)', 1946868757: 'movingon', 1467135980: 'Pluto', 2004703209: 'snowy day.', 1805865732: 'too late', 1332157070: 'Fairytale', 1808369143: 'to the sky.', 1961476118: 'Flying By', 1993687656: 'shall we talk.(Mestie Remix)', 1957464056: 'better off.', 1819688764: '17', 1377491624: 'Behemoth Attack', 1878916231: 'Leavin(Acoustic)', 1432871067: '喵内噶', 1927408253: '机械不夜之城', 1443573023: '熵', 1440336604: 'River Rose', 1425886171: 'Ocean In The Sky', 1446321350: '鲸落', 1429172529: '望', 1439586027: 'S T A R D U S T O D Y S S E Y', 1444803545: '持夜梦星赐.', 866298707: 'Adventures', 1927408250: '田园放克农庄', 864797838: 'Infinity', 541748184: 'Galaxy', 541076257: 'Hopeless', 1996161072: 'shall we talk.(Ferdinand Remix)', 1994976407: 'summer down,jazz,zhejiang,11.3', 1989646356: 'Leavin (MasterJ Remix)', 1971720828: '【BEAT】summer', 1967425071: 'Leavin（Glittering Wine remix）', 1967214557: 'getacandy', 1933652097: 'Chaos', 1927412819: 'Metro大都会', 1927412818: '星空水晶小镇', 1927408251: '黄金玛雅国度', 1922349060: 'Demo', 1921312236: 'Serenade für Streicher in G-Dur(Nylon Ver.)', 1919373209: "i'm fine.", 1911624414: 'in the sky.', 1900731947: 'Leavin(LYC Remix)', 1900729558: 'Leavin(Zhiqiu Yang Remix)', 1900728957: 'Leavin(Wildpants Remix)', 1900725356: "Leavin(Annn's Rethink)", 1900725138: 'Leavin(X-Eliminator Remix)', 1887741050: 'Armed Force', 1868953457: 'Anybody', 1862770585: 'never ever.', 1858382851: 'last summer.', 1852243135: '南平一中·紫云', 1495466749: 'Amber Invader', 1488054283: 'Mercy', 1483815753: '南 一 猴 山', 1480755807: 'silhouette.', 1469892059: 'Outro - Nebula'}
playlists = [jsonfile for jsonfile in os.listdir(folder_path) if jsonfile.endswith('.json') and '歌单内容获取失败' not in jsonfile]

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for MYSONGID, MYSONGNAME in MYSONGS_DICT.items():
    print(f'正在处理{MYSONGNAME}')
    filename = f'{MYSONGNAME}.csv'
    file_path = os.path.join(output_folder, filename)

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["playlist_name", "playlist_contributing_factor", "song_ranking", "playlist_heat", "trackcount", "playlist_playcount"])

        for playlist in playlists:
            file_path = os.path.join(folder_path, playlist)

            with open(file_path, 'r') as f:
                playlist_data = json.load(f)

                for song in playlist_data['songs']:
                    if song['id'] == MYSONGID:
                        playlist_name = playlist_data['playlist_info']['name']
                        song_ranking = playlist_data['songs'].index(song) + 1
                        playlist_heat = round(playlist_data['playlist_info']['heat'])
                        trackcount = playlist_data['playlist_info']['trackcount']
                        playlist_playcount = playlist_data['playlist_info']['playcount']
                        playlist_contributing_factor = round((1 - song_ranking / trackcount) * playlist_heat)
                        writer.writerow([playlist_name, playlist_contributing_factor, song_ranking, playlist_heat, trackcount, playlist_playcount])
                        break


print(f'\033[92m歌单处理完毕\033[0m')

# Sort the CSV files by the "playlist_contributing_factor" column
for MYSONGNAME in MYSONGS_DICT.values():
    filename = f'{MYSONGNAME}.csv'
    file_path = os.path.join(output_folder, filename)

    rows = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    sorted_rows = sorted(rows[1:], key=lambda row: int(row[1]), reverse=True)
    sorted_rows.insert(0, rows[0])

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sorted_rows)


contained_playlists = []
ARTIST = 'PHONO RECORDS'
for playlist in playlists:
    file_path = os.path.join(folder_path, playlist)

    with open(file_path, 'r') as f:
        fileStr = f.read()
        if ARTIST in fileStr:
            contained_playlists.append(playlist)

print(f'\033[92m{ARTIST}创作的歌曲被包含在{len(contained_playlists)}个歌单内\033[0m')