"""
Write a program to draw a box plot of day by tips for a dataset given in a url
https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
data = pd.read_csv(data_url)

sb.boxplot(x="day", y="tip", data=data)
plt.show()
