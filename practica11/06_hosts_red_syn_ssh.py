import sys
import ipaddress
from scapy.all import IP, TCP, sr, conf

# Configurar Scapy para evitar mensajes innecesarios
conf.verb = 0

def tcp_syn_scan(network_cidr, port=22):
    """Realiza un escaneo TCP SYN en un puerto específico para detectar hosts activos."""
    network = ipaddress.ip_network(network_cidr, strict=False)
    print(f"Escaneando la red {network_cidr} con TCP SYN en el puerto {port}...")

    ip_list = [str(ip) for ip in network.hosts()]  # Lista de IPs a escanear
    packets = [IP(dst=ip) / TCP(dport=port, flags='S') for ip in ip_list]
    
    answered, _ = sr(packets, timeout=1, verbose=False)  # Enviar paquetes SYN
    
    active_hosts = [rcv.src for snd, rcv in answered if rcv.haslayer(TCP) and rcv[TCP].flags & 0x12]
    
    # Mostrar resultados
    for ip in active_hosts:
        print(f"Host activo -> IP: {ip}")

    return active_hosts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: sudo python3 tcp_syn_scan.py <red/CIDR>")
        sys.exit(1)
    
    network_cidr = sys.argv[1]
    active_hosts = tcp_syn_scan(network_cidr)
    
    print("\nResumen de Hosts Activos:")
    for host in active_hosts:
        print(host)