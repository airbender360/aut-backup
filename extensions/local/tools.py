import subprocess
import json
import os
import re
import ftfy

class Tools:
    etiquetas = ['-FileName', '-Duration', '-FileSize', '-ImageHeight', '-FileTypeExtension', '-FileCreateDate']

    def crearCarpeta(self, ruta, nombre):
        rutaCarpeta = os.path.join(ruta, nombre)
        try:
            os.mkdir(rutaCarpeta)
        except FileExistsError:
            pass
        finally:
            return rutaCarpeta
    
    def exiftool(self, ruta):
        comando = ["exiftool", *Tools.etiquetas, "-json", ruta]
        proceso = subprocess.run(comando, capture_output=True, text=True, shell=True)

        if proceso.returncode != 0:
            print(f"Error: no se han podido extraer los metadatos.")
            return None
        
        resultado = proceso.stdout
        metadatos = json.loads(resultado)
        return metadatos  # Como acceder a la lista? acceso = metadatos[registro]['atributo']
    
    def formatearMetadatos(self, metadatos):
        regex = r'(\d+):(\d+):(\d+) (\d+):(\d+):(\d+)-\d+:\d+'
        
        for registro in metadatos:
            try:
                coincidencia = re.match(regex, registro['FileCreateDate'])
                registro['FileCreateDate'] = f'{coincidencia[3]}/{coincidencia[2]}/{coincidencia[1]} {coincidencia[4]}:{coincidencia[5]}:{coincidencia[6]}'
                registro['FileName'] = ftfy.fix_text(registro['FileName'])
            except Exception as e:
                print(f'Error {e} en FileName: {registro['FileName']}')
        return metadatos
    
    def ytdlp(self, argumento):
        comando = f'yt-dlp {argumento}'
        proceso = subprocess.run(comando, stderr=subprocess.PIPE, text=True)
        if proceso.returncode != 0:
            print(f'Error: {proceso.stderr}')