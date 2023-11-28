import openpyxl

class Hoja:
    def __init__(self, ruta, nombre, datos):
        self.ruta = ruta
        self.nombre = nombre
        self.datos = datos 
        self.libro = openpyxl.load_workbook(self.ruta)
        if self.nombre in self.libro.sheetnames:
            print('La hoja ' + self.nombre + " ya existe.")
        else:
            self.hoja = self.libro.create_sheet(self.nombre)
        
    def crearRegistro(self):
        self.hoja['A1'] = 'Nombre de Lista'
        self.hoja['B1'] = 'Nombre del Video'
        self.hoja['C1'] = 'Fecha de Subida (Canal Oficial)'
        self.hoja['D1'] = 'Duración'
        self.hoja['E1'] = 'Tamaño'
        self.hoja['F1'] = 'Calidad'
        self.hoja['G1'] = 'Formato'
        self.hoja['H1'] = 'Descargado Por'
        self.hoja['I1'] = 'Fecha Descarga (Backup)'
        self.hoja['J1'] = 'Enlace YouTube'
        self.hoja['K1'] = 'Enlace Drive'
        self.hoja['L1'] = 'Nota'
        
        for indice, registro in enumerate(self.datos):
            self.hoja['A' + str(indice+2)] = self.nombre
            self.hoja['B' + str(indice+2)] = registro['YouTubeName']
            self.hoja['C' + str(indice+2)] = registro['UploadDate']
            self.hoja['D' + str(indice+2)] = registro['Duration']
            self.hoja['E' + str(indice+2)] = registro['FileSize']
            self.hoja['F' + str(indice+2)] = registro['ImageHeight']
            self.hoja['G' + str(indice+2)] = registro['FileTypeExtension']
            self.hoja['H' + str(indice+2)] = 'Santiago Sánchez'
            self.hoja['I' + str(indice+2)] = registro['FileCreateDate']
        self.libro.save(self.ruta)