# Pands Project
# Iris Fisher data set
# Author : MAry Metcalfe

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

iris =pd.read_csv("iris_csv.csv") # this uses the imported iris_cv dataset

print (iris.shape) # this prints out the number of data points and the number of columns across

print (iris.columns) # this prints out the titles of the columns

print (iris["class"].value_counts()) # this prints out the class/species of the flowers and the number of data counts for each - 50. This is an example of a balanced dataset

print (iris.head(10)) # print out the first ten rows of the dataset

iris.plot(kind = "scatter", x = "sepallength", y = "petallength", color = "red") # visualising some of the data in a scattergraph

plt.title ("sepal vs petal", color = "green")  # title of the scattergraph



plt.show()