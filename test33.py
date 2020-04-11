# 07082019
# 친구관리 리스트

friends = []

def prn(list):
    print(list)

def add(list):
    name = input("추가할 이름을 입력 : ")
    list.append(name)
    print(list)
    #return list

def changeName(list):
    name = input("기존 이름 입력 : ")
    if name in list:
        list[list.index(name)] = input("변경할 이름 입력 : ")
    else :
        print("다시 입력하세요 : ")
        changeName(list) # 재귀함수
    #return list

def delete(list):
    name = input("삭제할 이름 입력 : ")
    if name in list:
        list.remove(name)
    #return list




menu = 0
while menu != 9 :
    print("--------------------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 이름 변경")
    print("4. 친구 삭제")
    print("9. 종료")
    print("--------------------------------")
    menu = int(input("메뉴를 선택하세요 : "))

    if menu == 1 :
        prn(friends)
    elif menu == 2 :
        add(friends)
    elif menu == 3 :
        changeName(friends)
    elif menu == 4 :
        delete(friends)
    elif menu == 9 :
        print("프로그램 종료")
        break
    else :
        print("다시 입력하세요")
        continue
