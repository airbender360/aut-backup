from extensions.local.tools import Tools

class Folder:
    
    def __init__(self, ruta, nombre, link):
        try:
            self.tools = Tools()
            self.linkPlaylist = link
            self.nombreCarpeta = nombre
            self.rutaCarpeta = self.tools.crearCarpeta(ruta, self.nombreCarpeta)
            
        except Exception as e:
            print(f'Error: {e}')
        else:
            print('1. Creación exitosa (Carpeta)')
        
    def obtenerMetadatos(self):
        try:
            metadatos = self.tools.exiftool(self.rutaCarpeta)
            metadatos = self.tools.formatearMetadatos(metadatos)
        except Exception as e:
            print(f'Error: {e}')
        else:
            print('4. Extracción exitosa (Metadatos)')
        finally:
            return metadatos
    
    def descargarVideos(self, ruta, link, flag):
        try:
            if flag:
                ruta = r'"{}\{}\%(title)s.%(ext)s"'.format(ruta, self.nombreCarpeta)
                argumento = f'-o {ruta} {link}'
                self.tools.ytdlp(argumento)
            else:
                print('Sin descarga de Playlist.')
        except Exception as e:
            print(f'Error: {e}')
        else:
            print('3. Descarga exitosa (Playlist)')