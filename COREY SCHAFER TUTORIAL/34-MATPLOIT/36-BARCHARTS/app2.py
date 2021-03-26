from matplotlib import pyplot as plt
import numpy as np
import csv
import pandas as pd
from collections import Counter
plt.style.use("fivethirtyeight")
data=pd.read_csv('data.csv')
ids=data['Responder_id']
response=data['LanguagesWorkedWith']
languages_count=Counter()
for response in response:
        languages_count.update(response.split(';'))


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