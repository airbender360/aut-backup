from script import Script

linkPlaylist = r"https://www.youtube.com/playlist?list=PLAKTtN7vEpniX15TkDhNkhTaJFpdpBSm_"
rutaCarpeta = r'C:\Users\063\Desktop\videos\playlist'
rutaExcel = r'C:\Users\063\Desktop\backupScripts\tools\bd.xlsx'

script = Script(linkPlaylist, rutaCarpeta, rutaExcel)
script.webEnMetadata()
script.documentarExcel()