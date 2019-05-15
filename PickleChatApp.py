
# import all necesary modules
#tkinter for GUI
from tkinter import *
#socket for connection 
import socket
#threading for running multiple functions at once
from threading import Thread
#time for pauses
import time
#requests for getting images from internet
import requests
#random for choosing random image
import random


# gets username then exits the start menu and opens the picklechat main communication page
def start(nameEnter, screen):
    global name

   # gets name from the name entry box
    name = nameEnter.get()
    # destroys the screen once connected to another computer
    screen.destroy()

# creates the gui for the start screen


def startMenu(host_name, ip):
    # creates screen and title
    screen = Tk()
    screen.title("PickleChat Menu")
    # combines ip and network name to be printed in a label
    h_ip = host_name + " ({})".format(ip)
    host_ip = Label(screen, text=str(h_ip))
    # places label
    host_ip.grid(column=0, row=0)
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    # creates a label to tell user to enter their desired username below
    nameBox = Label(screen, text="Enter name below:")
    nameBox.grid(column=0, row=1)  # places label in second row

    # entry box for the user to type their name

    nameEnter = Entry(screen, width = 160)
    nameEnter.grid(column=0, row=2)
    screen.bind("<Return>", lambda event: start(nameEnter, screen))
     # start button
    stb = Button(screen, text="Start with username above", fg="blue", bg = 'yellow', command=lambda: start(nameEnter, screen))
    stb.grid(column=0, row=3)

    screen.mainloop()
# inserts the window into the main loop creating it
# calls start menu screen to open creating isolated start menu screen



# --------------------------------------------------------



# send button function
# message is set equal to the contents of the message box
# sends message
# deletes content from message box
def sendf(connection, messageBox, mylist):
    message = messageBox.get()
    connection.send(message.encode())
    messageBox.delete(0, END)
    
    pm = "ME >>> " + message
    
    mylist.insert(END, pm)

def chatRoom(connection):

    window = Tk()
    window.title("PickleChat")
    # creates file title and dimensions of window
    window.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    sendButton = Button(window, text="SEND", bg="red", fg="black", command=lambda: sendf(connection, messageBox, mylist))
    sendButton.pack(side='top')
    # creates the entry box for your message
    messageBox = Entry(window, width=48)
    messageBox.pack(side='top')

    scrollbar = Scrollbar(window)
    scrollbar.pack(side="right", fill='y')

    mylist = Listbox(window, yscrollcommand=scrollbar.set, width=50, height=41)


    mylist.pack(side='bottom')
    scrollbar.config(command=mylist.yview)
    window.bind("<Return>",  lambda event: sendf(connction, messageBox, mylist))
    window.mainloop()


def incoming(connection, client_name, mylist):
    while True:
        cmessage = connection.recv(1024)
        cmessage = cmessage.decode()

        if cmessage != "":
            m = (client_name, " >>> ", cmessage)
            mylist.insert(END, m)



def picture():
    urls = ['http://clipart-library.com/images/ki8o54ybT.png', 'http://clipart-library.com/image_gallery/7951.jpg', 'https://cdn5.vectorstock.com/i/thumb-large/78/54/pickle-cartoon-character-with-attitude-vector-21537854.jpg', 'http://clipart-library.com/images/BTgAzRKoc.jpg', 'http://clipart-library.com/images/qTBXoggBc.jpg']
    url = random.choice(urls)
    r = requests.get(url, allow_redirects=True)
    open('google.ico', 'wb').write(r.content)
    return (google.ico)






def main():
    # create a port to communicate on
    port = 1234
    # self ip address for testing if firewall on network
    # ip = '127.0.0.1'
    # create variables for the name of the internet server, ip adress and variable soc for later function calls with socket
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)

    startMenu(host_name, ip)
    s = socket.socket()
    try:
        s.bind((host_name, port))
    except OSError:
        print("Restart the server side and client side shell and try again.")

    # prints your username in the main ide
    waiting_screen = Tk()
    waiting_screen.geometry("{0}x{1}+0+0".format(waiting_screen.winfo_screenwidth(), waiting_screen.winfo_screenheight()))
    waiting_screen.title("Waiting")
    
    pic = picture()
    x = (waiting_screen.winfo_screenwidth())//2
    y = (waiting_screen.winfo_screenheight())//2
    
    window.create_image(x,y, anchor=center, image=pic)      

    
    
    name_display = Label(waiting_screen, text = "Please wait for a connection...")
    name_display.grid(column = 0, row = 0)

    
    waiting_screen.mainloop()
    
    time.sleep(1)
    s.listen(5)
    # waits for incoming connections


    # accepts connections
    connection = s.accept()

    waiting_screen.destroy()
    # sends your username to the other computer that has connected
    connection.send(name.encode())

    # recv the username from the connected user
    client_name = connection.recv(1024)
    client_name = client_name.decode()
    print(client_name, "has joined your PickleChat server")



    if __name__ == '__main__':
        Thread(target = chatRoom(connection)).start()
        Thread(target = incoming(connection, client_name)).start()

main()

