# day5 07052019

text = input("문자열을 입력하세요: ")

data = ""

for word in text.upper().split(): ###### python의 강점 (문자열처리)
    data += word[0]
    #print(data)

print(data)
