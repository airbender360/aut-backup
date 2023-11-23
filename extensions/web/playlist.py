from extensions.web.youtubeApiGet import YoutubeApiGet
import re

class Playlist:
    def __init__(self, link):
        regex = r'(?<=list=)([\w-]+)' # si la estructura de los enlaces cambia, actualización necesaria
        self.id = re.findall(regex, link)
        self.youtubeapiget = YoutubeApiGet(self.id[0])
        self.nombre = self.youtubeapiget.obtenerNombre()
        self.fechasDeSubida = self.youtubeapiget.obtenerFechasDeSubida()
        self.fechasDeSubida = self.ordenarFechasDeSubida(self.fechasDeSubida)
        self.nombresVideos = self.youtubeapiget.obtenerNombresVideos()
        self.videos = dict(zip(self.nombresVideos, self.fechasDeSubida))
        
    def ordenarFechasDeSubida(self, lista):
        regex = r'(\d{4})-(\d{2})-(\d{2})T(\d{2}:\d{2}:\d{2})Z'
        regex2 = r'(\d{2}):(\d{2}):(\d{2})'
        fechasDeSubida = []
        for item in lista:
            coincidencia1 = re.match(regex, item)
            if coincidencia1:   
                fechaSeparada = list(coincidencia1.groups())
                coincidencia2 = re.match(regex2, fechaSeparada[3])
                if coincidencia2:
                    hora = list(coincidencia2.groups())
                    gmt = int(hora[0])
                    fechaSeparada[3] = f"{gmt-5}:{hora[1]}:{hora[2]}"
                else:
                    print('problema al formatear la hora')
                fechasDeSubida.append(f"{fechaSeparada[2]}/{fechaSeparada[1]}/{fechaSeparada[0]} {fechaSeparada[3]}")
            else: 
                print("problema al formatear la fecha")
                
        return fechasDeSubida
                
            