import socket
import threading
import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

HEADER = 64
#PORT = 16740
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER = '3.127.181.115'
SERVER = socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(None)
client.connect(ADDR)



print('Tvůj nick: ')
name = input() 
print('Zpráva: ')

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def recvv():
    while 1:
        print(client.recv(2048).decode(FORMAT))

thread = threading.Thread(target=recvv)
thread.start()

while 1:
    try:
        msg1 = input()
        delka = len(msg1)
        space = " "
        for i in range (delka):
            space  = space + " " 

        print("\033[A" + space + "\033[A")
        send("\n  "+name+": "+msg1)
    except KeyboardInterrupt:
        send("\n  "+name+": "+DISCONNECT_MESSAGE)