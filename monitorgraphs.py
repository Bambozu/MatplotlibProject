import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''Note:
de variables heten momenteel a en b, dit is natuurlijk geen best practice. Ook is de code niet helemaal perfect 
omdat de cpu usage plot een spike van 9.5 laat zien die boven de plot uitschiet, dit heb ik nog niet kunnen fixen.
Ben de hele dag bezig geweest met docs lezen/code testen, de data heeft zo zijn "issues": het was best lastig om het netjes uit te lezen
Maar voor nu is dit de basis.
De hoeveelheid data of welke range aan data is weergegeven kan je natuurlijk aanpassen
Overigens zijn de comments in het engels, because why not :)
'''
# importing data using pandas
data = pd.read_csv("systemUsage.csv")
a = np.array(list(data["ram"]))

# plotting data directly from dataframe
data.plot("timestamp","ram", color="red",figsize=(15,5) )

# use this for extracting range from data (not really necessary)
# a = np.array(list(data["ram"][0:60]))

b = np.array(range(len(a)))

# making plot wider horizontally
plt.figure(figsize=(15,5))

# plotting points
plt.plot(b,a)

# filling everything below curve (to make it an "area chart")
plt.fill_between(b,a,color="blue",alpha=0.1)

# dynamically setting the limit on the y axis so a curve can be observed (maybe change scalar for different data) again not really necessary
plt.ylim((np.min(a)-np.min(a)*0.001), (np.max(a)+np.max(a)*0.001))

plt.title("Monitoring")
plt.xlabel("time in seconds")
plt.ylabel("cpu usage")
plt.grid(True)
plt.show()