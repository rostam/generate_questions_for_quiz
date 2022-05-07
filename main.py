import csv, random

words = []
with open("persian-wikipedia.csv") as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if int(row[1]) > 2000:
            words.append(row[0])


dict = {}
with open("dict.csv") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        dict[row[1]] = row[0]

# print(dict)

with open("prepared_data.csv", "w") as f:
    writer = csv.writer(f)
    for w in words:
        if w in dict.keys():
            i = random.randint(0, len(words) - 1)
            j = random.randint(0, len(words) - 1)
            k = random.randint(0, len(words) - 1)
            writer.writerow([w, dict[w], words[i], words[j], words[k]])

