# 07112019
# 13-03 p.446

import csv
f = open("./korea_floating_population_data.csv","r")
reader = csv.reader(
    f,
    delimiter = ',',
    quotechar = '"',
    quoting = csv.QUOTE_ALL)

print(reader)
