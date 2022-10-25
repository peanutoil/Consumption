#create server
import socket
host = ''
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0",1234))
s.listen(10)
#connect client and print if connected
client, client_address = s.accept()
print("Client has connected with address: {}".formar(client_address))
#byter(text,"utf-8") uses string for socket
client.sendall(bytes("{} {}\n".formal(player1.x,player1.y),"utf-8"))
