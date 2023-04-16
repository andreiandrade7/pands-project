# Author: Andreia Santos
# Scope : Project - Fisher’s Iris data set analysis
# Aim : Upload the Fisher’s Iris data set. Perform a series of analysis to the data 

#------------------------------------------------------------------------------
#                            SCRIPT INDEX
#------------------------------------------------------------------------------

#The script is organized in the following way
#   0. Initialization: 
#               0.1) Upload libraries
#               0.2) Upload data set

#   2. Basis estimations - average , maximum, minimum, standart deviation,  correlation factor
#   3. Histograms creations
#   4. Scatter plot
#   5. Extra :
#         5.1)Pie chart

#   X. Show the "Menu Options"


#------------------------------------------------------------------------------
# 0. Initialization
#------------------------------------------------------------------------------



#                                                  0.1) Import python libraries 
#------------------------------------------------------------------------------


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import requests


#                                                          0.2) Upload data set 
#------------------------------------------------------------------------------

#The raw data import is upload either from 1) the current directory-cwd-if the file is available or 2) from the URL if the file is NOT available on the cwd

if os.path.exists('iris.data'): # check if "iris.data" is available to upload from the current directory

        frame = pd.read_csv('iris.data', sep=',') # read the file info and convert it into a panda dataframe 
        print("\n\n\nFile imported successfully from the current directory\n\n\n")

else:

        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        response = requests.get(url) # library responsable for download info from an URL

        with open('iris.data', 'wb') as f: # opens the file "iris.data" from the URL and write it in binary mode
               f.write(response.content)
        frame = pd.read_csv('iris.data', sep=',') # read the info on the file and convert it into a panda dataframe 

        print("\n\n\nFile  successfully download from URL\n\n\n")
        #print (frame)


frame.columns = ["sl", "sw", "pl", "pw", "class"] # atributes an individual id to each column, being (from first to last):sepal lenght, sepal width, petal length, petal width and class
#print(frame)

dt_array = frame.to_numpy() # convert the previous dataframe into an array. 
#print(frame)


#print(dt_array)

 #INFO: Data is upload from the file: iris.data located on the same folder as running script analysis.py


#------------------------------------------------------------------------------
# 1. Show data
#------------------------------------------------------------------------------


def show(dt_array, frame):
        print ("\n\n\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n")
        print ("\n\n\nORIGINAL ARRAY\n")
        print(dt_array)
        print ("\n\n INFO about the raw data")
        print("\tType of data:{}".format(type(dt_array)))
        print("\tSize of matrix is:{}\n\n".format(dt_array.shape))

        print ("\n\n\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n")
        print ("\n\n\nFRAME:\n")
        print(frame)

  
#------------------------------------------------------------------------------
# 2 . Basis estimations
#------------------------------------------------------------------------------

def estimations(dt_array):
    filt_dt=dt_array[:,:-1] # create a new array without the "class" information - useful for the quantitative estimation

    est_max=filt_dt.max(axis=0) # estimate the maximum
    est_min=filt_dt.min(axis=0)# estimate the minimum 
    est_med=np.median(filt_dt, axis=0)# estimate the median

    # estimate standart deviation + round the number (with two decimal places)
    est_std=np.std(filt_dt, axis=0, dtype=float)
    est_std2=np.around(est_std,decimals=2)

    # estimate average + convert the same value to float + round the number (with two decimal places)
    est_avg=np.average(filt_dt, axis=0)
    est_avg2 = est_avg.astype(np.float64)
    est_avg3=np.around(est_avg2,decimals=2)



    print("\n\n\n")
    print("maximum is:{}".format(est_max))
    print("minimum is:{}".format(est_min))
    print("median is:{}".format(est_med))
    print("average is:{}".format(est_avg3))
    print("standart deviation is:{}".format(est_std2))

    print("\n\n\n")

    print("This information is also saved on the automatically generated file 'summary-report.txt' saved on the current working directory ")
  
    with open("summary-report.txt","w") as f:
        f.write("------------------------------------------------------------------------------------------------------------\n")
        f.write("\t\t\t\t\t   Summary of the Fisher's Iris Data Set  \t\t\t\t\t\n")
        f.write("------------------------------------------------------------------------------------------------------------\n")

        f.write("\n\n\t\t\t\tSepal\t\t\t\tSepal\t\t\t\tPetal\t\t\t\tPetal\t\t\t\t\n")
        f.write("\t\t\t\tLength(cm)\t\t\tWidth(cm)\t\t\tLength(cm)\t\t\tWidth(cm)\n\n\n\n")

        f.write("\t") 
        f.write(f"Maximum is:  \t\t{est_max[0]}\t\t\t  {est_max[1]} \t\t\t{est_max[2]} \t\t\t\t{est_max[3]}")
        f.write("\n\n\n\n\t")
        f.write(f"Minimum is:  \t\t{est_min[0]}\t\t\t  {est_min[1]} \t\t\t{est_min[2]} \t\t\t\t{est_min[3]}")
        f.write("\n\n\n\n\t")
        f.write(f"Median is:  \t\t{est_med[0]}\t\t\t  {est_med[1]} \t\t\t{est_med[2]} \t\t\t\t{est_med[3]}")
        f.write("\n\n\n\n\t")
        f.write(f"Average is:  \t\t{est_avg3[0]}\t\t\t  {est_avg3[1]} \t\t\t{est_avg3[2]} \t\t\t\t{est_avg3[3]}")
        f.write("\n\n\n\n")
        f.write(f"Stand Deviation is:  \t\t{est_std2[0]}\t\t\t  {est_std2[1]} \t\t\t{est_std2[2]} \t\t\t\t{est_std2[3]}")
        f.write("\n\n\n\n")

        f.write("------------------------------------------------------------------------------------------------------------\n")
        f.write("\t\t\t\t\t   XXXXXXXXXXXXXXXXXXXXXXXXX  \t\t\t\t\t\n")
        f.write("------------------------------------------------------------------------------------------------------------\n")       


        #return (est_max, est_min, est_med, est_avg3, est_std2)

