from pathlib import Path
from extensions.local.tools import Tools

class Folder:
    
    def __init__(self, ruta):
        self.tools = Tools()
        self.nombreCarpeta = Path(ruta).name
        self.archivosMp4 = self.tools.ubicarArchivosMp4(ruta)
        self.metadatos = self.tools.obtenerMetadatos(self.archivosMp4)