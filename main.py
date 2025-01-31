import os
from archivo import Archivo
from repositorio import Repositorio

class Main:
    #Inicializa la clase Main
    def __init__(self):
        self.repo = Repositorio("Mi repositorio")
        self.archivos = {}
        self.init_git()
        self.iniciarConsola()
        
    def init_git(self):
        #Inicializa la ruta para el repositorio
        if not os.path.exists(".git"):
            os.mkdir(".git")
            os.makedirs(".git/objects")
            os.makedirs(".git/refs")
            os.makedirs(".git/refs/heads")
            print("Directorio .git creado.")
            
    def guardarComando(self, comando, resultado):
        #Guarda el comando y su resultado en el archivo de log
        with open('.git/log', 'a') as archivo_log:
            archivo_log.write(f"{comando} {resultado}\n")
    
    def iniciarConsola(self):
        #Inicia la consola que recibe los comandos
        print("Git iniciado, 'exit' para salir")
        while True:
            comando = input("Ingrese comando >>").strip()
            if comando == "exit":
                break
            elif comando.startswith("git add"):
                self.gitAdd(comando)
            elif comando.startswith("git commit"):
                self.gitCommit(comando)
            elif comando.startswith("git branch"):
                self.gitBranch(comando)
            elif comando.startswith("git checkout"):
                self.gitCheckout(comando)
            elif comando.startswith("git log"):
                self.gitLog()
            else:
                print("Comando no reconocido.")
    
    def gitAdd(self, comando):
        #Selecciona el archivo escrito y lo carga para modificarlo
        n = comando.split()
        if len(n) == 3:
            nombre = n[2]
            if nombre not in self.archivos:
                archivo = Archivo(nombre)
                self.archivos[nombre] = archivo
                mensaje = f"Archivo '{nombre}' agregado."
                print(mensaje)
            else:
                mensaje = f"Archivo '{nombre}' ya está agregado."
                print(mensaje)
        else:
            mensaje = "Comando no reconocido."
            print(mensaje)

    def gitCommit(self, comando):
    #Metodo que guarda el mensaje de los cambios hechos al archivo seleccionado
        n = comando.split(maxsplit=3)
        if len(n) == 4:
            mensaje = n[3]
            archivosModificados = list(self.archivos.values())
            if archivosModificados:
                self.repo.commitARama(mensaje, archivosModificados, "Admin")
                mensaje = f"Commit realizado con mensaje: '{mensaje}'"
                print(mensaje)
                self.archivos.clear()
            else:
                mensaje = "No hay archivos para hacer commit."
                print(mensaje)
        else:
            mensaje = "Comando no conocido"
            print(mensaje)

    def gitBranch(self, comando):
        #Metodo que crea ramas con el nombre escogido 
        n = comando.split()
        if len(n) == 3:
            nombre = n[2]
            self.repo.crearRama(nombre)
            mensaje = f"Rama '{nombre}' creada."
            print(mensaje)
        else:
            mensaje = "Comando no conocido"
            print(mensaje)
        self.guardarComando(comando, mensaje)
        
    def gitCheckout(self, comando):
    #Cambia la rama de trabajo para trabajar en otra
        partes = comando.split()
        if len(partes) == 3:
            nombre_rama = partes[2]
            self.repo.cambiarRama(nombre_rama)
            mensaje = f"Rama seleccionada: '{nombre_rama}'."
            print(mensaje)
        else:
            mensaje = "Comando no conocido."
            print(mensaje)
        self.guardarComando(comando, mensaje)

    def gitLog(self):
    #Muestra todos los commits realizados
        try:
            historial = self.repo.historialDeCommits()
            if historial:
                print("Historial de commits:")
                for commit in historial:
                    print(commit)
                    print("="*20)
            else:
                print("No hay commits en el historial.")
        except FileNotFoundError:
            print("No hay historial de commits.")
            
Main()
