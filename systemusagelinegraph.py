import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from collections import Counter

plt.style.use('fivethirtyeight') # a style

data = pd.read_csv('systemUsage.csv') # this is how to open the data using pandas module
timestamp = data['timestamp']
cpu_freq = data['cpu_freq']
ram = data['ram']

timestamp_counter = Counter()

for response in timestamp:
    timestamp_counter.update(response.split(';'))

# creating 2 empty lists, iterate over language counter using most_common method 15 (to get the 15 top values/tuples)
timestamp = []
cpu_freq = []
ram = []

 #with open('data.csv') as csv_file: # this opens the csv file
 #csv_reader = csv.DictReader(csv_file)

#for response in lang_responses:
   #language_counter.update(split['LanguagesWorkedWith'].split(';'))

    #for row in csv_reader:
       #language_counter.update(row['LanguagesWorkedWith'].split(';'))

for item in timestamp_counter.most_common(15):
    #timestamp.append(item[0])
    cpu_freq.append(item[0])
    ram.append(item[1])

timestamp.reverse()
cpu_freq.reverse()
ram.reverse()
plt.bar(cpu_freq, ram)
#plt.plot(timestamp, cpu_freq,
         #label='CPU Frequency')

#plt.plot(timestamp, ram,
        # label='Memory/RAM')

#plt.plot(timestamp, dev_y,
       #  color='#444444', linestyle='--', label='All Devs')

# plt.xkcd() # a method (comic looking style)
plt.title("CPU & Memory Monitoring")
# plt.ylabel("Programming Languages")
plt.xlabel("xxx")

plt.tight_layout()

plt.show()
# plt.savefig('plot.png') # this saves an image of this graph called plot.png to the project
