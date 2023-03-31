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

iris['class'].unique() # find out unique classification 
print(iris.groupby('class').size()) # print out above the uniques classification of the iris flowers and the amount of each.

# printing out a number of mathematical principals - 
print (iris.min()) # prints out the minimum measurement of the dataset
print (iris.max()) # prints out the maximum measurement of the dataset
print (iris.mean()) # prints out the mean/average of the measurements/dataset
print (iris.median()) # prints out the medium value of the measurements/dataset
print (iris.std()) # prints of the standard deviation

# creating a table which illustates the above mathematical principals above in the form of a table

summary = iris.describe()
summary = summary.transpose()
print (summary.head ())

# basic scatter plot
iris.plot(kind = "scatter", x = "sepallength", y = "petallength", color = "red") # visualising some of the data in a scattergraph

plt.title ("sepal vs petal", color = "green")  # title of the scattergraph

# basic boxplot to visualise one or more groups of numerical data. It compares the distributions of the Sepal Length, Sepal Width, Petal Length and Petal Width




plt.show()