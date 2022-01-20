import socket
from multiprocessing import Pool


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
    address = [(HOST, PORT)]
    # establish how many ever different connections, 2 is easier to see
    with Pool() as p:
        p.map(connect, address * 2)


if __name__ == "__main__":
    main()
