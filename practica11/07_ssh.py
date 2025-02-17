# Ejercicio 7: SSH
# Escribe un script que reciba una lista de servidores Linux y para cada uno de ellos se
# conecte por SSH y ejecutando comandos del sistema muestre la siguiente información:
#   • Dirección IP.
#   • Nombre de máquina.
#   • Machine-id (se puede obtener tanto del fichero /etc/machine-id como del comando
#     hostnamectl).
#   • Distro y versión.
#   • Procesador.
#   • Tiempo que la máquina lleva encendida.
#   • Carga en el último minuto, últimos cinco minutos y últimos quince.
#   • Memoria total y memoria libre.
#   • Versión de SSH instalada.
#
# Victor Manuel Andreu Felipe


import paramiko
import sys

# conectamos a una lista de servidores por SSH usando autenticación con clave

def get_server_info(host):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        client.connect(hostname=host, username='root', timeout=5)

        # definimos la lista de comandos a pasar para la info del server
        commands = {
            "Dirección IP": "hostname -I | awk '{print $1}'",
            "Nombre de máquina": "hostname",
            "Machine-id": "cat /etc/machine-id",
            "Distro y versión": "cat /etc/os-release | grep -E 'PRETTY_NAME' | cut -d '=' -f2 | tr -d '\"'",
            "Procesador": "lscpu | grep 'Nombre del modelo' | awk -F: '{print $2}' | sed 's/^ *//'",
            "Tiempo encendido": "uptime -p",
            "Carga": "uptime | awk -F'load average:' '{print $2}'",
            "Memoria Total": "free -h | grep 'Mem:' | awk '{print $2}'",
            "Memoria Libre": "free -h | grep 'Mem:' | awk '{print $7}'",
            "Versión de SSH": "ssh -V 2>&1 | awk '{print $1, $2}'"
        }
        
        print(f"\n Conectado a {host}...")
        for key, cmd in commands.items():
            stdin, stdout, stderr = client.exec_command(cmd)
            output = stdout.read().decode().strip()
            print(f"{key}: {output}")

        client.close()
    except Exception as e:
        print(f"Error al conectar con {host}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python ssh_info_gather.py <lista_servidores.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, "r") as file:
        servers = [line.strip() for line in file.readlines() if line.strip()]

    for server in servers:
        get_server_info(server)