#------------------------------------------------------------------------------
# 3 . Data histogram
#------------------------------------------------------------------------------

def histograms(dt_array):
        


        plt.figure(figsize=(12,9)) # defines the size of the window for ploting all the 4 histograms on the same window

        # Plot 1 - Sepal Length histogram
        plt.subplot(2,2,1) # divide the window into 2 rows, 2 columns and populate the 1st position with the Sepal Length histogram
        sl=dt_array[:,0] # create a "sl" array with all the value which is on the 1st column of the raw array "dt_array"
        #print (sl)
        plt.hist(sl, color = "green") # with the given data defines a histogram and attibutes a green color to it. no of bins automatically set to 10 which is fine for this data vizualization
        plt.title('Histogram: "Sepal Length"') # name the plot 
        plt.xlabel("Value") # name x axis
        plt.ylabel("Frequency") # name y axis


        # Plot 2 - Sepal Length histogram - similar to previous plot 1
        plt.subplot(2,2,2)
        sw=dt_array[:,1]
        #print (sw)
        plt.hist(sw ,color = "blueviolet")

        plt.title('Histogram: "Sepal Width"')
        plt.xlabel("Value")
        plt.ylabel("Frequency")

        # Plot 3 - Sepal Length histogram - similar to previous plot 1
        print("\n\n\n")
        plt.subplot(2,2,3)
        pl=dt_array[:,2]
        #print (pl)
        plt.hist(pl, color = "red")
        plt.title('Histogram: "Petal Length"')
        plt.xlabel("Value")
        plt.ylabel("Frequency")


        # Plot 4 - Sepal Length histogram - similar to previous plot 1
        print("\n\n\n")
        plt.subplot(2,2,4)
        pw=dt_array[:,3]
        #print (pw)
        plt.hist(pw, color = "blue")
        plt.title('Histogram: "Petal Width"')
        plt.xlabel("Value")
        plt.ylabel("Frequency")


        plt.tight_layout() # avoids overlaping between data/ legends/titles
        plt.show() # show on a window all the plotted info takin into account its positions


#------------------------------------------------------------------------------
# 4 . Scatter Plots
#------------------------------------------------------------------------------

def scatter_plots(dt_array):
     


        plt.figure(figsize=(17,12)) # defines the size of the window for ploting all individual scatter plots on the same window

        # individualize each column in a single array which contain different variables of the raw data

        sl=dt_array[:,0] # sepal length
        sw=dt_array[:,1] # sepal width
        pl=dt_array[:,2] # petal length
        pw=dt_array[:,3] # petal width
        classes=dt_array[:,4] # classes        
        

        classes_unique = np.unique(classes) # identify automatically how many distinct classes there are on the raw data and save them within the array "classes_unique"
        colors = ['purple', 'green', 'blue', 'orange', 'purple']  # initializate a list with colors ids (useful for segmentating the data accordingly to the classe)

        print (type(classes_unique))
        
        ######--------------------------------------------------------- ROW 1 - PLOT

        plt.subplot(4,4,1) # divide the window into 4 rows, 4 columns and populate the 1st position with the "Sepal Length" text. 1st position upper left. the following positions are clockwise rotation
        plt.text(0.3, 0.5, 'SEPAL LENGTH')  #1st position with the "Sepal Length" text
        
        # Sepal lengths plots as a "y" variable. The "x" variable are mentionally individually on the following comments

                # .... scatter with sepal width
        plt.subplot(4,4,2) 
        for i, c in enumerate(classes_unique): # "for" loop that goes through the different type of classes saved on the variable "c" using the counter "i"
          
                xpoints = sw[classes == c] # variable where is saved the "sepal widths" of all "c" class
                ypoints = sl[classes == c] # variable where is saved the "sepal lenght" of all "c" class
                plt.scatter(xpoints, ypoints, c=colors[i], label=str(c))  # scatter plot considering the color that is on "i" position and the label which is inside the "c" variable. This "c" is converted into a string to be inserted as legend of the data

                # .... scatter with petal length
        plt.subplot(4,4,3) 
        for i, c in enumerate(classes_unique):
                xpoints = pl[classes == c] # variable where is saved the "petal length" of all "c" class
                ypoints = sl[classes == c] # variable where is saved the "sepal length" of all "c" class
                plt.scatter(xpoints, ypoints, c=colors[i], label=str(c)) # scatter plot considering the color that is on "i" position and the label which is inside the "c" variable. This "c" is converted into a string to be inserted as legend of the data


                # .... scatter with petal width
        plt.subplot(4,4,4) 
        for i, c in enumerate(classes_unique): # "for" loop that goes through the different type of classes saved on the variable "c" using the counter "i"
                xpoints = pw[classes == c] # variable where is saved the "petal width" of all "c" class
                ypoints = sl[classes == c] # variable where is saved the "sepal length" of all "c" class
                plt.scatter(xpoints, ypoints, c=colors[i], label=str(c)) # scatter plot considering the color that is on "i" position and the label which is inside the "c" variable. This "c" is converted into a string to be inserted as legend of the data



        ###### ROW 2 --------------------------------------------------------- PLOT


        plt.subplot(4,4,6)  #  populate the #6 position with text information:"Sepal Width" 
        plt.text(0.3, 0.5, 'SEPAL WIDTH')    #6th position with the "Sepal width" text


        # Sepal width plots as a "y" variable. The "x" variable are mentionally individually on the following comments

                # .... scatter with petal length (same comments as before)
        plt.subplot(4,4,7) 
        for i, c in enumerate(classes_unique):
                xpoints = pl[classes == c] 
                ypoints = sw[classes == c] 
                plt.scatter(xpoints, ypoints, c=colors[i], label=str(c)) 

                # .... scatter with petal width
        plt.subplot(4,4,8) 
        for i, c in enumerate(classes_unique):
                xpoints = pw[classes == c] 
                ypoints = sw[classes == c] 
                plt.scatter(xpoints, ypoints, c=colors[i], label=str(c)) 


