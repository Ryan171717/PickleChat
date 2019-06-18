import socket, random
def user_num_update():
    with open("UserNum.txt") as f:
        user_num= f
    return(user_num)

def GetUsers(user_dict, AttrList, user_num):
    with open('UserInfo.txt') as f:
        for line in f:
            key, val = line.split()
            user_dict[key] = val
            addAttrs(key, user_num)
            user_num += 1
def addAttrs(key, user_num):
    attrs = user_dict[key].split('_')
    tempAttrList = []
    for attr in attrs:
        tempAttrList.append(attr)
    AttrList.append(tempAttrList)
    user_dict[key] = user_num
    user_num+=1
                        
        

class User:
    def __init__(self, username, password, ip, user_num):
        self.password = password
        self.username = username
        self.ip = ip
        self.message = self.assign_message()
        self.update_log(self.username, self.password, self.ip, self.message, user_num)

    def update_log(self, username, password, ip, message, user_num):
        with open("UserInfo.txt", 'a+') as f:
            f.write(self.username)
            f.write(' ')
            f_message = password+'_'+ip+'_'+message
            f.write(f_message)
            f.write('\n')
            user_num += 1
            GetUsers(user_dict, AttrList, user_num)
            
    def assign_message(self):
        messages =  ['hello.world', 'how.are.you', 'it.tastes.like.a.bologna.ball', 'doesnt.taste.like.much',
                    'that.was.the.plan', 'welp.that.didnt.work']
        return random.choice(messages)
def printMessage(message):
    m = ' '
    return m.join(message)
    

def main():

    global user_dict
    user_dict = {}
    global AttrList
    AttrList = []
    user_num = 0
    GetUsers(user_dict, AttrList, user_num)
    #u2 = User('adam', 'ninja', 'alisonHojlo', user_num)
    print(user_dict)
    print(printMessage(AttrList[user_dict['adam']][2].split('.')))
    
    
main()
