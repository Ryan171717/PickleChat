from tkinter import *
import time
import socket
import sys
port = 1234
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

screen = Tk()
screen.title("PickleChat Menu")

h_ip = host_name + " ({})".format(ip)
host_ip = Label(screen, text = h_ip)
host_ip.grid(column = 0, row = 0)

nameBox = Label(screen, text = "Enter name below:")
nameBox.grid(column = 0, row = 1)

nameEnter = Entry(screen, width = 25)
nameEnter.grid(column = 0, row = 2)

def st():
    start(nameEnter, screen)
def start(nameEnter, screen):
    global name
    name = nameEnter.get()
    screen.destroy()

stb = Button(screen, text = "Start with username above", fg = "blue", command = st)
stb.grid(column = 0, row = 3)

screen.mainloop()

print(name)
soc.bind((host_name, port))

connection, addr = soc.accept()