# -*- coding: utf-8 -*-
"""Diabetes_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mhaZJv2MR-UZLgbePId3DMJoCPLBqm3d
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm #support vector model
from sklearn.metrics import accuracy_score

"""Data Collection and Data Analysis

PIMA Diabetes Dataset
"""

diabetes_dataset = pd.read_csv('/content/diabetes.csv')

diabetes_dataset.head()



"""pd.read.csv? - gives all the info regarding the method"""

diabetes_dataset.shape

diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""0 - Non-diabetic
1 - Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']

print(X, Y)

"""Data Standardization"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X,Y)

"""Training and Testing Data seperation"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

print(Y.shape, Y_train.shape, Y_test.shape)

"""Training the model

"""

classifier = svm.SVC(kernel='linear')

classifier.fit(X_train, Y_train)

"""Model Evaluation"""

X_train_prediction = classifier.predict(X_train)
X_train_accuracy = accuracy_score(X_train_prediction, Y_train)
print('The accuracy score for the training data: ',X_train_accuracy)

"""Accuracy on test data"""

X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('The accuracy score for the test data: ',test_data_accuracy)

"""Making a predictive system"""

input_data = (3,113,50,10,85,29.5,0.626,25)
input_data_as_numpy_array = np.asarray(input_data)
print(input_data_as_numpy_array) 

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
input_data_scaled = scaler.transform(input_data_reshaped)
print(input_data_reshaped, input_data_scaled)

prediction = classifier.predict(input_data_scaled)
print(prediction)

if prediction[0] == 0:
  print('The patient is not diabetic!')
else:
  print('The patient is diabetic!')

