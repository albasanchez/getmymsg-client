import argparse

# Constants
DEFAULT = {
  'user': "assanchez.17",
  'server_ip': "10.2.126.2",
  'server_port': "19876",
  'client_ip': "10.2.126.102",
  'client_port': "6789",
  'time': "20",
}

# Functions
def getArgs():
  parser = argparse.ArgumentParser(description='Obtener un mensaje personalizado del servidor.')
  parser.add_argument("-u", "--user", help="Nombre del usuario (Por defecto: assanchez.17)", default=DEFAULT['user'])
  parser.add_argument("-Si", "--server_ip", help="IP del servidor (Por defecto: 10.2.126.2)", default=DEFAULT['server_ip'])
  parser.add_argument("-Sp", "--server_port", help="Puerto TCP del servidor (Por defecto: 19876)", default=DEFAULT['server_port'], type=int)
  parser.add_argument("-Ci", "--client_ip", help="IP del cliente (Por defecto: 10.2.126.102)", default=DEFAULT['client_ip'])
  parser.add_argument("-Cp", "--client_port", help="Puerto UDP del cliente (Por defecto: 6789)", default=DEFAULT['client_port'], type=int)
  parser.add_argument("-t", "--timeout", help="Tiempo máximo de espera para recibir el mensaje (Por defecto: 20)", default=DEFAULT['time'], type=int)
  return parser.parse_args()