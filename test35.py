# 07082019

# 한글깨짐 해결
# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class SoccerPlayer(object):
    def __init__(self,name,position,back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경: from %d to %d" % (self.back_number,new_number))
        self.back_number = new_number

    def __str__(self):
        return("Hello, My name is %s. I play in %s in center." % (self.name,self.position))


jinhyun = SoccerPlayer("Jinhyun","MF",10)

print("현재 선수의 등번호는 ", jinhyun.back_number)
jinhyun.change_back_number(5)
print("현재 선수의 등번호는 ", jinhyun.back_number)
