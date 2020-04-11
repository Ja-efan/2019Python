# 07082019
# 문자열의 문자개수, 공백 개수 계산


table = {"alphas":0, "digits":0 , "space":0}
str = input("문자열 입력: ")

for i in str:
    if i.isalpha():
        table["alphas"] += 1
    elif i.isdigit():
        table["digits"] += 1
    elif i.isspace():
        table["space"] += 1

print(table)
