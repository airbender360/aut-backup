from script import Script

#Se cambia cada ejecución
linkPlaylist = r'https://www.youtube.com/playlist?list=PLM5IaC7oTKAWcX79aQjjbTu4HMU14SqjD'
#Se cambia solo una vez
rutaCarpeta = r'D:\videos'  #Ruta de la carpeta 'main' donde se guardarán las subcarpetas
rutaExcel = r'D:\aut-backup\tools' #Ruta 'main' del archivo de Excel (ajustar nombre en clase excel/self.ruta)

script = Script(linkPlaylist, rutaCarpeta, rutaExcel)
script.main(1) #0 Como argumento para omitir la descarga de los videos








#---------------------------------------------------------------------------------------------------------------------
# if error, use in console to download manually then document manually, replace "directory" and "playlist-link" below:
# yt-dlp -o "directory\%(title)s.%(ext)s" playlist-link
# example:
# yt-dlp -o "D:\videos\test\%(title)s.%(ext)s" https://www.youtube.com/playlist?list=PLM5IaC7oTKAWcX79aQjjbTu4HMU14SqjD