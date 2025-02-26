import socket

def port_scanner(target, ports):

    print(f"[*] {target} scaning")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((target, port)) == 0:
                    print(f"[+] port {port}is open!")
        except Exception as e:
            print(f"[-] port {port} error: {e}")


target_ip = 'IP'
ports_to_scan = range(1, 1025)
port_scanner(target_ip, ports_to_scan)
