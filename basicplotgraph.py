import matplotlib.pyplot as plt

#plt.style.use('fivethirtyeight') a style
plt.xkcd() # a method (comic looking style)

ages_x = [25, 26, 27, 28, 29, 30, 31]
dev_y = [38000, 39000, 40523, 50492, 50392, 50230, 54320]
py_dev_y = [40000, 45000, 50000, 55000, 60000, 70000, 86000]
js_dev_y = [40000, 66034, 67503, 68309, 69203, 70432, 80349]

plt.plot(ages_x, py_dev_y,
         label='Python')

plt.plot(ages_x, js_dev_y,
         label='Javascript')

plt.plot(ages_x, dev_y,
         color='#444444', linestyle='--', label='All Devs')

plt.xlabel("Age in years")
plt.ylabel("Salary in Euro")
plt.title("Salary by Age")
plt.legend()
plt.tight_layout()
plt.savefig('plot.png') # this saves an image of this graph called plot.png to the project
plt.show()