import socket
import threading
 
PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
print(ADDRESS)
FORMAT = "utf-8"
 
# Data example

"""
{
    "Grupo 1': {
        "criador": "João",
        "cliente": "Cliente 1".
        participantes: [
            "João",
        ]
        "mensagens": [
            {
                "nick": "João",
                "mensagem": "Olá, tudo bem?"
            }
        ]
    }
}
"""

data = {}

clients, names = [], []
 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS)
 
# Lists that will contains
# all the clients connected to
# the server and their names.
clients, names = [], []
 
# Create a new socket for
# the server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
# bind the address of the
# server to the socket
server.bind(ADDRESS)
 
# function to start the connection
def start_chat():
   
    print(f"Servidor funcionando no endereço: {ADDRESS[0]}:{ADDRESS[1]}")
     
    # listening for connections
    server.listen()
     
    while True:
       
        # accept connections and returns
        # a new connection to the client
        #  and  the address bound to it
        conn, addr =  server.accept()
        # conn.send("NAME".encode(FORMAT))
         
        # 1024 represents the max amount
        # of data that can be received (bytes)
        name = conn.recv(1024).decode(FORMAT)
         
        # append the name and client
        # to the respective list
        names.append(name)
        clients.append(conn)
         
        print(f"O nome é :{name}")
         
        # broadcast message
        broadcast_message(f"{name} entrou no chat!\n".encode(FORMAT))
         
        conn.send('Conexão feita!'.encode(FORMAT))
         
        # Start the handling thread
        thread = threading.Thread(target = handle,
                                  args = (conn, addr))
        thread.start()
         
        # no. of clients connected
        # to the server
        print(f"Qtd de conexões ativas {threading.activeCount()-1}")
 
# method to handle the
# incoming messages
def handle(conn, addr):
   
    print(f"Nova conexão {addr}")
    connected = True
     
    while connected:
          # receive message
        message = conn.recv(1024)
         
        # broadcast message
        broadcast_message(message)
     
    # close the connection
    conn.close()
 
# method for broadcasting
# messages to the each clients
def broadcast_message(message):
    for client in clients:
        client.send(message)
 
def handle_message(message, conn):
    if message.startswith("GROUP_"):
        group = message.split("_")[1]
        nick = message.split("_")[3]
        print(f"{nick} criou o grupo {group}")
        data[group] = {}
        data[group]["criador"] = nick
        data[group]["participantes"] = []
        data[group]["participantes"].append(nick)
        data[group]["mensagens"] = []
        data[group]["cliente"] = conn

    print(data)
    
# call the method to
# begin the communication
start_chat()