###### ROW 3 --------------------------------------------------------- PLOT


        plt.subplot(4,4,11) #  populate the #11 position with text information:"Petal Width" 
        plt.text(0.3, 0.5, 'PETAL LENGTH')  

        # Petal length plots as a "y" variable. The "x" variable are mentionally individually on the following comments
                # .... scatter with petal length
        plt.subplot(4,4,12) 
        for i, c in enumerate(classes_unique):
                xpoints = pw[classes == c] 
                ypoints = pl[classes == c] 
                plt.scatter(xpoints, ypoints, c=colors[i], label=str(c)) 
                
                
###### ROW 4 --------------------------------------------------------- PLOT


        plt.subplot(4,4,16) # populate the #16 position with text information:"Petal Width" 
        plt.text(0.3, 0.5, 'PETAL WIDTH')  





######  --------------------------------------------------------- PLOT

        plt.legend()
        plt.show() 

#------------------------------------------------------------------------------
# 5 . Extra
#------------------------------------------------------------------------------

 #------------------------------------------------------------------------------
# 5.1. Pie chart
#------------------------------------------------------------------------------

def pieChart(frame):


        #generate a pie chart  

        frame['class'].value_counts().plot.pie(figsize=(10, 10), startangle=90, autopct='%1.1f%%') # counts how many occurences there are in each class and plot them in a chart pie
        plt.title('Iris Species')
        plt.show()





#------------------------------------------------------------------------------
# XX . Functions call
#------------------------------------------------------------------------------



#show(dt_array) # show the raw data
#estimations(dt_array) # perform some basic analysis do the dataset and save it to "summary-report.txt" file
#histograms(dt_array) # perform the histogram of the raw data 
#scatter_plots(dt_array)  # perform the scatter plots of the raw data 
#pieChart(frame)



print("\n\n\n\n\n\n\n")



 #                                                  1.3)Show the "Menu Options"
#------------------------------------------------------------------------------

menu = {}  # Initalizates the menu dictionary
menu['1'] = "Show the data"
menu['2'] = "Basis estimations"
menu['3'] = "Histograms"
menu['4'] = "Scatter plot"
menu['5'] = "Pie chart"

# Print the menu
while True:

    options=menu.keys()
    print ("\n\n\n\n\n")
    print ("----------------------------------NEW RUN----------------------------------")
    for entry in options: 
        print (entry, menu[entry])

    selection=input("Please select the option you would like to perform: ") 
    if selection =='1':
        print ("\n\nSelected option:\n\t\tShow data\n\n")
        show(dt_array,frame)
    elif selection =='2': 
        print ("\n\nSelected option:\n\t\tBasis estimations\n\n")
        estimations(dt_array)
    elif selection == '3': 
        print ("\n\nSelected option:\n\t\tHistograms")
        print ("\t\t(Data plotted on a separate window)\n\n")
        histograms(dt_array)
    elif selection == '4': 
        print ("\n\nSelected option:\n\t\tScatter plot\n\n")
        print ("\t\t(Data plotted on a separate window)\n\n")
        scatter_plots(dt_array)
    elif selection == '5': 
        print ("\n\nSelected option:\n\t\tPie chart\n\n")
        print ("\t\t(Data plotted on a separate window)\n\n")
        pieChart(frame)
        #break
    else: 
        print ("A option from the menu should be inserted, please select a valid number")




