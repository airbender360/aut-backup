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
            for video in videos.items():
                for registro in metadatos:
                    if video[0] + '.mp4' == registro['FileName']:
                        registro['YouTubeName'] = video[0]
                        registro['UploadDate'] = video[1]
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("5. Integración exitosa (Metadatos + API)")
            self.metadatos = metadatos
            
    def documentarExcel(self):
        self.hoja = Hoja(self.rutaExcel, self.playlist.nombrePlaylist, self.metadatos)
        self.hoja.formatearHoja()
        self.hoja.crearRegistro()

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
        
    def main(self, flag):
        self.playlist.datosVideos()
        self.folder.descargarVideos(self.ruta, self.linkPlaylist, flag)
        self.metadatos = self.folder.obtenerMetadatos()
        
        self.webEnMetadata()
        self.documentarExcel()