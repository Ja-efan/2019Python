menu = []
price = []

for i in range(100):
    tmpmenu = input("메뉴를 입력하세요 : ")
    if tmpmenu == "quit":
        break
    else:
        tmpprice = input("가격을 입력하세요 : ")
        menu.append(tmpmenu)
        price.append(tmpprice)
print(menu)
print(price)

selmenu=input("메뉴를 선택하세요 : ")
i = 0
while(i<len(menu)):
    if selmenu == menu[i]:
        print("선택한 메뉴의 가격은 ",price[i],"입니다.")
        break
    else:
        i+=1
