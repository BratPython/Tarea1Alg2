from rama import Rama
from commit import Commit
class Repositorio:
    
    def __init__(self, nombre):
        #Inicializacion de la clase repositorio
        self.nombre = nombre
        self.ramas = {}
        self.ramaEscogida = None
        self.crearRama("main")
    
    def crearRama(self, nombre):
        #Crear nueva rama
        ramaNueva = Rama(nombre)
        self.ramas[nombre] = ramaNueva
        if not self.ramaEscogida:
            self.ramaEscogida = ramaNueva
            
    def cambiarRama(self, nombre):
        #Cambia la rama actual por otra rama
        if nombre in self.ramas:
            self.ramaEscogida = self.ramas[nombre]
        else:
            print(f"La rama '{nombre}'  no existe")
    
    
    def commitARama(self, mensaje, archivos, autor):
        #Crea un nuevo commit en la rama seleccionada
        commitID = len(self.ramaEscogida.commits) + 1
        commitNuevo = Commit(commitID, mensaje, archivos, autor)
    
    def historialDeCommits(self):
        #Muestra el historial de commits de la rama seleccionada
        historial = []
        for rama in self.ramas.values():
            historial.extend(rama.commits)
        historial.sort(key=lambda commit: commit.timestamp, reverse=True)
        return historial

    def __str__(self):
        #Convierte el objeto de tipo Repositorio a una cadena
        ramas = ", ".join(self.ramas.keys())
        return (f'Repositorio: {self.nombre}\n'
                f'Ramas: {ramas}\n'
                f'Rama actual: {self.ramaEscogida.nombre if self.ramaEscogida else "Ninguna"}\n')