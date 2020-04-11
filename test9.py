data = []

f = open("data.txt", "r")

for line in f.readlines():
    data.append(line.strip())

print(data)

for line in data:
    print(line)
