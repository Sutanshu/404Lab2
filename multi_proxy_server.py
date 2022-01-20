import socket, sys
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        sys.exit()

    print(f"IP Address of {host} is {remote_ip}")
    return remote_ip


def main():
    host = "www.google.com"
    port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)

        while True:
            conn, addr = proxy_start.accept()

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                remote_ip = get_remote_ip(host)
                proxy_end.connect((remote_ip, port))
                p = Process(target=handle_proxy_server, args=(proxy_end, conn))
                p.daemon = True
                p.start()
                print("Process started: ", p)

            conn.close()


def handle_proxy_server(proxy_end, conn):
    sendFData = conn.recv(BUFFER_SIZE)
    proxy_end.sendall(sendFData)
    proxy_end.shutdown(socket.SHUT_WR)
    data = proxy_end.recv(BUFFER_SIZE)
    print(data)
    conn.send(data)


if __name__ == "__main__":
    main()
