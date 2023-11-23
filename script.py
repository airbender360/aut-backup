from extensions.web.playlist import Playlist
from extensions.local.folder import Folder


class Script:
    def __init__(self, link, rutaCarpeta):
        self.link = link
        self.rutaCarpeta = rutaCarpeta
        
    def webEnMetadata(self):
        playlist = Playlist(self.link)
        videos = playlist.videos  #debug en linea 13 y revisar elementos
        folder = Folder(self.rutaCarpeta)
        metadatos = folder.metadatos  #debug en linea 15 y revisar metadatos
        for nombreVideo, tiempoVideo in videos:
            for registro in metadatos:
                if registro['FileName'] == nombreVideo:
                    registro['YouTubeName'] = nombreVideo
                    registro['UploadDate'] = tiempoVideo
                    break
                
        return metadatos