from script import Script
from extensions.web.playlist import Playlist

linkPlaylist = r"https://www.youtube.com/watch?v=dWxbX827Klc&list=PLAKTtN7vEpniX15TkDhNkhTaJFpdpBSm_&ab_channel=CentrodeInnovaci%C3%B3nYDesarrollo"
rutaCarpeta = r'C:\Users\063\Desktop\videos\hegel'

playlist = Playlist(linkPlaylist)
nombres = playlist.videos
for nombre in nombres:  #debug
    print(nombre)
#script = Script(linkPlaylist, rutaCarpeta)
#registro = script.webEnMetadata()
#for item in registro:
#    print(item)