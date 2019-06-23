import socket, random
def user_num_update():
    with open("UserNum.txt") as f:
        user_num= f
    return(user_num)

def GetUsers(user_dict, AttrList, user_num):
    user_dict = {}
    user_num = 0
    AttrList = []
    with open('UserInfo.txt') as f:
        AttrList = []
        for line in f:
            name, val = line.split()
            user_dict.update({name: val})
            addAttrs(name, user_num, user_dict)
            user_num += 1
        return user_dict
def addAttrs(name, user_num, user_dict):
    attrs = user_dict[name].split('_')
    tempAttrList = []
    for attr in attrs:
        tempAttrList.append(attr)
    AttrList.append(tempAttrList)
    user_dict[name] = user_num
    user_num+=1
                        
        

class User:
    def __init__(self, username, password, ip, user_num):
        self.password = password
        self.username = username
        self.ip = ip
        self.message = self.assign_message()
        self.fmessage = self.update_log(self.username, self.password, self.ip, self.message, user_num)
        AttrList = []
    def update_log(self, username, password, ip, message, user_num):
        with open("UserInfo.txt", 'a+') as f:
            f.write(self.username)
            f.write(' ')
            self.fmessage = self.password+'_'+self.ip+'_'+self.message
            f.write(self.fmessage)
            f.write('\n')
            user_num += 1
            AttrList = []
            self.add_user(self.username, self.fmessage)
            return self.fmessage
    def assign_message(self):
        messages =  ['hello.world', 'how.are.you', 'it.tastes.like.a.bologna.ball', 'doesnt.taste.like.much',
                    'that.was.the.plan', 'welp.that.didnt.work', 'only.one.way.to.find.out']
        return random.choice(messages)
    def add_user(self, username, fmessage):
        user_dict.update({self.username: self.fmessage})
        tempAttrList = []
        for attr in user_dict[username].split('_'):
            tempAttrList.append(attr)
        AttrList.append(tempAttrList)
        user_dict[self.username] = len(user_dict)-1
    
def printAttribute(attr, attr_num):

    if attr_num == 2:
        m = ''
        for letter in attr:
            if letter != '.':
                m+= letter
            if letter == '.':
                m+= ' '
        return m
                
    else:
        return attr
    
def create_user():
        while True:
            new = input("Would you like to create a new user: (y/n)")
            if new == 'y':
                username = ' '
                while ' ' in username:
                    username = input("Enter username\n")
                    if ' ' in username:
                        print('try again. use only letters and characters other than {} and {}'.format("'_'", 'spaces'))
                while True:
                        password = input("Enter password\n")
                        confirmation = input("Enter password again\n")
                        if password == confirmation:
                            break
                        else:
                            print("Make sure you type the same password")
                ip = socket.gethostbyname(socket.gethostname())
                User(username, password, ip, user_num)
                AttrList = []
                
            if new == 'n':
                return
def accessAttribute():
        print(AttrList, '\n', user_dict)
        attr = input("What attribute would you like to find? (ip, password, message)\n")
        if attr != 'message':
            if attr == 'ip':
                attr_num = 1
            if attr == 'password':
                attr_num = 0
            name = input("Enter username of the user you would like to find the attribute for:\n")
            print(printAttribute(AttrList[user_dict[name]][attr_num], attr_num))
        if attr == 'message':
            attr_num = 2
            name =input("Enter username of the user you would like to find the attribute for:\n")
        print(printAttribute(AttrList[user_dict[name]][attr_num], attr_num))
        print(AttrList, '\n', user_dict)
def main():

    global user_dict
    user_dict = {}
    global AttrList
    AttrList = []
    global user_num
    user_num = 0
    
    user_dict = GetUsers(user_dict, AttrList, user_num)

    print(user_dict)
    print(AttrList)
    while True:
        choice = input("Would you like to create a new user or access an attribute? (new/access)\n")
        if choice == 'new':
            create_user()
        if choice == 'access':
            accessAttribute()
        if choice =='break':
            break

    
main()
