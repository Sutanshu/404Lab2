import socket

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHst: www.google.com\r\n\r\n"


def connect(address):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        data = s.recv(BUFFER_SIZE)
        print(data)
    except Exception as error:
        print(error)
    finally:
        s.close()


def main():
    connect(("127.0.0.1", 8001))


if __name__ == "__main__":
    main()
