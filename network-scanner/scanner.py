import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

if __name__ == "__main__":
    scan_ports("127.0.0.1", 1, 1024)