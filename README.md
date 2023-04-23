# Pands Project - Fisher Iris dataset #

## Introduction ##

The Iris flower data set is a well known data set used to demonstrate various statistical models or algorithims. This data set is the core focus of presenting my learning in the Programming and Scripting module of the Higher Diploma in Data Anslytics from the ATU - the ATlantic Technologcal UNiversity

I will begin this project with a brief history of the Fisher Iris data set.

Sir Ronald Aylmer Fischer was born in London England in 1890. He was a statisician and a geneticist. In 1912 he graduated from Cambridge University with a degree in astronomy. He founded the  Cambridge Society eugenics Society. HE held many prestigious positions in his career. In 1933 he was a Galton Professor of Eugenics in UNiversity College London. In 1943 He was appointed the BAlfour Professor of Genetics at Cambrige. He was a forerunner in the application of statistical procedures to scientific experiments. Fisher developed formula for his "exact test", the "maximum likelihood estimator" and the "analysis of variance".
His work included the following three papers: Statistical Methods for research (1925), The Genetical Theory of NAtural Selection (1930) and Statistical Methods and Scientific Inference (1956)

In 1936 he published a paper titled "The Use of Multiple Measurements in Taxanomic Problems" in the journal "Annals of Eugenics". In this paper he described a linear function to differentiate between three species of the Iris flower genus.

The data he used in the paper was collected by botanist Edgar Anderson in the Gaspe Peninsula of Canada. Edgar Anderson graduated from Michigan State College in 1918 with a degree in botony and agriculture. In 1920 he was awarded a masters and in 1922 he was awarded a doctorate of science in agricultural genetics.

The data Me Anderson collected quantifies the morphologic variations of 3 species of Iris flowers : the Iris Versicolor, Iris Setosa and the Iris Virginica.

