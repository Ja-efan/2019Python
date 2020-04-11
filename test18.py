def countdown(n):
    if n%2 == 0 :
        print("Even")
    else:
        print("Odd")
        countdown(n-1)
countdown(3)
