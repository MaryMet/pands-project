# Pands Project
# Iris Fisher data set
# Author : MAry Metcalfe

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

iris =pd.read_csv("iris_csv.csv") # this uses the imported iris_cv dataset

print (iris.shape) # this prints out the number of data points and the number of columns across
iris.describe()

print (iris.columns) # this prints out the titles of the columns

print (iris["class"].value_counts()) # this prints out the class/species of the flowers and the number of data counts for each - 50. This is an example of a balanced dataset

print (iris.head(10)) # print out the first ten rows of the dataset - contains data about sertosa - just how the data was compiled
print (iris.tail(10)) # print out the last ten rows of the dataset - contains data about virginica - just how the data was compiled

iris['class'].unique() # find out unique classification 
print(iris.groupby('class').size()) # print out above the uniques classification of the iris flowers and the amount of each.

print(iris.isnull().sum()) # check is the data has any missing values

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
plt.show

# another scatter plot - sepal length and sepal width

iris.plot(kind="scatter", x = "sepallength", y =  "sepalwidth")
plt.show()
# no discrimination between species. Visualisation is not clear.


# using seaborn to distinguish the graph by species -sns
sns.set_style("whitegrid")
sns.FacetGrid(iris, hue="class", height=4) \
    .map(plt.scatter, "sepallength", "sepalwidth") \
    .add_legend()
plt.show()
# the species are distingushed by colour and the differences easily seen by using seaborn and compared to the scatter graph above.
# blue, class setosa, is separated from the other two - versicolour -orange and virginica. This can be used to identify/clasify setosa easily but not the other two.
# one setosa could be misclassified because of where it is situated on this graph.

# below will print out a number of graphs that will dispalay comparisons between the differnt measurements/dimensions measured- sepallength, petallenth, speal width, petal width
# one of these may give the best dimension comparison to completely separate the species thus leading to better tools for identification

plt.close()
sns.set_style("whitegrid")
sns.pairplot(iris, hue="class", height=3, diag_kind="hist") # diag_kind - changed line graph to histograms
plt.show()
# petal width on the x ais and the other dimensions on the y axis seem to give best grouping/separtion thus being a tool for identification.

# histogram to show sepal length

plt.figure(figsize = (10,7))
x = iris['sepallength']

plt.hist(x, bins =20, color = "blue")
plt.title(" Sepal Length in cm", color = "blue")
plt.xlabel("Sepal Length" , color = "blue")
plt.ylabel("Count", color = "blue")
plt.show()

# histogram for sepal width
plt.figure(figsize = (10,7) )
x = iris['sepalwidth']

plt.hist(x, bins =20, color = "red")
plt.title("Sepal Width", color = "red")
plt.xlabel("sepalwidth", color ="red")
plt.ylabel("Count", color = "red")
plt.show()

# histogram for petal length
plt.figure(figsize = (10,7) )
x = iris['petallength']

plt.hist(x, bins =20, color = "green")
plt.title("Petal Length", color = "green")
plt.xlabel("Petallength", color ="green")
plt.ylabel("Count", color = "green")
plt.show()

#histogram for petal width
plt.figure(figsize = (10,7) )
x = iris['petalwidth']

plt.hist(x, bins =20, color = "yellow")
plt.title("Petal Width", color = "yellow")
plt.xlabel("Petalwidth", color ="yellow")
plt.ylabel("Count", color = "yellow")
plt.show()


# box plot - displays how the data is distributed and any outliers
# basic boxplot to visualise one or more groups of numerical data. It compares the distributions of the Sepal Length, Sepal Width, Petal Length and Petal Width

plt.figure(figsize = (10, 7)) # basic boxplot which compares the differnet attributes in the dataset
iris.boxplot() # there is no clear distinction between species
plt.show()

#More boxplots to visualise the data - 4 box blots according to different data sets to visualise differences between species

sns.set(style="darkgrid", palette="deep")  # identifying a style and theme to easily differentiate between the different species/classes
f, axes = plt.subplots(2, 2, sharey=False, figsize=(10, 10)) # 4 boxplots - 2 on top and 2 at bottom
sns.boxplot(x="class", y="petallength",data=iris, ax = axes[0,0], hue="class") # using seaborn to draw the boxplots. x is the class/species and the y axis contains data from petallength. Hue = legend
sns.boxplot(x="class", y="sepallength", data=iris, ax= axes[0,1]) # uses seaborn. x axis has the class/sepies, y axis the sepal length
sns.boxplot(x="class", y="petalwidth" ,data=iris, ax= axes[1,0]) # uses seaborn. x axis is the class/species, y axis is petal width
sns.boxplot(x="class", y="sepalwidth", data=iris, ax= axes[1,1]) # uses seaborn. x axis is the class/species. y axis is the sepal width
f.suptitle("Boxplot of the iris plant data set to visualise differences")
plt.show()

print(iris.groupby("class").describe())
print(iris.groupby("class").corr())

# piechart - another method of visualising data
#colors = sns.choose_dark_palette
#labels=["Iris-setosa, Iris-versicolor, Iris-virginica"]
#explode=(0,0,0.1)
#plt.pie(iris["class"].value_counts(),labels=labels,explode=explode, colors = "colors", autopct="%1.1f%%")
#plt.title("Distribution")
#plt.show()

#iris["class"].value_counts().plot(kind="pie")

#plt.show

