#Import necessary libraries
import numpy as np # for numerical computations
import pandas as pd #for handling the dataset
import matplotlib.pyplot as plt #for plotting graphs

#step-1 load the dataset
dataset = pd.read_csv('C:\Users\Student\Downloads\Salary_Data.csv')
dataset.head()

#step-2 data preprocessing
#extract independent variable (years of experience)
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

#step-3 split the dataset into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(x, y, test_size= 1/3,random_state=0)

#step-4 train the linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#step-5 predict the salaries for the test set
y_pred = regressor.predict(X_test)
print("Predicted salaries:",y_pred)
print("Actual salaries:",y_test)

#step-6 Visualise the results
#Plot for the training set
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train),color='blue')
plt.title("Salary vs Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

#plot for test set
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train),color='blue')
plt.title("Salary vs Experience (Test Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
