import datetime
class Commit:
    def __init__(self, commitID, mensaje, mod, autor):
        #Inicializacion de la clase Commit
        self.mensaje = mensaje
        self.commitID = commitID
        self.timestamp = datetime.datetime.now() #Fecha y hora de creacion del commit
        self.mod = mod #Archivos modificados
        self.autor = autor
        
        def __str__(self):
            #Convierte el objeto de clase Commit a una cadena 
            archivos = ", ".join([archivo.nombre for archivo in self.mod])
            return(f'ID de Commit: {self.commitID}\n' 
                    f'Mensaje: {self.mensaje}\n'
                    f'Fecha: {self.timestamp}\n'
                    f'Archivo(S) modificado(s): {self.mod}\n'
                    f'Autor: {self.autor}')