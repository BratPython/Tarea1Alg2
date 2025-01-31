class Rama:
    def __init__(self, nombre):
        #Inicializacion de la clase Rama
        self.nombre = nombre
        self.commits = []
        self.head = None 
    
    def agregar(self, commit):
        #Agrega un commit a la rama y actualizar el head
        self.commits.append(commit)
        self.head = commit
        
    def historial(self):
        #Retorna la lista de los commits con la fecha en la que se realizaron los cambios
        return sorted(self.commits, key=lambda commit: commit.timestamp, reverse=True)
    
    def __str__(self):
        #Convierte el objeto de tipo Rama a una cadena
        return(f'Rama: {self.nombre}\n'
                f'Head: {self.head.commitID if self.head else "None"}\n'
                f'Commits: {[commit.commitID for commit in self.commits]}')