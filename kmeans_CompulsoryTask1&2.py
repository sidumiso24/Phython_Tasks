# kmeans.py
# Written by: Sidumiso Debbie Mabaso
# Date: 03 August 2020 


# importing packages needed
import math
import csv
import random
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

#Some hints on how to start have been added to this file.
#You will have to add more code that just the hints provided here for the full implementation.
fig = plt.figure()
ax1 = plt.subplot(1,1,1)

cd = {1: 'ro', 2: 'yo', 3: 'bo', 4: 'go', 5: 'co', 6: 'mo'}

# Defining a function that computes the distance between two data points
def distance(point1,point2):
    x = (point1[0] - point2[0])**2
    y = (point1[1] - point2[1])**2
    return math.sqrt(x+y)
    
    
with open('databoth.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter= ',')


# Defining a function that reads data in from the csv files 
def csvReader (theFile):
    f = open(theFile, 'r')
    xy = {}
    fReader = csv.reader(f)
    i = 0 
    for row in fReader:
        if i >0:
            xy.update({row[0]: [float(row[1]), float(row[2])]})
        i += 1
    return xy
        



# Writing the initialisation procedure
databoth = csvReader('dataBoth.csv')
numSamples = int(input("How many clusters should we make? \n"))
setNumberOfClusters = numSamples
iterations = int(input("How many iterations would you like to do? \n"))
setNumberOfIterations = iterations

sampleCount = 1
#samples will be the random starting points
samples = {}
#creating a dictionary to calculate means
means = {}
#creating a dictionary of removed countries
removed = {}
#Convergence meter
sumSquaredDistances = {x:0 for x in range(1,setNumberOfClusters+1)}


#Looping over until we've created desired number of clusters
while numSamples >0:
    #randomSample is the name of the country
    randomSample = random.sample(list(databoth), 1)[0]
    print ("random Sample = " + str(randomSample))
    #updating samples with randoms
    samples.update({sampleCount: databoth[randomSample]})
    means.update({sampleCount:{randomSample: databoth[randomSample]}})
    #removing starting sample from dataset
    sampleCount += 1
    numSamples -= 1
    # plotting initial points only if not iterating
    if iterations == 1:
        ax1.plot(databoth[randomSample][0], databoth[randomSample][1], 'yx')
    removed.update({randomSample:databoth[randomSample]})
    del databoth[randomSample]

sampleCount -= 1
#counter to make sure removed data only gets added in the first iteration
dataCounter = sampleCount

print (samples)
print ("means is = " + str(means))

# Implement the k-means algorithm, using appropriate looping


while iterations>0:

    #Iterate through each row in the file
    for row in databoth:
        d = 1000000 #set d as a high number, so that we know it will be reset on the first comparison
        colour = 1

       #Iterate through the samples and compare to each datapoint to find which sample each point in the file is nearest to.
        for sample in samples:
            newD = distance(databoth[row], samples[sample])
            if newD<d:
                d = newD
                colour = sample
            sumSquaredDistances[sample] += d    
        (means[colour])[row] = databoth[row]
        
        
        if iterations == 1:
            ax1.plot(databoth[row][0], databoth[row][1], cd[colour])
        
    
    print ("SumSquaredDistances: " + str(sumSquaredDistances))
    sumSquaredDistances = {x:0 for x in range(1,setNumberOfClusters+1)}

    #Compute the means for each cluster
    while sampleCount >0:
        x=0
        y=0    
        for country in means[sampleCount]:    
            x+=means[sampleCount][country][0]
            y+=means[sampleCount][country][1]
        xMean = x/len(means[sampleCount])
        yMean = y/len(means[sampleCount])
        mean = [xMean, yMean]
        #make new starting points
        samples[sampleCount] = mean
        sampleCount -= 1
        numSamples += 1
        
    #add removed samples back to the dataset
    databoth.update(removed) 
    final = means
    means = {}
    while numSamples >0:
        means.update({numSamples:{}})
        sampleCount += 1
        numSamples -= 1    
    
    
    iterations -= 1


    # Print out the results
for clusters in range(1,setNumberOfClusters+1):
    print ("The number of countries in cluster " + str(clusters) +": " + str(len(final[clusters])))
    print ("The Countries in cluster " + str(clusters) + " are: \n" + str(final[clusters].keys()))
    print ("The mean life expectancy of cluster " + str(clusters) + " is " + str(samples[clusters][0]))
    print ("The mean birth rate of cluster " + str(clusters) + " is " + str(samples[clusters][1]))
plt.show()

