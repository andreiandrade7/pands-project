# Author: Andreia Santos
# Scope : Project - Fisher’s Iris data set analysis
# Aim : Upload the Fisher’s Iris data set. Perform a series of analysis to the data 


#------------------------------------------------------------------------------
# 0. Index
#------------------------------------------------------------------------------

#The script is organized in the following way
#   1. Upload the data set
#   2. Basis estimations - average , maximum, minimum, standart deviation,  correlation factor
#   3. Histograms creations
#   4. Scatter plot


#  Import python libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



  

#------------------------------------------------------------------------------
#   1 . Upload the data 
#
#   INFO: Data is upload from the file: iris.data located on the same folder as running script analysis.py
#------------------------------------------------------------------------------



frame = pd.read_csv('iris.data', sep=',') # read the info on the file and convert it into a panda dataframe 


dt_array = frame.to_numpy() # convert the previous dataframe into an array. 




def show(dt_array):
    
    print ("\n\n\nPRINTED ARRAY\n")
    print(dt_array)
    print ("\n\n INFO about the raw data")
    print("\tType of data:{}".format(type(dt_array)))
    print("\tSize of matrix is:{}\n\n".format(dt_array.shape))
    



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
    est_avg2 = est_avg.astype(np.float)
    est_avg3=np.around(est_avg2,decimals=2)



    print("\n\n\n")
    print("maximum is:{}".format(est_max))
    print("minimum is:{}".format(est_min))
    print("median is:{}".format(est_med))
    print("average is:{}".format(est_avg3))
    print("standart deviation is:{}".format(est_std2))

    print("\n\n\n")

    
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
# 4 . Data histogram
#------------------------------------------------------------------------------




#------------------------------------------------------------------------------
# XX . Functions call
#------------------------------------------------------------------------------



#show(dt_array) # show the raw data
#estimations(dt_array) # perform some basic analysis do the dataset and save it to "summary-report.txt" file
histograms(dt_array)






################################ trials 

#x=estimations(dt_array)

#print(x)




#print(frame.describe())
