import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('data.csv', sep=',', index_col=0)
df.plot()
plt.show()
