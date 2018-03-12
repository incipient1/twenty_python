import string

class Sense_word():
    def __init__(self):
        self.list = []
        inputfile = open('filter_word.txt','r')
        for line in inputfile.readlines():
            self.list.append(str(line).strip('\n'))

        inputfile.close()
        #self.list = map(string.strip(),self.list)
        for item in self.list:
            print(item)

    def check_word(self,words):
        for word in self.list:
            if word in words:
                return True
        return False

if __name__ == '__main__':
    mycheck = Sense_word()
    ipstr = input('请输入语句：')
    if ipstr not in ('',' ','  '):
        if mycheck.check_word(ipstr):
            print('Freedom')
        else:
            print('HumanRight')
    else:
        print('wrong input')