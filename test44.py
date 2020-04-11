# 07092019
# 메소드 오버 라이드 실습 Employee class 와 Manager class 가 있다
# 직원은 월급만, 매니저는 월급외에 보너스가 있다.
# 아래의 코드에 직원을 추가 출력하시오

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def  getSalary(self):
        return salary

    def __repr__(self):
        return "이름: "+ self.name+ "; 월급: "+ str(self.salary)

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)  #보모 클래스의 __init__호출

        self.bonus =bonus

    def  getSalary(self):
        salary = super().getSalary()  #부모 클래스의 급여 리턴값 호출
        return salary + self.bonus

    def __repr__(self):
        return "이름: "+ self.name+ "; 월급: "+ str(self.salary)+\
                "; 보너스: "+ str(self.bonus)

kim = Manager("김철수", 2000000, 1000000)
lee = Employee("홍길동", 1500000)
print(kim)
print(lee)
