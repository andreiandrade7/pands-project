
#  Import python libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




frame = pd.read_csv('iris.data', sep=',') # read the info on the file and convert it into a panda dataframe 


dt_array = frame.to_numpy() # convert the previous dataframe into an array. 

print(dt_array)





# Separate columns 
x = dt_array[:, 0] 
y = dt_array[:, 3] 
classes = dt_array[:, 4] 
print(type(classes))

#creating a dictionary to count the number of occurences 
#data_dict = {i:classes.count(i) for i in classes}

#creating the x and y values for the pie chart 
#x = list(data_dict.keys())
#y = list(data_dict.values())

#creating the pie chart
plt.pie(y, labels=x, autopct='%1.1f%%')

#displaying the pie chart
plt.show()