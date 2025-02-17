# Ejercicio 5: procesamiento de ficheros de logs
# Escribe un script que reciba como parámetro un fichero de logs de Nginx, como por
# ejemplo /var/log/nginx/access.log, y muestre una estadística mostrando el número de
# visitas que el servidor recibe por IP, ordenado de mayor a menor número de visitas.
#
#   Víctor Manuel Andreu Felipe 2025

import sys
import collections

# procesa un archivo de logs de Nginx y muestra la lista de ip ordenadas por visitas
def process_nginx_log(log_file):
    ip_counts = collections.Counter()
    try:
        with open(log_file, 'r') as file:
            for line in file:
                parts = line.split()
                if parts:
                    ip = parts[0]  # la ip está en el primer campo del log
                    ip_counts[ip] += 1
    # comprobación de excepciones
    except FileNotFoundError:
        print(f"Error: El archivo {log_file} no existe.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: No tienes permisos para leer {log_file}.")
        sys.exit(1)
    
    # ordenación de las ips
    sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
    
    print("IP Address | Visit Count")
    print("--------------------------------")
    for ip, count in sorted_ips:
        print(f"{ip} | {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python nginx_log_stats.py <ruta_del_log>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    process_nginx_log(log_file)
