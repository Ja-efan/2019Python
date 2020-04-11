# day5 07052019

table = { "B4" : "Before",
        "TX" : "Thanks",
        "BBL" : "Be Back Later",
        "BCN" : "Be Seeing You",
        "HAND" : "Have A Nice Day"}

msg = input("번역할 문장을 입력하세요 : ")
words = msg.split()

result = ""

for word in words:
    if word in table:
        result += table[word] + " " # table에 있는 값을 result에 더함

    else:
        result += word + "" # table에 없는 값은 result에 더함

print(result)
