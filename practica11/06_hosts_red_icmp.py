# Ejercicio 6: hosts iniciados
# Escribe un script que reciba una red en notación CIDR y la escanee buscando máquinas
# que estén encendidas. Para ello NO se podrá llamar a ningún comando externo como nmap o
# ping, pero sí utilizar cualquier librería que nos proporcione cualquier funcionalidad útil.
# Para enumerar las máquinas de la red será obligatorio utilizar la librería ipaddress.
#
#   Víctor Manuel Andreu

# por alguna razón este script falla en la red virtual de libvirt

import ipaddress
import sys
from scapy.all import ICMP, IP, sr, conf

# escanea la red especificada usando ICMP
def scan_network_icmp_fast(network_cidr):
    
    network = ipaddress.ip_network(network_cidr, strict=False)
    print(f"Escaneando la red {network_cidr} con ICMP...")

    ip_list = [str(ip) for ip in network.hosts()]  # Lista de IPs a escanear

    # enviamos paquetes ICMP a todas las ips al mismo tiempo
    packets = [IP(dst=ip) / ICMP() for ip in ip_list]
    answered, _ = sr(packets, timeout=1, verbose=False)  # envío masivo

    active_hosts = [rcv.src for snd, rcv in answered]

    
    # for ip in active_hosts:
    #     print(f"Host activo -> IP: {ip}")

    return active_hosts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: sudo python3 scan_icmp_fast.py <red/CIDR>")
        sys.exit(1)

    network_cidr = sys.argv[1]
    active_hosts = scan_network_icmp_fast(network_cidr)

    # resultado
    print("\nResumen de Hosts Activos:")
    for host in active_hosts:
        print(host)
