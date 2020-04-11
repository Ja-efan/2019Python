# 07122019

import csv

linenum = 0
outlist = []
head = []

#파일열기
infile = open("data.csv","r") #읽어올 파일
outfile = open("out_file.csv","w",encoding = "ANSI") #작성할 파일

data = csv.reader(infile)
writer = csv.writer(outfile)

for line_data in data :
    if linenum == 0:
        head = line_data
        head.append("sum")
        head.append("avg")
        print(head)
        outlist.append(head)
        print(outlist)


    else:
        name, c, java, python = line_data #언팩
        sum = int(c) + int(java) + int(python)
        avg = float(sum) / 3

        student = [name, c, java, python, sum, avg]
        outlist.append(student)

    linenum += 1

for outline in outlist:
        writer.writerow(outline)

print(outlist)
