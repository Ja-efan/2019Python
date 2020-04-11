# 07092019
#vehicle class (추상클래스 : drive(), stop()) 상속을 받은 Car class 와 Truck class 작성
# 아래의 추상 메소드를 자식 클래스에서 오버라이드 하여 구현.
#	- drive() : 자동차를 출발하는 메소드
#	- stop() : 자동차를 정지합니다.

class Vehicle: # 부모 class
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("이것은 추상메소드입니다. ") #예외처리

    def stop(self):
        raise NotImplementedError("이것은 추상메소드입니다. ") #예외처리

class Car(Vehicle):
    def drive(self):
        return '승용자를 운전합니다. '

    def stop(self):
        return '승용자를 정지합니다. '


class Truck(Vehicle):
    def drive(self):
        return '트럭을 운전합니다. '

    def stop(self):
        return '트럭을 정지합니다. '

cars = [Truck('truck1'), Truck('truck2'),  Car('car1')]

for car in cars:
    print( car.name + ': ' + car.drive())
    print( car.name + ': ' + car.stop())
