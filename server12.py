import socket
import threading

HEADER = 64
PORT = 1060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

list = []
sockets = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[novy join]{addr} pripojen.")

    list.append(addr)
    print(list)
    print(tuple(list))
    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                sockets.remove(conn)
                connected = False

            print(f"[{addr}] {msg}")

            # conn.send(f"{msg}".encode(FORMAT))
            # conn.send(f"cvgh".encode(FORMAT))
            # conn.sendto(f"{lastmsg}".encode(FORMAT), lastaddr)
            for socket in sockets:
                if socket is not conn:
                    socket.sendall(f"{msg}".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[working] Server funguje na {SERVER}")
    while True:
        conn, addr = server.accept()
        sockets.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[pocet pripojeni] {threading.activeCount() - 1}")

print("[start] server se zapina...")
start()
