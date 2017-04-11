import matplotlib.pyplot as plt
import numpy

matrix =numpy.array([
    [10, 23],
    [12, 22],
    [14, 50],
    [15, 10],
    [17, 30],
    [19, 40],
])
x_values = matrix[:, 0]
y_values = matrix[:, 1]

# scatter adds markers on graph
plt.scatter(x_values, y_values, color="black")

# plots lines on graph
plt.plot(x_values, y_values, color="green")

# setting labels on graph
plt.xlabel("HOURS")
plt.ylabel("Sale of Televisions")
plt.title("Television Sales graph")

plt.axis([0,20,0,60])
plt.grid(True)
# finaly show the graph
plt.show()
