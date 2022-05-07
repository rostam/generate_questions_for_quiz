import csv

words = []
with open("persian-wikipedia.csv") as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if int(row[1]) > 4000:
            words.append(row[0])



with open("dict.csv") as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader: