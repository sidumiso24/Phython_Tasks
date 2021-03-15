# IrisDatasetPlot.py
# Written by: Sidumiso Debbie Mabaso
# Date: 29 July 2020
# Function : This program display 12 subplots

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

fig, subs = plt.subplots(4,3)

iris = load_iris()
data = np.array(iris['data'])
targets = np.array(iris['target'])

cd = {0 : 'r', 1 : 'b', 2 : "g"}
cols = np.array([cd[target] for target in targets])

# Row 1

subs[0][0].scatter(data[:,0], data[:,1], c = cols)
subs[0][1].scatter(data[:,0], data[:,2], c = cols)
subs[0][2].scatter(data[:,0], data[:,3], c = cols)

# Row 2

subs[1][0].scatter(data[:,1], data[:,0], c = cols)
subs[1][1].scatter(data[:,1], data[:,2], c = cols)
subs[1][2].scatter(data[:,1], data[:,3], c = cols)

# Row 3

subs[2][0].scatter(data[:,2], data[:,0], c = cols)
subs[2][1].scatter(data[:,2], data[:,1], c = cols)
subs[2][2].scatter(data[:,2], data[:,3], c = cols)

# Row 4

subs[3][0].scatter(data[:,3], data[:,0], c = cols)
subs[3][1].scatter(data[:,3], data[:,1], c = cols)
subs[3][2].scatter(data[:,3], data[:,2], c = cols)

plt.show()