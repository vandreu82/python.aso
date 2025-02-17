import paramiko
import sys
import sqlite3
import datetime

# crea la base de datos y la tabla si no existen

def setup_database():   
    conn = sqlite3.connect("server_info.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_info (
            ip TEXT PRIMARY KEY,
            hostname TEXT,
            machine_id TEXT,
            distro TEXT,
            processor TEXT,
            uptime TEXT,
            load_avg TEXT,
            mem_total TEXT,
            mem_free TEXT,
            ssh_version TEXT,
            last_update TEXT
        )
    ''')
    conn.commit()
    conn.close()


# guarda o actualiza la información del servidor en la base de datos
def save_server_info(data):
    conn = sqlite3.connect("server_info.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO server_info (ip, hostname, machine_id, distro, processor, uptime, load_avg, mem_total, mem_free, ssh_version, last_update)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(ip) DO UPDATE SET
            hostname=excluded.hostname,
            machine_id=excluded.machine_id,
            distro=excluded.distro,
            processor=excluded.processor,
            uptime=excluded.uptime,
            load_avg=excluded.load_avg,
            mem_total=excluded.mem_total,
            mem_free=excluded.mem_free,
            ssh_version=excluded.ssh_version,
            last_update=excluded.last_update
    ''', data[:11])  # raro, me decía que estaba mandado 12 valores
    conn.commit()
    conn.close()

def get_server_info(host):
    # se conecta a un servidor por SSH usando autenticación con clave y obtiene información del sistema
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()
        client.connect(hostname=host, username='root', timeout=5)

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
        data = [host]
        for key, cmd in commands.items():
            stdin, stdout, stderr = client.exec_command(cmd)
            output = stdout.read().decode().strip()
            print(f"{key}: {output}")
            data.append(output)
        
        data.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        save_server_info(data)
        client.close()
    except Exception as e:
        print(f"Error al conectar con {host}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python ssh_info_gather.py <lista_servidores.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    setup_database()
    
    with open(file_path, "r") as file:
        servers = [line.strip() for line in file.readlines() if line.strip()]

    for server in servers:
        get_server_info(server)
