import csv
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight') # a style

with open('systemUsage.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    cpu_counter = Counter()

    for row in csv_reader:
        cpu_counter.update(row = next(csv_reader))
print(cpu_counter)





#plt.xkcd() # a method (comic looking style)


# plt.title("Salary by Age")
# plt.xlabel("Age in years")
# plt.ylabel("Salary in Euro")
# plt.tight_layout()
# plt.savefig('plot.png') # this saves an image of this graph called plot.png to the project
# plt.show()