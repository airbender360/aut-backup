from extensions.web.youtubeApiGet import YoutubeApiGet
import re

class Playlist():
    def __init__(self, link):
        regex = r'(?<=list=)([\w-]+)' # si la estructura de los enlaces cambia, actualización necesaria
        self.id = re.findall(regex, link)
        self.youtubeapiget = YoutubeApiGet(self.id[0])
        self.nombrePlaylist, self.fechas, self.nombres = self.youtubeapiget.obtenerDatosPlaylist()
        
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
                    zona = 5
                    flag = 0
                    if gmt < zona:
                        gmt = gmt + 24
                        if fechaSeparada[2] == '01':
                            if fechaSeparada[1] in ['01', '03', '05', '07', '08', '10', '12']:
                                fechaSeparada[2] = '31'
                                if fechaSeparada[1] == '01':
                                    fechaSeparada[1] = '12'
                                    flag = 1
                            elif fechaSeparada[1] in ['04', '06', '09', '11']:
                                fechaSeparada[2] = '30'
                            elif fechaSeparada[1] == '02':
                                if (int(fechaSeparada[0]) % 4 == 0 and int(fechaSeparada[0]) % 100 != 0) or (int(fechaSeparada[0]) % 400 == 0):
                                    fechaSeparada[2] = '29'
                                else:
                                    fechaSeparada[2] = '28'
                            if flag != 1:
                                if int(fechaSeparada[1]) < 10:
                                    fechaSeparada[1] = f"0{str(int(fechaSeparada[1])-1)}"
                                else:
                                    fechaSeparada[1] = str(int(fechaSeparada[1])-1)
                        else:
                            fechaSeparada[2] = str(int(fechaSeparada[2])-1)
                    fechaSeparada[3] = f"{gmt-zona}:{hora[1]}:{hora[2]}"
                else:
                    print('Problema al formatear la hora')
                fechasDeSubida.append(f"{fechaSeparada[2]}/{fechaSeparada[1]}/{fechaSeparada[0]} {fechaSeparada[3]}")
            else:
                print("Problema al formatear la fecha")
        return fechasDeSubida
                
    def datosVideos(self):
        try:
            fechasOrdenadas = self.ordenarFechasDeSubida(self.fechas)
            videos = dict(zip(self.nombres, fechasOrdenadas))
        except Exception as e:
            print(f'error: {e}')
        finally:
            print('2. Extracción Exitosa de Información (API)')
            self.videos = videos