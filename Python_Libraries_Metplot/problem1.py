import matplotlib.pyplot as plt
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(X)
print("Values of Y (thrice of X):")
print(Y)

plt.plot(X, Y)

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('Draw a line.')

plt.show()