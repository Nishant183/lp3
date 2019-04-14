#import packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#create dataset using DataFrame
df=pd.DataFrame({'X':[0.1,0.15,0.08,0.16,0.2,0.25,0.24,0.3],
                 'y':[0.6,0.71,0.9,0.85,0.3,0.5,0.1,0.2]})
f1 = df['X'].values
f2 = df['y'].values
X = np.array(list(zip(f1, f2)))
print(X)

#centroid points
C_x=np.array([0.1,0.3])
C_y=np.array([0.6,0.2])
centroids=C_x,C_y


#import KMeans class and create object of it
from sklearn.cluster import KMeans
model=KMeans(n_clusters=2)
model.fit(X)
labels=model.labels_
print(labels)

print("P6:(0.25,0.5) belongs to : "+str(labels[5]+1))

#using labels find population around centroid
count=0
for i in range(len(labels)):
    if (labels[i]==1):
        count=count+1

print('No of population around cluster 2:',count-1)
	
#Find new centroids
new_centroids = model.cluster_centers_

print('Previous value of m1 and m2 is:')
print('M1==',centroids[0])
print('M2==',centroids[1])

print('updated value of m1 and m2 is:')
print('M1==',new_centroids[0])
print('M2==',new_centroids[1])

for i in range(len(labels)):
    if (labels[i]==1):
    	plt.scatter(X[i][0],X[i][1],color = 'red')
    else:
    	plt.scatter(X[i][0],X[i][1],color = 'blue')    	
plt.show()    		
