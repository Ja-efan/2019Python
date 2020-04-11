# 07092019
# __str__() 메소드 활용 테스트 : 객체의 문자열 표현 반환


class MyTime:

    def __init__(self, hour, minute, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)


time = MyTime(10,35)
print(time)
