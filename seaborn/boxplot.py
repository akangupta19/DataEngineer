"""
Write a program to draw box plot of life expectancy by continent for a data set given in a url
https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv
Box Plot Review:
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/a/box-plot-review
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data_url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
data = pd.read_csv(data_url)

sb.boxplot(x="continent", y="lifeExp", data=data)

plt.show()
