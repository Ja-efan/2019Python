def f():
    global s
    s = "i love london!"
    print(s)

s = "i love paris!"
f()
print(s)
