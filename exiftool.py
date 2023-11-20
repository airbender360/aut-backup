import subprocess
import json

def obtener_metadatos_subprocess(files, etiquetas):
    args = []
    path =[]
    args.extend('-{}'.format(etiqueta) for etiqueta in etiquetas)
    path.extend('{}'.format(file) for file in files)
    comando = ["exiftool", *args, "-json", *files]
    resultado = subprocess.run(comando, capture_output=True, text=True)

    if resultado.returncode != 0:
        print(f"Error al obtener metadatos para archivos.")
        return None
    salida_exiftool = resultado.stdout
    metadata_list = json.loads(salida_exiftool)

    # Como acceder a la lista? acceso = metadata_list[registro]['atributo']
    return metadata_list

# Ejemplo de uso.
archivos = [r"C:\Users\USUARIO\Documents\prueba\video1.mp4", r"C:\Users\USUARIO\Documents\prueba\video2.mp4",r"C:\Users\USUARIO\Documents\prueba\video3.mp4"]
etiquetas_deseadas = ['FileName', 'Duration', 'FileSize', 'ImageHeight', 'FileTypeExtension', 'FileCreateDate']
# El método recibe 2 listas, una con las ubicaciones de los archivos y otra con las etiquetas a extraer de exiftool.
salida_exiftool = obtener_metadatos_subprocess(archivos, etiquetas_deseadas)

print(salida_exiftool)