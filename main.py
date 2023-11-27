from script import Script
from extensions.web.playlist import Playlist


linkPlaylist = r"https://www.youtube.com/playlist?list=PLAKTtN7vEpniX15TkDhNkhTaJFpdpBSm_"
rutaCarpeta = r'C:\Users\063\Desktop\videos\playlist'

script = Script(linkPlaylist, rutaCarpeta)
registro = script.webEnMetadata()
for item in registro:
    print(item)