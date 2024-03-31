from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class YoutubeApiGet:
    apikey = ''
    
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
        
        fechas = [elemento['contentDetails']['videoPublishedAt'] for elemento in datosVideos['items']]
        nombres = [elemento['snippet']['title'] for elemento in datosVideos['items']]

        return nombrePlaylist, fechas, nombres