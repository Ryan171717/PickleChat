import socket
import random
print(socket.gethostbyname(socket.gethostname()))

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

        userip = [username, ip]
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

        messages = ['hello world', 'how are you', 'it tastes like a bologna ball', 'doesnt taste like much',
                    'that was the plan', 'welp that didnt work']

        return random.choice(messages)


def login(pass_dict):
    while True:
        name = input("Enter name\n")
        password = input("Enter password\n")

        if name in pass_dict:
            if pass_dict[name] == password:
                print("Access Granted")
                User.print_ip(name, name)
                print(user_dict[name].message)
                break
            else:
                print("Incorect Password. Try again.")
        else:
            print("Username is not in database. Try again.")


def create_user():
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    while True:
        username = input("Enter username:\n")
        if username not in user_dict:
            break
        else:
            print("Try a different username")
    name = username
    password = input("Enter password\n")
    user_dict[name] = User(username, password, ip)
    print(user_dict[name])

    global pass_dict
    pass_dict = {}

    with open("UserPassword_log.txt") as f:
        for line in f:
            (key, val) = line.split()
            pass_dict[key] = val
    return user_dict[name]
def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    port = 55555
    soc.bind((host_name, port))
    connection = soc.accept()
    global user_dict
    user_dict = {}
    while True:
        selection = connection.recvall()
        selection = selection.decode()

        if selection == 'y':
            create_user()

        if selection == 'n':
            login(pass_dict)

        if selection == 'e':
            break

        if selection != 'y' and 'n' and 'e':
            print('Try a different key')
main()
