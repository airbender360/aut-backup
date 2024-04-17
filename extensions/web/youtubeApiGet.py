from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class YoutubeApiGet:
    apikey = 'AIzaSyAQHm8oLKXDbFfv6ox45Vaqzp-pKn4zcQc'
    
    def __init__(self, id):
        global youtube
        youtube = build('youtube', 'v3', developerKey=YoutubeApiGet.apikey)
        self.playlistId = id
    
    def obtenerDatosPlaylist(self):
        respuesta = youtube.playlists().list(
        part='snippet',
        id=self.playlistId
        ).execute()
        nombrePlaylist = respuesta['items'][0]['snippet']['title']
        datosVideos = youtube.playlistItems().list(
            part='contentDetails,snippet',
            playlistId=self.playlistId,
            maxResults=120
        ).execute()
        
        fechas = []
        nombres = []
        for elemento in datosVideos['items']:
            try:
                fechaPub = elemento['contentDetails']['videoPublishedAt']
                nombreVid = elemento['snippet']['title']
                nombres.append(nombreVid)
                fechas.append(fechaPub)
            except KeyError:
                continue

        return nombrePlaylist, fechas, nombres