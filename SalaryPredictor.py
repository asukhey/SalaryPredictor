# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:15:35 2018

@author: sukhe
"""



import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #Simple Linear Regression model Package

#os.chdir('F:\\Proj\\Salary_Predictor');

data = pd.read_csv('Salary_Data.csv') 


"""Data Preprocessing"""

#Divide Dataset into 2 parts- Independent and Dependent variables

iv=data.iloc[:,0:1].values #Salary is considered as independent variable
dv=data.iloc[:,1].values #Salaries are dependent since they vary on experience.

#Splitting Dataset into Training and test set
iv_train, iv_test, dv_train, dv_test = train_test_split(iv,dv,test_size=1/3,random_state=0)

#Atleast for this case we don't need to worry about feature scaling as regression model takes care of it.

"""On to the main task- Building Simple Linear Regression model and predicting values"""
#Build model and train it
regressor = LinearRegression()
regressor.fit(iv_train,dv_train) #Add Training Values

#Predicting Values - in this case salary of an employee with 6.5 years of experience.

pred_data = regressor.predict(6.5)

pred_data = regressor.predict(iv_test) #Compare this with dv_test (Actual Salaries)

"""Visuatizations of Training and test set"""

#Training Set

plt.scatter(iv_train,dv_train, color='red')
plt.plot(iv_train,regressor.predict(iv_train),color='blue')
plt.title('Salary Predictor')
plt.xlabel('Experience (Years)')
plt.ylabel('Salaries')
plt.show()

#Test Set

plt.scatter(iv_test,dv_test, color='red')
plt.plot(iv_train,regressor.predict(iv_train),color='blue')
plt.title('Salary Predictor')
plt.xlabel('Experience (Years)')
plt.ylabel('Salaries')
plt.show()

