import matplotlib.pyplot as plt
with open("test.txt") as f:
    data = f.read()
    x=[]
    y=[]
    data= data.split('\n')
    data.remove(data[-1])
    for row in data:
         x.append(int(row .split(' ')[0]))
         y.append(int(row.split(' ')[1]))

plt.plot(x,y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw  Graph')
plt.show()


