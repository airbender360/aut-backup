from script import Script

#Se cambia cada ejecución
linkPlaylist = r"https://www.youtube.com/playlist?list=PLM5IaC7oTKAXeqPdMD37v_7JjTQyVTnQT"
#Se cambia solo una vez
rutaCarpeta = r'C:\Users\063\Desktop\videos\playlist'  #Ruta de la carpeta 'main' donde se guardarán las subcarpetas
rutaExcel = r'C:\Users\063\Desktop\backupScripts\api\tools' #Ruta 'main' del archivo de Excel (ajustar nombre en clase excel/self.ruta)

script = Script(linkPlaylist, rutaCarpeta, rutaExcel)
script.main()