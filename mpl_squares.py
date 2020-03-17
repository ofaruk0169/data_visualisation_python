import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=300)
ax.plot(input_values, squares, linewidth=3)

#Sset chart title and label axes

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels
ax.tick_params(axis='both',which='major', labelsize=14)

plt.show()