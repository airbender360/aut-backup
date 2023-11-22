import subprocess
import json
import os
import glob

def obtener_metadatos_subprocess(files, etiquetas):
    args = []
    path = []
    args.extend('-{}'.format(etiqueta) for etiqueta in etiquetas)
    path.extend('{}'.format(file) for file in files)
    comando = ["exiftool", *args, "-json", *files]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    
    if resultado.returncode != 0:
        print(f"Error al obtener metadatos para archivos.")
        return None
    salida_exiftool = resultado.stdout
    metadata = json.loads(salida_exiftool)
    # Como acceder a la lista? acceso = metadata[registro]['atributo']
    return metadata

def obtener_ubicaciones_glob(carpeta):
    archivos_mp4 = glob.glob(os.path.join(carpeta, '*.mp4'))
    # glob.glob() regresa una lista con directorios específicados, os.path.join() construye un directorio completo para archivos con el parámetro *.mp4
    return archivos_mp4

# Ejemplo de uso.
#Se especifica la ruta de la carpeta
archivos = obtener_ubicaciones_glob(r'rutacarpeta')
#Se especifican las etiquetas
etiquetas_deseadas = ['FileName', 'Duration', 'FileSize', 'ImageHeight', 'FileTypeExtension', 'FileCreateDate']
# El método recibe 2 listas, una con las ubicaciones de los archivos y otra con las etiquetas a extraer de exiftool.
salida_exiftool = obtener_metadatos_subprocess(archivos, etiquetas_deseadas)