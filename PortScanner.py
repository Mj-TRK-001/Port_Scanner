import socket
import argparse


def port_scan(target_ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()


if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Port scanner Tool")
    parser.add_argument("target_ip",type=str, help="Target IP address to scan")
    parser.add_argument("start_port",type=int, help="Start port of the scan range")
    parser.add_argument("end_port",type=int, help="End port of the the scan range")

    args = parser.parse_args() #Parse the arguments

    port_scan(args.target_ip, args.start_port, args.end_port)

#target_ip = "10.10.X.X" #Change This
#port_scan(target_ip,1, 1000)