import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight') # a style
#plt.xkcd() # a method (comic looking style)

ages_x = [25, 26, 27, 28, 29, 30, 31]

x_indexes = np.arange(len(ages_x)) # creates the variable x_indexes with an array of values, its a numbered version of the X values
width = 0.25

dev_y = [38000, 39000, 40523, 50492, 50392, 50230, 54320]
py_dev_y = [40000, 45000, 50000, 55000, 60000, 70000, 86000]
js_dev_y = [40000, 66034, 67503, 68309, 69203, 70432, 80349]

plt.bar(x_indexes - width, dev_y,
         width=width, color='#e5ae38', linestyle='--', label='All Devs')

plt.bar(x_indexes, py_dev_y,
         width=width, color='#444444', label='Python')

plt.bar(x_indexes + width, js_dev_y,
         width=width, color='#008fd5', label='Javascript')

plt.legend()
plt.xticks(ticks=x_indexes, labels=ages_x) # uses x_indexes as ticks and ages as labels instead of numbering 12345 etc
plt.title("Salary by Age")
plt.xlabel("Age in years")
plt.ylabel("Salary in Euro")
plt.tight_layout()
# plt.savefig('plot.png') # this saves an image of this graph called plot.png to the project
plt.show()