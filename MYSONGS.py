import os
import json

folder_path = '关于歌单信息/歌单json'


MYSONGS = ['Standing Still', 
           'The Whisper Of Galaxy', 
           'Everything Flows', 
           'The Breeze Of Dusk', 
           'As Time Goes By', 
           'The Other Side Of Us', 
           'Forest And Sunset', 
           'Summer Story', 
           'Fading Memories', 
           'Chilly Nights', 
           'My Guiding Star', 
           'Moving On']

MYSONGS_ID = [
1467985762,
1469549176,
1471802235,
1474891634,
1482032199,
1490735020,
1834969578,
1872745825,
1882181042,
1922523191,
1936650330,
2013630617]



playlists = [jsonfile for jsonfile in os.listdir(folder_path) if jsonfile.endswith('.json')]
contained_playlists = []


for playlist in playlists:
    file_path = os.path.join(folder_path,playlist)
    
    with open(file_path,'r') as f:
        fileStr = f.read()
        if 'Polaranica' in fileStr:
            contained_playlists.append(playlist)


for p in contained_playlists:
    print(p)
        
print(len(contained_playlists))