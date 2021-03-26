from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
plt.style.use("fivethirtyeight")

with open('data.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    languages_count=Counter()
    row=next(csv_reader)
    for row in csv_reader:
        languages_count.update(row['LanguagesWorkedWith'].split(';'))

    # print(row['LanguagesWorkedWith'].split(';'))
languages=[]
popularity=[]
for item in languages_count.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
languages.reverse()
popularity.reverse()
plt.barh(languages,popularity)
plt.title("programming lang popularity")
plt.xlabel("popularity")
plt.ylabel("languages")

plt.tight_layout()

plt.show()