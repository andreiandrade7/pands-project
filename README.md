# Author: 
Andreia Santos

# Scope : 
Project - Fisher’s Iris data set analysis

# Aim : 
Upload the Fisher’s Iris data set. Perform a series of analysis to the data 

# Files: 
   -Python script: analysis.py
   -Output text file: summary-report.txt
   -Output plot images: histogram.png, scatter.png, pie-chart.png


# Dataset description:
    -The current script requires as input the raw data named "iris.data". This will be automarically upload from the url is not uploaded om the working directory. 
    - The "iris.data" corresponds to a matrix with size: 149 rows X 5 columns. 
    -The first 4 columns represent the attributte information, namely: "sepal length" , "sepal width","petal length"  and "petal width" in cm
    -The 5th column (last) represents the classification of the of iris plant, namely : "Iris Setosa", "Iris Versicolour" and "Iris Virginica"
    -Each occurence, represented by a row  refers to a type of iris plant


# Script run:
    -Requirement: To run the script is necessary to have a  code editor plataform . The used for this developement was: Visual Studio Code 
    -The script is running by typing on the terminal :  python .\analysis.py
    -A sequential steps occur namely:
        .All needed libraries and the database are upload
        .A menu is prompted which gives the user the right to chose within a set of options:
            > 1.Vizualize numeric data on the console
            > 2.Estimate a summary report of each attribute - example: sepal length(average ,maximum, minimum, standart deviation). This information is exported to a file called summary-report.txt
            > 3.Plot histograms into a new opening window. This gives a genereric ideia of the values distribution of each atribute.
            > 4.Scatter plots into a new opening window. This gives a genereric ideia of the distribution of each atribute for the considered types of iris plants. For example, considering for "petal lenght" is is easily distinguish ("<2")iris-setosa from other two iris types( ">2.2") 
            > 5.Plot a pie chart  into a new opening window  - gives an idea of the distribution of each iris type. One must conclude that the data set is well distributed between all three iris types.        

# References 
1. https://www.geeksforgeeks.org/python-os-path-exists-method/
2. https://numpy.org/doc/stable/reference/generated/numpy.mean.html
3. https://numpy.org/doc/stable/reference/generated/numpy.std.html
4. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html
5. https://realpython.com/visualizing-python-plt-scatter/
6. https://docs.python.org/3/library/enum.html
7. https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
8. https://stackoverflow.com/questions/19964603/creating-a-menu-in-python

#------------------------------------------------------------------------------

