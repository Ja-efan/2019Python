menu = []
price = []

for i in range(100):
    menu.append(input("메뉴를 입력하세요 : "))
    if menu[i] = "quit":
        menu.remove("quit")
        break
    price.append(input("가격을 입력하세요 : "))

print(menu)
print(price)

select = input("메뉴를 선택하세요 : ")
print(price[menu.index(select)])
print("선택한 메뉴의 가격은", price[menu.index(select)],"입니다.")
