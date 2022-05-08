import csv, random, json
from itertools import permutations

words = []
with open("persian-wikipedia.csv") as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if int(row[1]) > 2000:
            words.append(row[0])

dict_en_fa = {}
dict_fa_en = {}
words_english = []
with open("dict.csv") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        dict_en_fa[row[1]] = row[0]
        dict_fa_en[row[0]] = row[1]
        words_english = row[1]


# print(dict)

data = []
with open("prepared_data.csv", "w") as f:
    with open("words_questions.json", "w") as f2:
        writer = csv.writer(f)
        for w in words:
            if w in dict_en_fa.keys():
                ind = [i,j,k] = random.sample(range(0, len(words) - 1), 3)
                writer.writerow([w, dict_en_fa[w], words[i], words[j], words[k]])

                perm = permutations([0, 1, 2, 3])
                choices = []
                d = {}
                cnt = 0
                answer = 0
                for i in list(perm)[0]:
                    if i == 3:
                        choices.append(w)
                        answer = cnt
                    else:
                        choices.append(words[ind[i]])
                    cnt = cnt + 1
                data.append({
                    "question": dict_en_fa[w],
                    "choices": choices,
                    "answer": answer
                })

        for w in words_english:
            if w in dict_fa_en.keys():
                ind = [i, j, k] = random.sample(range(0, len(words_english) - 1), 3)
                writer.writerow([w, dict_fa_en[w], words_english[i], words_english[j], words_english[k]])

                perm = permutations([0, 1, 2, 3])
                choices = []
                d = {}
                cnt = 0
                answer = 0
                for i in list(perm)[0]:
                    if i == 3:
                        choices.append(w)
                        answer = cnt
                    else:
                        choices.append(words[ind[i]])
                    cnt = cnt + 1

                data.append({
                    "question": dict_fa_en[w],
                    "choices": choices,
                    "answer": answer
                })

        json.dump(data, f2, indent=2, ensure_ascii=False)
