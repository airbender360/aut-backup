from extensions.web.playlist import Playlist
from extensions.local.folder import Folder
from extensions.excel import Hoja


class Script:
    def __init__(self, link, rutaCarpeta, rutaExcel):
        self.link = link
        self.rutaCarpeta = rutaCarpeta
        self.rutaExcel = rutaExcel
        
        self.folder = Folder(self.rutaCarpeta)
        self.playlist = Playlist(self.link)
        self.playlistName = self.playlist.nombre
        
    def webEnMetadata(self):
        videos = self.playlist.videos
        self.metadatos = self.folder.metadatos 
        for indice, (nombreVideo, tiempoVideo) in enumerate(videos.items()):
                    self.metadatos[indice]['YouTubeName'] = nombreVideo
                    self.metadatos[indice]['UploadDate'] = tiempoVideo
        return self.metadatos
    
    def documentarExcel(self):
        self.hoja = Hoja(self.rutaExcel, self.playlistName, self.metadatos)
        self.hoja.crearRegistro()