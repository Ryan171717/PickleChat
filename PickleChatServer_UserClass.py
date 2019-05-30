import socket
import random
class User:
    def __init__(self, username, password, ip):
        self.password = password
        self.username = username
        self.ip = ip
        self.update_log(username, password, ip)
        self.message = self.assign_message(username)
    def update_log(self, username, password, ip):
        u_p_log = open("UserPassword_log.txt", 'a+')
        u_i_log = open("UserIp_log.txt", 'a+')
        userpassword = [username, password]
        for word in userpassword:
            u_p_log.write(word)
            u_p_log.write(' ')
        u_p_log.write('\n')
        userip = [username,  ip]
        for word in userip:
            u_i_log.write(word)
            u_i_log.write(' ')
        u_i_log.write('\n')

    def print_ip(self, name):
        ip_dict = {}
        with open("UserIp_log.txt") as f:
            for line in f:
                (key, val) = line.split()
                ip_dict[key] = val
        print(name, ' ------> ', ip_dict[name])
    def assign_message(self, name):
        messages = ['hello world', 'how are you', 'it tastes like a bologna ball', 'doesnt taste like much', 'that was the plan', 'welp that didnt work']
        return random.choice(messages)
    


        
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
username = input("Enter username\n")
password = input("Enter password\n")
user1 = User(username, password, str(ip))

pass_dict = {}
with open("UserPassword_log.txt") as f:
    for line in f:
       (key, val) = line.split()
       pass_dict[key] = val

def login(pass_dict''', user1'''):
    while True:
        name = input("Enter name\n")
        password= input("Enter password\n")
        if name in pass_dict:
            if pass_dict[name] == password:
                print("Access Granted")
                user1.print_ip(name)
                print(user1.message)
                break
            else:
                print("Try again")
        else:
            print("Try again")


def create_user():
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    username = input("Enter username:\n")
    password = input("Enter password\n")
    exec('%s = User % (username, (username, password, ip)))

    
    
    
while True:
    selection = input("Would you like to create a new user(y) or login to to a pre-existing account(n).  To exit enter 'e'? (y/n/e)\n")
    if selection == 'y':
        create_user()
    if selection == 'n':
         login(pass_dict)
    if selection == 'e':
         break
    else:
         print('Try a different key')
            
    
