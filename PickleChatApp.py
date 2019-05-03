# import all necesary modules
from tkinter import *
import socket
import sys
import time
import thread
#create a port to communicate on
port = 1234

#self ip address for testing if firewall on network
#127.0.0.1

#create variables for the name of the internet server, ip adress and variable soc for later function calls with socket
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

#gets username then exits the start menu and opens the picklechat main communication page
def start(nameEnter, screen):
    global name

    #gets name from the name entry box
    name = nameEnter.get()

    #destroys the screen once connected to another computer
    screen.destroy()

#creates the gui for the start screen    
def startMenu(soc, host_name, ip):
    #creates screen and title
    screen = Tk()
    screen.title("PickleChat Menu")
    
    #combines ip and network name to be printed in a label
    h_ip = host_name + " ({})".format(ip)
    host_ip = Label(screen, text = h_ip)
    #places label
    host_ip.grid(column = 0, row = 0)
    
    #creates a label to tell user to enter their desired username below
    nameBox = Label(screen, text = "Enter name below:")
    nameBox.grid(column = 0, row = 1)#places label in second row
    
    #entry box for the user to type their name
    nameEnter = Entry(screen, width = 25)
    nameEnter.grid(column = 0, row = 2)

    #start button
    stb = Button(screen, text = "Start with username above", fg = "blue", command = lambda : start(nameEnter, screen))
    stb.grid(column = 0, row = 3)

    screen.mainloop()#inserts the window into the main loop creating it
#calls start menu screen to open creating isolated start menu screen
startMenu(soc, host_name, ip)
#--------------------------------------------------------

#puts port and network name together
soc.bind((host_name, port))

#prints your username in the main ide
print("Username: ",name)
print("Waiting for incoming connections...")

#waits for incoming connections
soc.listen(5)

#accepts connections
connection, addr = soc.accept()

#sends your username to the other computer that has connected
connection.send(name.encode())

#recv the username from the connected user
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name, "has joined your PickleChat server")

#send button function
#message is set equal to the contents of the message box
#sends message
#deletes content from message box
def sendf(messageBox):
    message = messageBox.get()
    connection.send(message.encode())
    messageBox.delete(0, END)
#creates the gui for the main pickle chat app

def chatRoom(soc, connection, addr, port, host_name, ip, name, client_name):
    window = Tk()
    window.title("PickleChat")
    #creates file title and dimensions of window
    window.geometry("450x700")

    #placed at the top
    #calls the sendf function with messageBox parameter
    sendButton = Button(window, text = "SEND", command = lambda : sendf(messageBox))
    sendButton.grid(column = 0, row = 0)
    
    window.bind(<Enter>, sendf(messageBox)

    #creates the entry box for your message
    messageBox = Entry(window, width = 48)
    messageBox.grid(column = 0, row = 1)
            
    window.mainloop()
def incoming(soc, connection, addr, port, host_name, ip, name, client_name):
    while True:
        cmessage = connection.recv(1024)
        cmessage = cmessage.decode()
        print(client_name, " >>> ", cmessage)
threading.Thread(target = chatRoom(soc, connection, addr, port, host_name, ip, name, client_name)).start()
threading.Thread(target = incoming(soc, connection, addr, port, host_name, ip, name, client_name)).start()
