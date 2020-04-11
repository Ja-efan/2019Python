height=float(input("키 입력: "))
weight=float(input("몸무게 입력: "))

bmi = (weight / (height**2))*100

print("bmi= ", bmi)
print("bmi= %5.1f" % (bmi) )
