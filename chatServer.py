#create server
import socket
host = ''
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(('',1234))
s.listen(10)
#connect client and print if connected
#byter(text,"utf-8") uses string for socket
client, client_address = s.accept()
print("Client has connected with address: {}".format(client_address))

while True:
    messg = input("Send to client:")
    client.send(messg.encode())
    #client.sendall(bytes("{} {}\n".format(player1.x,player1.y),"utf-8"))
    #get and print data from client
    data = client.recv(1024).decode('utf-8')
    print("From client:",repr(data))
s.close()
