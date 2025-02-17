# Ejercicio 3: creación y modificación de ficheros
#   Inotify es una API del kernel de Linux que permite a las aplicaciones monitorizar en
#   tiempo real los cambios que ocurren en el sistema de ficheros. Esto incluye eventos como la
#   creación, modificación, eliminación o movimiento de archivos y directorios.
#   Entre sus características principales destacan:
#       • Monitorización en tiempo real: permite recibir notificaciones inmediatas cuando se
#       produce algún cambio en el sistema de archivos, evitando la necesidad de realizar
#       consultas periódicas (polling).
#       • Eficiencia: al ser una API basada en eventos, inotify reduce el consumo de recursos ya
#       que el sistema notifica solo cuando se detecta un cambio, en lugar de tener que revisar
#       constantemente el estado del sistema de ficheros.
#       • Facilidad de integración: varios lenguajes de programación, incluyendo Python, tienen
#       librerías que facilitan el uso de inotify. En el caso de Python se pueden utilizar módulos
#       como pyinotify o inotify_simple para integrar esta funcionalidad en cualquier
#       script.
#   Escribe un script que muestre un mensaje en pantalla cada vez que se cree o se modifique
#   un fichero en cualquier subdirectorio bajo /etc.
#
#   Víctor Manuel Andreu Felipe


import inotify.adapters


# monitorización del directorio etc
def monitor_directory(path="/etc"):
    notifier = inotify.adapters.InotifyTree(path)
    print(f"Monitoreando cambios en {path}...")
    
    try:
        for event in notifier.event_gen(yield_nones=False):
            (_, type_names, path, filename) = event
            
            # avisa cuando se crea o modifica un fichero
            if "IN_CREATE" in type_names:
                print(f"[CREADO] {path}/{filename}")
            elif "IN_MODIFY" in type_names:
                print(f"[MODIFICADO] {path}/{filename}")
    except KeyboardInterrupt:
        print("Monitorización finalizada.")

if __name__ == "__main__":
    monitor_directory()
