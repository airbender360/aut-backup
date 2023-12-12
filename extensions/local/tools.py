import subprocess
import json
import os
import glob
import re

class Tools:
    etiquetas = ['FileName', 'Duration', 'FileSize', 'ImageHeight', 'FileTypeExtension', 'FileCreateDate']

    def crearCarpeta(self, ruta, nombre):
        rutaCarpeta = os.path.join(ruta, nombre)
        os.mkdir(rutaCarpeta)
        return rutaCarpeta
    
    def ubicarArchivosMp4(self, ruta):
        rutaArchivosMp4 = glob.glob(os.path.join(ruta, '*.mp4'))
        rutaArchivosMp4 = sorted(rutaArchivosMp4, key=os.path.getctime)
        
        if len(rutaArchivosMp4) == 0:
            print('Error: no se encontraron archivos .mp4 en la carpeta destino.')
        return rutaArchivosMp4
    
    def exiftool(self, archivos):
        parametros = []
        ubicaciones = []
        parametros.extend('-{}'.format(etiqueta) for etiqueta in Tools.etiquetas)
        ubicaciones.extend('{}'.format(archivo) for archivo in archivos)
        comando = ["exiftool", *parametros, "-json", *ubicaciones]
        proceso = subprocess.run(comando, capture_output=True, text=True, shell=True)
        
        if proceso.returncode != 0:
            print(f"Error: no se han podido extraer los metadatos.")
            return None
        
        resultado = proceso.stdout
        metadatos = json.loads(resultado)
        return metadatos  # Como acceder a la lista? acceso = metadata[registro]['atributo']
    
    def formatearMetadatos(self, metadatos):
        regex = r'(\d+):(\d+):(\d+) (\d+):(\d+):(\d+)-\d+:\d+'
        
        for registro in metadatos:
            coincidencia = re.match(regex, registro['FileCreateDate'])
            registro['FileCreateDate'] = f'{coincidencia[3]}/{coincidencia[2]}/{coincidencia[1]} {coincidencia[4]}:{coincidencia[5]}:{coincidencia[6]}'
        return metadatos
    
    def ytdlp(self, argumento):
        comando = f'yt-dlp {argumento}'
        proceso = subprocess.run(comando, stderr=subprocess.PIPE, text=True)
        if proceso.returncode != 0:
            print(f'Error: {proceso.stderr}')