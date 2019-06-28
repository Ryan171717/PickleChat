import socket, random

class User:
    def __init__(self, username, password, ip, *kwargs):
        self.password = password
        self.username = username
        self.ip = ip
        if kwargs:
            self.message = kwargs
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
        print('here here')
    def createFile(self, username, password, ip, message, **kwargs):
        print('here here')
        with open("{}_UserFile.txt".format(username), 'w+') as f:
            if '.' not in f or kwargs is True:
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
    def changePassword(self, password):
        original = input("Enter original password:\n")
        if original == self.password:
            new_password = input("Enter your new password:\n")
            self.password = new_password
            self.createFile(self.username, self.password, self.ip, self.message, True)
            print("Password change successful")
    def printAttr(self, name, attr):
        if attr == 'message':
            passcode = input("Enter your password:\n")
            print('here;')
            print(user_dict[name].password)
            if passcode == user_dict[name].password:
                print(user_dict[name].message)
        elif attr == 'ip':
            print(user_dict[name].ip)
        elif attr == 'password':
            passcode = input("Enter your password:\n")
            if passcode == self.password:
                print(user_dict[name].password)
def choices(user_dict):
     print(user_dict)
     for key in user_dict.keys():
         print(user_dict[key])
     while True:
            choice = input('Would you like to create a new user? (y/n)\n')
            if choice == 'y':
                username = input("Username:\n")
                while True:
                    password = input("Password:\n")
                    confirmation = input("C onfirm password:\n")
                    if password == confirmation:
                        break
                    print('Make sure both passwords are the same.')
                ip = socket.gethostbyname(socket.gethostname())
                user_dict[username] = User(username, password, ip)
            if choice == 'n':
                print(user_dict)
                choice = input('Would you like to access an attribute?(y/n)\n')
                if choice == 'y':
                    name = input('name:\n')
                    user_dict[name].printAttr(name, input('Which attribute?\n'))
                    #User.printAttr(user_dict[name], name, input("Which attribute?\n"))
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
   # try:
    with open("Users.txt", 'r+') as f:
        for line in f:
            if line != '':
                username = line
                print('here')
                file = '{}_UserFile.txt'.format(username.strip('\n'))
                if file != '_UserFile.txt':
                    with open(file, 'r+') as u:
                        attrs = [username]
                        for line in u:
                            attrs.append(line)
                            print(attrs)
                        print(attrs[2])
                        user_dict[username.strip('\n')] = User(username, attrs[2], attrs[3], attrs[4])
 #   except FileNotFoundError:
     #  choices()
    choices(user_dict)                    
main()
