from tkinter import *
import time
import socket
import sys
port = 1234
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

def start(nameEnter, screen):
    global name
    name = nameEnter.get()
    screen.destroy()
    
def startMenu(soc, host_name, ip):

    screen = Tk()
    screen.title("PickleChat Menu")

    h_ip = host_name + " ({})".format(ip)
    host_ip = Label(screen, text = h_ip)
    host_ip.grid(column = 0, row = 0)

    nameBox = Label(screen, text = "Enter name below:")
    nameBox.grid(column = 0, row = 1)

    nameEnter = Entry(screen, width = 25)
    nameEnter.grid(column = 0, row = 2)

    stb = Button(screen, text = "Start with username above", fg = "blue", command = lambda : start(nameEnter, screen))
    stb.grid(column = 0, row = 3)

    screen.mainloop()
startMenu(soc, host_name, ip)
#--------------------------------------------------------

soc.bind((host_name, port))
print("Username: ",name)
print("Waiting for incoming connections...")
soc.listen(1)
connection, addr = soc.accept()
connection.send(name.encode())
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name, " has joined your PickleChat server")

def chatRoom(soc, connection, addr, port, host_name, ip, name, client_name):
    window = Tk()
    window.title("PickleChat")
    window.geometry("450x700")

    messageBox = Entry(window, width = 48)
    messageBox.grid(column = 0, row = 0)
    
    
    window.mainloop()
    
chatRoom(soc, connection, addr, port, host_name, ip, name, client_name)
