import subprocess
import json
import os
import glob
import re

class Tools:
    def __init__(self):
        Tools.etiquetas = ['FileName', 'Duration', 'FileSize', 'ImageHeight', 'FileTypeExtension', 'FileCreateDate']
        
    def obtenerMetadatos(self, archivos):
        parametros = []
        ubicaciones = []
        parametros.extend('-{}'.format(etiqueta) for etiqueta in Tools.etiquetas)
        ubicaciones.extend('{}'.format(archivo) for archivo in archivos)
        comando = ["exiftool", *parametros, "-json", *ubicaciones]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        
        if resultado.returncode != 0:
            print(f"Error al obtener metadatos para archivos.")
            return None
        
        salidaExiftool = resultado.stdout
        metadata = json.loads(salidaExiftool)
        regex = r'(\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2})([+-]\d{2}:\d{2})'
        
        for registro in metadata:
            coincidencia = re.match(regex, registro['FileCreateDate'])
            registro['FileCreateDate'] = coincidencia[1]
            
        return metadata  # Como acceder a la lista? acceso = metadata[registro]['atributo']
    
    def ubicarArchivosMp4(self, ruta):
        archivos = glob.glob(os.path.join(ruta, '*.mp4'))
        archivosMp4 = sorted(archivos, key=os.path.getctime)
        
        return archivosMp4