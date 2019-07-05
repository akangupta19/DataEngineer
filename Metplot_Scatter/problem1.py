import matplotlib.pyplot as plt
from pylab import random
X = random(200)
Y = random(200)
plt.scatter(X,Y, color='red')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("scatter chart")
plt.show()