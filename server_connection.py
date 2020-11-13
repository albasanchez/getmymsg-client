import re
import base64
from hashlib import md5

# Constants
BUFFER_SIZE = 1024
PETITION_MAX_TIMES = 5

# Classes
class CommandFailedException(Exception):
    """
    Exception para lanzar al fallar la ejecución del commando
    """
    def __init__(self, data):
        self.data = data

# Functions
def checkUserName(socket, username):
    socket.send(f'helloiam {username}'.encode('utf-8'));
    data = socket.recv(BUFFER_SIZE).decode('utf-8').rstrip('\n')
    if (data != 'ok'):
        raise CommandFailedException(f'(helloiam) {data}')

def getMessageLength(socket):
    socket.send('msglen'.encode('utf-8'));
    data = socket.recv(BUFFER_SIZE).decode('utf-8')
    sizes = re.findall(r'\d+', data)
    if (len(sizes) == 0):
        raise CommandFailedException(f'(msglen) {data}')
    return sizes[0]

def askForMessage(socket, udp_port):
    socket.send(f'givememsg {udp_port}'.encode('utf-8'));
    data = socket.recv(BUFFER_SIZE).decode('utf-8').rstrip('\n')
    if (data != 'ok'):
        raise CommandFailedException(f'(givememsg) {data}')

def getMessage(socket_udp, udp_port):
    udp_data = ""
    petition_number = 0
    while petition_number < PETITION_MAX_TIMES:
        udp_data, addr = socket_udp.recvfrom(1024)
        petition_number = + 1
        if (udp_data != ""):
            break
    return base64.b64decode(udp_data)

def checkMessage(socket, message):
    socket.send(f'chkmsg {md5(message).hexdigest()}'.encode('utf-8'));
    data = socket.recv(BUFFER_SIZE).decode('utf-8').rstrip('\n')
    if (data != 'ok'):
        raise CommandFailedException(f'(chkmsg) {data}')

def closeConnection(socket_tcp, socket_udp):
    socket_tcp.send('bye'.encode('utf-8'));
    data = socket_tcp.recv(BUFFER_SIZE)
    socket_udp.close()
