import sys
import socket

import argument_parser as pars
import server_connection as con

# Getting arguments
args = pars.getArgs()

user = args.user
server_ip, server_port = args.server_ip, args.server_port
client_ip, client_port = args.client_ip, args.client_port
timeout = args.timeout

'''
    Connection
'''
try:
    # Sets timeout
    socket.setdefaulttimeout(timeout)
    # Starting connections
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_tcp.connect((server_ip, server_port))
    sock_udp.bind((client_ip, client_port))
    # helloiam <usuario>
    con.checkUserName(sock_tcp, user)
    print("\n- Usuario:", user)
    # msglen
    size = con.getMessageLength(sock_tcp)
    print("- Tamaño del mensaje:", size)
    # givememsg
    con.askForMessage(sock_tcp, client_port)
    message = con.getMessage(sock_udp, client_port)
    # chkmsg
    con.checkMessage(sock_tcp, message)
    print("- Mensaje:", message.decode('utf-8'))
    # bye
    con.closeConnection(sock_tcp, sock_udp)

except socket.timeout:
    print(f'\nERROR: Error de conexión, intente nuevamente más tarde')
except ConnectionRefusedError:
    print(f'\nERROR: Conexión fallida. Revise los datos e intente nuevamente')
except con.CommandFailedException as exc:
    print(f'\n{exc.data}')
    print(f'ERROR: Un comando falló durante la ejecución. Revise los datos e intente nuevamente')
except Exception as exc:
    print('ERROR:', exc)