"""
Write a program to draw a point plot for sex against survived for a dataset given in url
https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset("titanic")
sb.pointplot(x="sex", y="survived",hue="class", data=df)
# to get list of data set available for sea born
print(sb.get_dataset_names())
plt.show()
