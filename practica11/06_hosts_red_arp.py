# Ejercicio 6: hosts iniciados
# Escribe un script que reciba una red en notación CIDR y la escanee buscando máquinas
# que estén encendidas. Para ello NO se podrá llamar a ningún comando externo como nmap o
# ping, pero sí utilizar cualquier librería que nos proporcione cualquier funcionalidad útil.
# Para enumerar las máquinas de la red será obligatorio utilizar la librería ipaddress.
#
#   Víctor Manuel Andreu

import sys
from scapy.all import ARP, Ether, srp, conf

# Configurar Scapy para evitar mensajes innecesarios
conf.verb = 2

def arp_broadcast_scan(network_cidr):
    """Envía un paquete ARP Broadcast para descubrir hosts en la red."""
    print(f"Enviando ARP Broadcast en {network_cidr}...")

    # Crear paquete ARP broadcast
    arp_request = ARP(pdst=network_cidr)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast / arp_request

    # Enviar el paquete y recibir respuestas
    answered, _ = srp(arp_packet, timeout=2, verbose=False)

    active_hosts = []
    for snd, rcv in answered:
        active_hosts.append((rcv.psrc, rcv.hwsrc))  # IP y MAC del host
        print(f"Host activo -> IP: {rcv.psrc}, MAC: {rcv.hwsrc}")

    return active_hosts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: sudo python3 arp_broadcast_scan.py <red/CIDR>")
        sys.exit(1)

    network_cidr = sys.argv[1]
    active_hosts = arp_broadcast_scan(network_cidr)

    print("\nResumen de Hosts Activos:")
    for ip, mac in active_hosts:
        print(f"{ip} - {mac}")