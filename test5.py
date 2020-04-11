dan = int(input("몇 단? "))

print("구구단 ", dan,"단을 계산한다.")

for i in range(1,10,1):
    result = dan*i
    print(dan,"x",i,"=",result)
