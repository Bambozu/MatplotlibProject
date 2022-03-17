import csv
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight') # a style


data = pd.read_csv('data.csv') # this is how to open the data using pandas module
ids = data['Responder_id']
lang_responses = ['LanguagesWorkedWith']


# with open('data.csv') as csv_file: # this opens the csv file
# csv_reader = csv.DictReader(csv_file)

language_counter = Counter()

for response in lang_responses:
    language_counter.update(['LanguagesWorkedWith'].split(';'))

    #for row in csv_reader:
       # language_counter.update(row['LanguagesWorkedWith'].split(';'))

# creating 2 empty lists, iterate over language counter using most_common method 15 (to get the 15 top values/tuples)
languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

# plt.xkcd() # a method (comic looking style)
plt.title("Most popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of people who Use")
plt.tight_layout()
plt.show()
# plt.savefig('plot.png') # this saves an image of this graph called plot.png to the project
