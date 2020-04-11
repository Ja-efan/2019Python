def get_line(x1,y1,x2,y2):
    if(x1==x2):
        return 0,0
    else:
        slope = (float)(y2-y1) / (float)(x2-x1)
        yintercept = y1-slope*x1
        return slope,yintercept #return값 2개

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

slope,yintercept = get_line(x1,x2,y1,y2) #return값 두개를 변수 두개에 대입

print("기울기는 = ",slope,"y절편은 = ",yintercept)
