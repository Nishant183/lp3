import matplotlib.pyplot as plt
import pandas as pd

# Read Dataset
dataset=pd.read_csv("data1.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

# Import the Linear Regression and Create object of it
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)
Accuracy=regressor.score(X, y)*100
print("Accuracy :"+str(Accuracy))

# Predict the value using Regressor Object from user input
hours=int(input('Enter the no of hours : '))
y_pred=regressor.predict([[hours]])
print('Risk score ' + str(y_pred))

#calculate the value of y
print("equation of line is : risk_score = %f * hours + %f"%(regressor.coef_,regressor.intercept_))

import matplotlib.pyplot as plot
plot.scatter(X, y, color = 'red')
plot.plot(X, regressor.predict(X), color = 'blue')
plot.title('Title')
plot.xlabel('Number of hours spent driving')
plot.ylabel('Risk score on a scale of 0-100')
plot.show()