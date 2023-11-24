from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class YoutubeApiGet:
    apikey = 'AIzaSyAxtPrNEo4n5S9qvOWs8CLid2UbRDVZQu0'
    
    def __init__(self, id):
        global youtube
        youtube = build('youtube', 'v3', developerKey=YoutubeApiGet.apikey)
        self.playlistId = id
    
    def obtenerNombre(self):
        respuesta = youtube.playlists().list(
        part='snippet',
        id=self.playlistId
        ).execute()
        
        playlistName = respuesta['items'][0]['snippet']['title']
        return playlistName
    
    def obtenerDatosVideos(self):
        fechasDeSubida = []
        nombresVideos = []
        respuesta = youtube.playlistItems().list(
            part='contentDetails, snippet',
            playlistId=self.playlistId,
            maxResults=150
        ).execute()
        
        for elemento in respuesta['items']:
            fechasDeSubida.append(elemento['contentDetails']['videoPublishedAt'])
            nombresVideos.append(elemento['snippet']['title'])
        return fechasDeSubida, nombresVideos