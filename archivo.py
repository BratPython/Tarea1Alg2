class Archivo:
    def __init__(self, nombre):
        #Inicializacion de la clase Archivo
        self.nombre = nombre
        self.cont = self.leer_contenido()
    
    def leer_contenido(self):
        #Lee el contenido del archivo
        try:
            with open(self.nombre, 'r') as archivo:
                return archivo.read() #Abrir archivo en modo lectura y retorna contenido
        except FileNotFoundError:
            return "El archivo no existe."

    def __str__(self):
        #Convierte el objeto de tipo Archivo a una cadena
        return f'Archivo: {self.nombre}, Contenido: {self.informacion[:30]}...'   