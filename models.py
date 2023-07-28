# models.py
# Machine Learning Algorithm with Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

class Suman:
    def __init__(self, file):
        self.file = file
    
    # Method to read the CSV
    def read_csv(self):
        data = pd.read_csv(self.file)
        return data
    
    # Method for the Machine Learning model based on Linear Regression - Supervised Learning
    def linear_regression_model(self):
        x = self.read_csv().iloc[:, :3]
        y = self.read_csv().iloc[:, -1]
        linear_regression = LinearRegression()
        linear_regression.fit(x, y)
        pickle.dump(linear_regression, open('suman_test_model.pkl', 'wb'))
        return("Pickel Model Generated !")


file = "C:\\Users\\sgang\\OneDrive\\Desktop\\workspace\\ML-With-Flask\\data.csv"

suman = Suman(file)

suman.linear_regression_model()