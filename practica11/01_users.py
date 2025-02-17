# Ejercicio 1: creación de usuarios
#   Escribe un script que reciba un nombre de grupo (ejemplo: asir1) por línea de
#   parámetros y realice las siguientes tareas:
#   • Compruebe que el grupo no exista. En ese caso:
#       • Asigne un GID libre desde el 8000 en adelante, si el 8000 y el 8001 están
#       ocupados, deberá asignar el 8002.
#       • Cree el grupo asir1 con el GID asignado utilizando el comando groupadd.
#   • Cree 100 usuarios (UPG) utilizando el comando useradd, desde asir1-00 hasta asir1-
#   99. Además deberá:
#       • Fijar changeme como contraseña.
#       • Añadir al usuario al grupo asir1.
#       • Crear en el directorio HOME un fichero de bienvenida al sistema llamado
#       welcome.ASIR1.user.txt.
#
#   Víctor Manuel Andreu Felipe 2025

import os
import subprocess
import sys

# buscamos los gid existentes a partir del 8000 hasta encontrar uno libre
def get_next_free_gid(start_gid=8000):
    existing_gids = {int(line.split(':')[2]) for line in open('/etc/group')}
    while start_gid in existing_gids:
        start_gid += 1
    return start_gid

# comprobamos que el grupo exista
def group_exists(group_name):
    try:
        subprocess.run(["getent", "group", group_name], check=True, stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

# creamos el grupo con el id correcto
def create_group(group_name, gid):
    subprocess.run(["sudo", "groupadd", "-g", str(gid), group_name], check=True)
    print(f"Grupo '{group_name}' creado con GID {gid}.")

# creación de usuarios con su home y grupo adecuado
def create_user(username, group_name):
    subprocess.run(["sudo", "useradd", "-m", "-G", group_name, username], check=True)
    
    # asignacion de password con chpasswd a changeme
    subprocess.run(["sudo", "chpasswd"], input=f"{username}:changeme\n".encode(), check=True)
    
    # creación de fichero de bienvenida
    home_dir = f"/home/{username}"
    welcome_file = os.path.join(home_dir, f"welcome.{group_name}.{username}.txt")
    with open(welcome_file, "w") as f:
        f.write(f"Bienvenido al sistema, {username}!\n")
    subprocess.run(["sudo", "chown", f"{username}:{username}", welcome_file])
    print(f"Usuario '{username}' creado y añadido a '{group_name}'.")

def main():
    if len(sys.argv) != 2:
        print("Uso: sudo python3 create_users_group.py <nombre_grupo>")
        sys.exit(1)

    group_name = sys.argv[1]

    # comprobación de grupo
    if group_exists(group_name):
        print(f"El grupo '{group_name}' ya existe.")
        sys.exit(1)

    gid = get_next_free_gid()
    create_group(group_name, gid)

    # iteración de usuarios
    for i in range(100):
        username = f"{group_name}-{i:02d}"
        create_user(username, group_name)

    print("Proceso de creación completado.")

if __name__ == "__main__":
    main()
