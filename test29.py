# day5 07052019

def process(w) :
    output = ""
    for ch in w:
        if ch.isalpha() :
            output += ch
    return output.lower()

words  = set()
#text = ""
filename = input("파일명 입력 : ")
file = open(filename, "r")

for line in file :
    linewords = line.split()
    #text += line.strip() + " "
    for word in linewords :
        words.add(process(word))

#print(text)
#print(len(text))
print("사용된 단어의 개수 : ",len(words))
print(words)
