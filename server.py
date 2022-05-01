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
server.listen()
 
# function to start the connection
def startChat():
   
    print("server is working on " + SERVER)
     
    while True:
        try:
       
            # accept connections and returns
            # a new connection to the client
            #  and  the address bound to it
            conn, addr =  server.accept()
            
            # 1024 represents the max amount
            # of data that can be received (bytes)
            message = conn.recv(1024).decode(FORMAT)
            
            handle_message(message, conn)
            
            conn.send('Connection successful!'.encode(FORMAT))
            
            # Start the handling thread
            thread = threading.Thread(target = handle,
                                    args = (conn, addr))
            thread.start()
            
            # no. of clients connected
            # to the server
            print(f"active connections {threading.activeCount()-1}")
        
        except KeyboardInterrupt:
            print("\nErro! Server is closed")
            server.close()
 
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

# method to handle the
# incoming messages
def handle(conn, addr):
   
    print(f"new connection {addr}")
    connected = True
    
    try:
        while connected:
            # receive message
            message = conn.recv(1024)

            handle_message(message, conn)

            print(message)
            
            # broadcast message
            broadcastMessage(message)
        
        # close the connection
        conn.close()
    except:
        print("Erro ao lidar com mensagem do cliente")
        server.close()
        exit()
 
# method for broadcasting
# messages to the each clients
def broadcastMessage(message):
    try:
        for client in clients:
            client.send(message)
    except:
        print("Erro ao enviar mensagem")
        server.close()
        exit()
 
# call the method to
# begin the communication
try:
    startChat()
except KeyboardInterrupt:
    print("\nServer is closed")
    server.close()
    exit()