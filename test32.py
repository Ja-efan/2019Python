# 07082019
# 함수 ver
# 오름차순

def selectionSort(alist): # 선택정렬 func
    for i in range(len(alist)):
        least = i # 인덱스 값
        leastValue = alist[i] # i번째 인덱스의 값

        for j in range(i+1,len(alist)):
            if alist[j] < leastValue: # 인덱스 i번째 값과 인덱스 j번째 값을 비교
            # j번째 인덱스 값이 i번재 인덱스 값보다 작으면
                least = j # 인덱스저장 변수에 j 저장
                leastValue = alist[j] #최소값 변수에 인덱스 j값 저장
                # 후에 j+1과 계속 비교
        tmp = alist[i] # 기존 i번째 인덱스 값을 tmp라는 변수에 저장
        alist[i] = alist[least] # 리스트 i번째 인덱스에 least번째 인덱스 값(최소값)을 저장
        alist[least] = tmp # least번째 인덱스가 비었으니 기존 i번째 인덱스 값을 대입


data = [7,9,5,1,8]
print("before : " , data)
selectionSort(data)
print("after : ", data)
