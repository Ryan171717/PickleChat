import socket, random

class User:
    def __init__(self, username, password, ip):
        self.password = password
        self.username = username
        self.ip = ip
        user_dict.update({username:username})
        self.message = self.assignMessage()
        with open("Users.txt", 'a+') as f:
            f.write('{}{}'.format(self.username, '\n'))
        self.createFile(self.username, self.password, self.ip, self.message)

    def createFile(self, username, password, ip, message):
        with open("{}_UserFile.txt".format(username), 'w+') as f:
            f.write("{} {} {} {}".format(username, password, ip, message))
    def assignMessage(self):
        defaultMessages = ['hello world', 'how are you', 'it tastes like a bologna ball',
                          'doesnt taste like much','that was the plan', 'welp that didnt work',
                          'only one way to find out']
        return random.choice(defaultMessages)
    def changeMessage(self, new_message):
        passcode = input("Enter your password:\n")
        if passcode == self.password:
            self.message = new_message
            self.createFile(self.username, self.password, self.ip, self.message)
    def changePassword(self, password):
        original = input("Enter original password:\n")
        if original == self.password:
            new_password = input("Enter your new password:\n")
            self.password = new_password
            self.createFile(self.username, self.password, self.ip, self.message)
            print("Password change successful")
    def printAttr(self, name, attr):
        if attr == 'message':
            passcode = input("Enter your password:\n")
            if passcode == self.password:
                print(self.message)
        elif attr == 'ip':
            print(user_dict[name].ip)
        elif attr == 'password':
            passcode = input("Enter your password:\n")
            if passcode == self.password:
                print(self.password)
def choices():
     while True:
            choice = input('Would you like to create a new user? (y/n)\n')
            if choice == 'y':
                username = input("Username:\n")
                while True:
                    password = input("Password:\n")
                    confirmation = input("Confirm password:\n")
                    if password == confirmation:
                        break
                    print('Make sure both passwords are the same.')
                ip = socket.gethostbyname(socket.gethostname())
                User(username, password, ip)
            if choice == 'n':
                print(user_dict)
                choice = input('Would you like to access an attribute?(y/n)\n')
                if choice == 'y':
                    User.printAttr(user_dict[input("Username")], input("Which attribute?\n"))
                if choice == 'n':
                    choice = input("Would you like to change username or password? (message/password)")
                    if choice == 'message':
                        name = user_dict[input("Username")]
                        User.changeMessage(name, name, input("New message:\n"))
                    if choice == 'password':
                        User.changePassword(user_dict[input("Username")], input("New password:\n"))
                if  choice == 'break':
                    break
            if choice == 'break':
                break
def main():
    global user_dict
    user_dict ={}
    try:
        with open("Users.txt") as f:
            for line in f:
                if line:
                    username = line
                    with open("{}_UserFile.txt".format(username), 'r+') as u:
                        if '.' in u:
                            for line in u:
                                username, password, ip, message = line.split()
                                User(username, password, ip, message)
    except FileNotFoundError:
       choices()
    choices()
                    
main()
