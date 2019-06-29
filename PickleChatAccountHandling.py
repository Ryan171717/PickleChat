import socket, random

class User:
    def __init__(self, username, password, ip, *kwargs):
        self.password = password
        self.username = username
        self.ip = ip
        if kwargs:
            for part in kwargs:
                self.message = part
        else:
            self.message = self.assignMessage()
        file = open('Users.txt').read()
        with open("Users.txt", 'a+') as f:
            add = True
            if self.username in file:
                add = False
            if add:
                f.write('{}{}'.format(self.username, '\n'))
        if not kwargs:
            self.createFile(self.username, self.password, self.ip, self.message)
    def createFile(self, username, password, ip, message, *kwargs):
        with open("{}_UserFile.txt".format(username), 'w+') as f:
            if kwargs is True or '.' not in f:
                parts = [self.username, '\n', self.password,'\n', self.ip,'\n', self.message]
                for part in parts:
                    f.write('{}'.format(part))
    def assignMessage(self):
        defaultMessages = ['hello world', 'how are you', 'it tastes like a bologna ball',
                          'doesnt taste like much','that was the plan', 'welp that didnt work',
                          'only one way to find out']
        return random.choice(defaultMessages)
    def changeMessage(self, new_message):
        passcode = input("Enter your password:\n")
        if passcode == self.password:
            self.message = new_message
            self.createFile(self.username, self.password, self.ip, self.message, True)
            print('Message change successful')
    def changePassword(self, password):
        original = input("Enter original password:\n")
        if original == self.password:
            new_password = input("Enter your new password:\n")
            self.password = new_password
            self.createFile(self.username, self.password, self.ip, self.message, True)
            print("Password change successful")
    def printAttr(self, name, attr):
        passcode = input("Enter your password:\n")
        if passcode == self.password:
            if attr == 'message':
                print(self.message)
            elif attr == 'ip':
                print(self.ip)
            elif attr == 'password':
                print(self.password)
def choices(user_dict):
    keys = []
     for key in user_dict.keys():
         keys.append(key)
     print('user_dict keys: {}'.format(key for key in keys))
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
                user_dict[username] = User(username, password, ip)
            if choice == 'n':
                print(user_dict)
                choice = input('Would you like to access an attribute?(y/n)\n')
                if choice == 'y':
                    name = user_dict[input("Username")]
                    name.printAttr(name, input('Which Attribute?\n'))
                if choice == 'n':
                    choice = input("Would you like to change username or password? (message/password)")
                    name = input('Username:\n')
                    if choice == 'message':
                        OBJname = user_dict[name]
                        OBJname.changeMessage(input("New message:\n"))
                    if choice == 'password':
                        User.changePassword(input("New password:\n"))
                if  choice == 'break':
                    break
            if choice == 'break':
                break
def main():
    global user_dict
    user_dict ={}
    with open("Users.txt", 'r+') as f:
        for line in f:
            username = line.strip('\n')
            file = '{}_UserFile.txt'.format(username.strip('\n'))
            if file != '_UserFile.txt':
                attrs= []
                with open(file, 'r+') as u:
                    for line in u:
                        attrs.append(line.strip('\n'))
                    user_dict[username.strip('\n')] = User(username, attrs[1], attrs[2], attrs[3])
    choices(user_dict)                    
main()

