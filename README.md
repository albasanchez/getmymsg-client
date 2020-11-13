# getmymsg-client

Cliente elaborado por Alba Sánchez para la Práctica 3 del curso de Sistemas Distribuidos.

## Pasos a seguir

1. Realizar los siguientes comandos para copiar el contenido de este repositorio

   ```bash
   git clone https://github.com/albasanchez/getmymsg-client.git
   cd getmymsg-client
   ```

2. En la carpeta donde se encuentra ejecutar el siguiente comando

   ```bash
   py client.py
   ```

3. En caso de querer modificar los argumentos, puede revisarlos en el apartado [argumentos](#argumentos) o puede observar los mismos ejecutando el siguiente comando

   ```bash
   py client.py -h
   ```

## Argumentos

- **-u** _Nombre del usuario (Por defecto: assanchez.17)_
- **-Si** _IP del servidor (Por defecto: 10.2.126.2)_
- **-Sp** _Puerto TCP del servidor (Por defecto: 19876)_
- **-Ci** _IP del cliente (Por defecto: 10.2.126.102)_
- **-Cp** _Puerto UDP del cliente (Por defecto: 6789)_
- **-t** _Tiempo máximo de espera para recibir el mensaje (Por defecto: 20)_

## Archivos

- **argument_parser** _Obtención de argumentos mediante argparse, indicando los argumentos por defecto_
- **client** _Código del cliente, ejecuta el flujo ideal de la conexión_
- **server_connection** _Funciones que realizan la comunicación con el servidor, utilizando el protocolo establecido_
