import random


def func(board):

    for r in range(10):
        for c in range(10):
            if board[r][c]:
                print("#",end="")
            else:
                print(".",end="")
            print("\n")

board = [[False for x in range(10)] for y in range(10)]

for r in range(10):
    for c in range(10):
        if(random.random() < 0.3):
            board[r][c] = True

func(board)

while True:
    row = int(input("지뢰의 위치를 입력 (행) : "))
    col = int(input("지뢰의 위치를 입력 (열) : "))

    if board[row-1][col-1]:
        print("지뢰")
        board[row-1][col-1] = False
    else:
        print("땡")

    ans=input("계속 하시겠습니까? (y/n) : ")

    if ans == "n":
        break
    else:
        func(board)