[Iris Versicolour, Iris Setosa and the Irish Virginica](https://www.google.com/imgres?imgurl=https%3A%2F%2Fs3.amazonaws.com%2Fassets.datacamp.com%2Fblog_assets%2FMachine%2BLearning%2BR%2Firis-machinelearning.png&tbnid=P-PGjABuYKeYpM&vet=12ahUKEwjGwrvMpOz9AhVEFMAKHa9qCdgQMygAegUIARCUAQ..i&imgrefurl=http%3A%2F%2Fwww.lac.inpe.br%2F~rafael.santos%2FDocs%2FCAP394%2FWholeStory-Iris.html&docid=DWcNzEt0Tz4F4M&w=1275&h=477&q=3%20species%20of%20irish%20flowers%20in%20the%20data%20set&ved=2ahUKEwjGwrvMpOz9AhVEFMAKHa9qCdgQMygAegUIARCUAQ)

The data set has 50 samples of each of the three species. So 150 samples total. The four features of the flowers that were measured were the petal length, the petal width, the spepal length and the spepal width. 

Refernces for the above information include:

[History of the Fisher Anderson Iris data set](https://kaggle.com/datasets/arshid/iris-flower-dataset)

[Encyclopedia Britannica](https://www.britannica.com/biography/Ronald-Aylmer-Fisher)

[Wikipedia](https://en.wikipedia.org/wiki/Edgar_Anderson)

[Kaggle](https://www.kaggle.com/datasets/uciml/iris)

[Another resources](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)



---

## Uses of the Iris Fisher dataset ##

The Iris dataset is widely used in pattern recognition learning. One varient of the Iris flower is linearly separable from the other 2 varients. Those two varients are not linerly separable from each other.

Thw data set is used in data exploration, machine learning and data visualisaetion. it is well understood dataset that can be used to demonstarte many concerpts of data science. Many resources can be fouond online and is thus ideal for beginners of data science.

Data Exploration - The analysis of the data set can be used to identify patterns and relationships in the data.
Machine Learning - Algorithims can be developed to classify the different Iris species based on charcteristics in the data set.
Data Visualisation - The data set can be visualised using histograms, scatter graphs and box plots.

[LevelUpGitConnected](https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d)

## Technology Used ##

### Python ###

Python is a high level programming language. It was developed by Guido van Rossum in 1991. It has many applications including : web development, software development, maths and system scripting. Python can work on many different platforms and has a simple syntax simialr to english. It is popular because of its readability. It allows its users to develop programs that have fewers lines that other programs such as C. Code can be executed quickly as it runs on an interpreter system. Python has many inbuilt libraries to assist the user. Examples of the libraries I will be using in this project are :

### Matplotlib ###

Matplotlib is a tool for use in python programming. It is a library used to create visualisations of data in python.
Matplotlib makes easy things easy and hard things possible - Quote from [matplotlib](https://matplotlib.org/)
Types of plots that can be created with matplotlib include: plot graphs, scatter plots and histograms.

### Seaborn ###

Seaborn is based on Matplotlib, seaborn is a library of tools wihich can be used to visualise data through python.
Seaborn provides a high-level interface for drawing attractive and informative statistical graphics. [seaborn](https://seaborn.pydata.org/#:~:text=Seaborn%20is%20a%20Python%20data,attractive%20and%20informative%20statistical%20graphics.)

### Pandas ###

Pandas is an open source Python library that is most widely used for data science/data analysis and machine learning tasks. It is related to and builds upon another Python package called numpy. 
Pandas is used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008. 
[w3schools](https://www.w3schools.com/python/pandas/pandas_intro.asp#:~:text=What%20is%20Pandas%3F,by%20Wes%20McKinney%20in%202008.)

### NumPy ###

NumPy is a Python library. It is used for working with arrays. It works with linear algebra and matrices
NumPy is short for "Numerical Python". It was created in 2005 by Travis Oliphant. It is an open source project.
[w3schools](https://www.w3schools.com/python/numpy/default.asp)

-----

## Analysis ##

Initially I completed a basic exploration of the the iris dataset to analyse the data. 
I then created a number of different types of graphs/plots to visualise the data set - this could help identify patterns in the data.

The first step for me was to import the iris data set. I imported this into git hub from [UCI Machine Learning repository](https://archive.ics.uci.edu/ml/datasets/iris). 
I then used the command git pull to have it in my Visual Basic pands -project folder. This was then available to use in my analysis.

I imported the folowing librarys for use in my analyis - numpy, matplotlib, seaborn and panda. See above for brief descriptions of these libraries.

I made liberal use of comments to explain my analysis of the data.

The shape prompt showed that the dataset I downloaded has 5 columns and 150 rows.
The columns prompts showed the titles of each column 
THe class prompt named the flower variety/class and the number of data points collected for each class - i.e 50
The head prompt prints out the first ten rows of the dataset. The first ten lines are data points collected from the Setosa class. This is how the data was compiled/listed.
The tail prints out the last ten lines of the data set. This data belongs to class virginica - because of how the data was compliled/listed.
The unique prompts is a different method of naming the variet/class and the data points collected for each.
The null command lists any missing entries - there were none

The describe command creates a table conatining descriptive statistics of the data. From this we can see that the Iris virginica has the longest average sepal length. iris setosa has the shortest average sepal length 4.3.

Correlation is a statistical method that expresses the relationship between variables. The corelation coefficient ranges from -1 to +1. The closer to 0 the weaker the linear relationship. Positive values indicate a positive corelation - the values of the valiable increase together. Negative values - when one variable's value increase the other decreases. Looking at the corelation table of the Iris dataset we can deduce: Iris setosa : sepal length and sepal width are highly co-related - the longer the seapl, the wider it is. In versicolor -petal length and petal width are the most corelated variable. The longer the petal the wider it is. In virginica - the strongest correlation is between petal length and sepal length - 0.864225.

[staistics](https://www.jmp.com/en_ca/statistics-knowledge-portal/what-is-correlation.html#:~:text=Correlation%20is%20a%20statistical%20measure,together%20at%20a%20constant%20rate)


### Scattergraphs ###

I created a number of scatterplots from the basic to  more complex. I used different libararies (matplotlib and seaborn) to give resources for my graphs.
I used different dimensions on each axis, (dimensions being sepallenth, sepal width, petal length, petal width), in the hope that I can use them to clearly distinguish between the species.

My initial scatterplot - all points were blue in colour. There was no distinguishing between the species.
using the seaborn library I was able to give each specied a specific colour or hue. 
My first graph using seaborn had sepalwidth on y axis and sepallength on y axis. i also added a legend - class setosa is blue, veriscolor is orange and virginica is green. On this graph the blue points (setosa) was clustered together and orange (versicolour) and green (virginica) were mixed up. This clearly shows that setosa is easily identifying . Veriscolour and virginica are indistinguishable from each other when those two dimensions are being compared. ( There was one blue spot separated form the cluster)

I than plotted more scattergraphs, (using pairplot), using different dimensions on the axes and comapring all to see if I could get a graph where versicolour and virginica are are more distingusihable from each other. This produced a matrix of scattergraphs and histograms. The legend was the same as above. On all graphs setosa was clustered together - easily identifiable/classified. I found the graph that had petal width on the x axis and petal length on the y showed the separation of the classes and there was only a small amount of overlap. Setosa was completely separated. So if I picked an iris flower and measured the petal width and pletal width I would have nearly 100 confidence that if I identified it as a setosa based on this graph - i would be correct. I would be more confident with the other two but there is still a level of unsurity.
The average petal length for Stosa is much smaller than the other two varieties. The Virginica has the largest measurements in petal lengths and there is overlaps with the last variety -versicolor.
The line graph clearly shows the overlap and length of dimensions where there would be an unsurity. Measurements above and below this area of overlap would be clear as to the class of the flower.

I found resources on youtube very helpful with my analysis above. An example of this is [Iris Dataset EDA leactur 1 and 2](https://youtu.be/FLuqwQgSBDw)

### Histogram ###

I completed histograms for several of the attributes separately. These were not separated into species therefore not very illustrative of the data.

I used pairplot to complete my scattergraphs. It also histograms which not only demonstrated the different attributes but it also defined the species in each. The different colours made the species more distinct and therefore the histograms were easily read. Again the histograms illustrated that the measurements of spepal length and width made it very difficult to distinguish between the different species. One you look at histograms illustrating the petal length and width the species are more easily distinguishable. Setosa is set away from the other two. Virginica and Versicolour are intermingled in the middle measurements but can be distingusihed at the outer limits of the measurements - veriscolour in the measurements, virginica in the higher - referring to the x axis. 

Histograms - I recieved assistance from website [geeksforgeeks](https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/). I also used [kaggel](https://www.kaggle.com/code/kstaud85/iris-data-visualization)

### Boxplots ###

A boxplot is another type of graph that is used to visualise data. the shape of the boxplot shows how the data is distributed and it shows any outliers. It shows a 5 number summary - the minimum, first quartile, median, third quartile and maximum. The line in the middle is the median.

My initial boxplot was a very simple reprentation of all of the data types collected - sepallenth, sepalwidth, petallength and petalwidth. Shows the minimum data sample in each category, the median and the maximum. THe boxes show the lower and upper quartiles of the data in each category. The data isn't does not discriminate between the Iris species/classes. I than decided to create four tables of each category/attribute which also represents the classes. The output of this code is illustrative of the data set and the differences between each class/species. This graphs shows the clear differences between sertosa and the other two classess in almost all attributes. Setetosa is clearly searately and easily identifyable while the other two cannot be easily distinguished except at the outer ranges of the data - minimum and maximum measurements. The onle oddity is the seratosa has the largest variation in sepalwidth.
I used [geekforgeeks](https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/), [Nick McCullum](https://www.nickmccullum.com/python-visualization/boxplot/), [datascience learner](https://www.datasciencelearner.com/matplotlib-boxplot-example-in-python/), [angelaC](https://www.angela1c.com/projects/iris_project/investigating-the-iris-dataset/)

### Piechart ###

I decided to do a simple pie chart representation of the data - just to have practice with this aspect of data visualisation

## Summary ##

The Iris data set is easily imported and is a very useful tool to demonstrate how python can be used to vsualise data.  Data analysis is the process of examining a data set and summarising the main characteristics of the set. It is beginner friendly and there are many only resources to explain the history of the dataset, what the dataset represents and how to use inbuilt libraries in Python to vsiualise the data in the set. The data set is easily understood and the species/classification is easily visualised.
In doing this project I gained experience in using Python's inbuilt libraries - Pandas, Matplotlib and Seaborn. 
Initally I used pandas to explore the dataset and to show the data it contains in various different ways.
I then used Marplotlib and Seaborn to create graphs/plots to easily vsiualise the data. I produced various histograms, scatterplots and boxplots. I made an attempt to creat a piechart.
My first plots were basic in nature and it was difficult to distinguish between the 3 different flowers or the attributes of the flowers.
I then used differnt colour schemes and labelling to make the data clearer and to distuguish between the varieties and their attributes. The latter visualisations clearly shows how visualising the data in terms of plots can help the user to distinguish between the varieties of the flowers and where mistakes could be made in the identification , it where the data could indication both versicolour and visrginica. Setosa is easily identifies from looking at the plots. There are overlaps in the data of the other two which indicates that mistakes can be made if the measurements falls with the overlapping areas.
The visualisations highlight both the similarities and the differences between the species.
In conclusion the setosa variety is clearly distinguishable from the other two varieties. Versicolour and Virginica can be indeistuishable from each other exept at the the extremes of their attribute measurements - verginica at the upper limits of the data and versicolour at the lower.
The Iris dataset clearly demonstarates the linear discriminant - it shows a linear combination of features that characterises or separates two or more classes of objects.









