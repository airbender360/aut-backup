from extensions.web.playlist import Playlist
from extensions.local.folder import Folder
from extensions.excel import Hoja

class Script:
    def __init__(self, linkPlaylist, ruta, rutaExcel):
        self.linkPlaylist = linkPlaylist
        self.ruta = ruta
        self.rutaExcel = rutaExcel
        
        self.playlist = Playlist(self.linkPlaylist)
        self.folder = Folder(self.ruta, self.playlist.nombrePlaylist, self.linkPlaylist)
        
    def webEnMetadata(self):
        videos = self.playlist.videos
        metadatos = self.metadatos
        try:
            for indice, (nombreVideo, tiempoVideo) in enumerate(videos.items()):
                        metadatos[indice]['YouTubeName'] = nombreVideo
                        metadatos[indice]['UploadDate'] = tiempoVideo
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("5. Integración exitosa (Metadatos + API)")
            self.metadatos = metadatos
            self.rutaArchivos = dict(zip(list(videos), self.rutaArchivos))
            
    def documentarExcel(self):
        self.hoja = Hoja(self.rutaExcel, self.playlist.nombrePlaylist, self.metadatos)
        self.hoja.formatearHoja()
        self.hoja.crearRegistro()
        
    def main(self):
        self.playlist.datosVideos()
        self.folder.descargarVideos(self.ruta, self.linkPlaylist)
        self.rutaArchivos, self.metadatos = self.folder.obtenerMetadatos()

        self.webEnMetadata()
        self.documentarExcel()