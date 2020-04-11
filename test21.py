
def prime(n):
    for i in range(2,n):
        #for k in range(2,i+1):
        if n % i == 0:
        b     return False
    return True


cnt = 0
n = int(input("정수를 입력하세요: "))

for i in range(2,n+1):
    if prime(i):
        print("%3d" % (i), end="")
        cnt += 1
        if cnt % 5 == 0:
            print()
