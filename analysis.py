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