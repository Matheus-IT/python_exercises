import csv

f = open('./mega_sena.tsv', 'r')
print(f)
temp = csv.reader(f, delimiter="\t")
for l in temp:
    print(l)
f.close()