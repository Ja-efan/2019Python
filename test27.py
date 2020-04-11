# day5 07052019

email = input("이메일 주소를 입력하세요 : ")

print(email)

id, domain = email.split("@") # '@'기준으로 두개로 나뉘어져 변수 두개로 받음

print("ID : ",id)
print("DOMAIN : ",domain)
