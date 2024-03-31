from script import Script

#Se cambia cada ejecución
linkPlaylist = r"https://www.youtube.com/playlist?list=PLAKTtN7vEpnjZROtvOInkx2m3iBrpsrBj"
#Se cambia solo una vez
rutaCarpeta = r'D:\videos'  #Ruta de la carpeta 'main' donde se guardarán las subcarpetas
rutaExcel = r'D:\aut-backup\tools' #Ruta 'main' del archivo de Excel (ajustar nombre en clase excel/self.ruta)

script = Script(linkPlaylist, rutaCarpeta, rutaExcel)
script.main()