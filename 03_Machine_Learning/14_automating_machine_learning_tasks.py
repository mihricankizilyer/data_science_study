# -*- coding: utf-8 -*-
"""3.10 Automating Machine Learning Tasks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hvQ8M5vWVkoA665uCKi7nOt6mtBE5Do3

# Makine Öğrenmesi Görevlerinin Otomatikleştirilmesi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor 
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor

df = pd.read_csv("/content/Hitters.csv")
df = df.dropna()
dms = pd.get_dummies(df[['League','Division','NewLeague']])

def compML(df, y, alg):
  
  # train-test ayrimi
  y= df[y] #bağımlı değişken
  X_ = df.drop(['Salary','League','Division','NewLeague'], axis = 1).astype('float64')
  X = pd.concat([X_, dms[['League_N','Division_W','NewLeague_N']]], axis=1)
  X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.25,random_state = 42)
  
  #modelleme
  model = alg().fit(X_train, y_train)
  y_pred = model.predict(X_test)
  RMSE = np.sqrt(mean_squared_error(y_test, y_pred))
  model_ismi = alg.__name__
  print(model_ismi, "Modeli test hatası:", RMSE)

compML(df, "Salary", SVR)

models = [LGBMRegressor,
          XGBRegressor,
          GradientBoostingRegressor,
          RandomForestRegressor,
          DecisionTreeRegressor,
          MLPRegressor,
          KNeighborsRegressor,
          SVR]

for i in models:
  print(compML(df, "Salary", i))

