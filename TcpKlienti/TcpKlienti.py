from socket import *
import sys
import time


print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("TCP Klienti")
print("-----------------------\n")

serverName = "127.0.0.1"
serverPort = 9000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print ("Zgjedh nje opcion :  \n IP \n PORT \n HOST \n KOHA  \n KENO  \n ")
opcioni = input("")

                
if opcioni=="IP":
    clientSocket.send(opcioni.encode('ASCII'))
    modifiedOpcioni = clientSocket.recv(1024)
    print("From Server:", modifiedOpcioni.decode('ASCII'))
    clientSocket.close()
elif opcioni=="PORT":
    clientSocket.send(opcioni.encode('ASCII'))
    modifiedOpcioni = clientSocket.recv(1024)
    print("From Server:", modifiedOpcioni.decode('ASCII'))
    clientSocket.close()

elif opcioni=="HOST":
    clientSocket.send(opcioni.encode('ASCII'))
    modifiedOpcioni = clientSocket.recv(1024)
    print("From Server:", modifiedOpcioni.decode('ASCII'))
    clientSocket.close()

elif opcioni=="KOHA":
    clientSocket.send(opcioni.encode('ASCII'))
    modifiedOpcioni = clientSocket.recv(1024)
    print("From Server:", modifiedOpcioni.decode('ASCII'))
    clientSocket.close()

elif opcioni=="KENO":
    clientSocket.send(opcioni.encode('ASCII'))
    modifiedOpcioni = clientSocket.recv(1024)
    print("From Server:", modifiedOpcioni.decode('ASCII'))
    clientSocket.close()




   




