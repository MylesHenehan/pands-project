# pands-project

# Investigation of the Iris Dataset
Author: Myles Henehan
***

## Project Summary
This project consists of an exploration of the Iris Data Set, using Python to examine its attributes and form a conclusion about the data contained within. There will be 3 main aims to this project; the first will be to identify the variables present in the data set and export each of them to a single text file. The second approach will be to produce representations of said variables in the form of histograms, and save them as png files. Finally, we will produce a scatter plot of each of the variables, and conclude by providing any other relevant analysis that may be of interest to someone investigating this data set.

## Background of the Dataset
First introduced in 1936 by British statistician Ronald Fisher in his paper titled "The use of multiple measurements in taxonomic problems," the Iris Data set is a staple in the field of machine learning and statistics, and serves as a simple, straightforward source of data through which beginners in the field of data analytics can build up their knowledge.

The data set contains 150 instances, split evenly between 3 different types (otherwise known as classes) of Iris flower. These types are setosa, versicolor, and virginica. Moreover, each flower has 4 different features (known as variables): sepal length, sepal width, petal length and petal width. This combination of classes and variables gives students in the field of data science a simple yet all-encompassing set of data through which to explore data representation using Python.

## Variables within the Dataset


## Contents of the py file
The main component of this project is a Python file called analysis.py, which carries out a number of actions to help us explore the Iris data set. It is also accompanied by a file named functions.py, which stores the main functions created for this project.

- Reads in the dataset and assigns each data frame to a variable name
- Writes a description of each of the 4 main numerical variables and stores this in a single txt file.
- Outputs histograms to show the spread of each numerical variable and saves these as png files.
- Creates a set of scatter plots, showing the relationship between each possible combination of variables.
- Using an example scatter plot, fits the best fit line and gets the Pearson Correlation Coefficient
- Addresses the differences between iris species by creating a representation which includes 3 variables

## References
- Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.
- Turney, S. (2022). "Pearson Correlation Coefficient (r) | Guide & Examples". Available at: https://www.scribbr.com/statistics/pearson-correlation-coefficient/#:~:text=The%20Pearson%20correlation%20coefficient%20(r,the%20relationship%20between%20two%20variables [Accessed 14 May 2024]
- Waskom, M. (n.d.). "Visualizing statistical relationships". Available at: https://seaborn.pydata.org/tutorial/relational.html [Accessed 14 May 2024]