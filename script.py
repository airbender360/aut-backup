from extensions.web.playlist import Playlist
from extensions.local.folder import Folder


class Script:
    def __init__(self, link, rutaCarpeta):
        self.link = link
        self.rutaCarpeta = rutaCarpeta
        
    def webEnMetadata(self):
        playlist = Playlist(self.link)
        videos = playlist.videos
        folder = Folder(self.rutaCarpeta)
        metadatos = folder.metadatos 
        
        for indice, (nombreVideo, tiempoVideo) in enumerate(videos.items()):
                    metadatos[indice]['YouTubeName'] = nombreVideo
                    metadatos[indice]['UploadDate'] = tiempoVideo
        return metadatos