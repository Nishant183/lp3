import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('datasetAss3.csv')
X = dataset.iloc[:, [0, 1]].values  # IV
Y = dataset.iloc[:, 2].values  # DV
X.astype(np.float64)
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X, Y)
print("Enter the Xcoordinate of point")
frst = int(input())
print("Enter the Ycoordinate of point")
scnd = int(input())
X_pred = [(frst, scnd)]

Y_pred = classifier.predict(X_pred)

# Plotting
# Plot initial data


orange = dataset.loc[dataset['Color class'] == 'Orange']
blue = dataset.loc[dataset['Color class'] == 'Blue']



plt.scatter(dataset['X'],dataset['Y'],c=dataset['Color class'],label='data')

# Results
print("KNN SAYS that YOUR POINT WILL BE.... ")
if (Y_pred == 'Orange'):
    print("Orange in COLOUR")

    plt.plot(frst, scnd, color='Orange',marker='*', label='Data')        

    plt.xlabel('X coordinate', color='black')
    plt.ylabel('Y coordinate', color='black')
    plt.title('Plotting of datapoints', color='black')
    plt.xticks(color='black')
    plt.yticks(color='black')
    plt.legend()
    plt.show()
elif (Y_pred == 'Blue'):
    print(" Blue in COLOUR")
    
    plt.plot(frst, scnd, color='Blue',marker='*', label='Data')
    
    plt.xlabel('X coordinate', color='black')
    plt.ylabel('Y coordinate', color='black')
    plt.title('Plotting of datapoints', color='black')
    plt.xticks(color='black')
    plt.yticks(color='black')
    plt.legend()
    plt.show()

else:
    print("Can't Decide")
    
    
    
