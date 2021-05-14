# -*- coding: utf-8 -*-
"""3.1 K Nearest Neighbor

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1urbV8eebMu54i8tOcGYdJVOCCXYyqFK0

# **DOĞRUSAL OLMAYAN REGRESYON MODELLERİ**

- K En Yakın Komşu
- Destek Vektör Regresyonu
- Yapay Sinir Ağları
- CART
- Random Forest
- Gradient Boosting Machines
- XGBoost
- LightGBM
- CatBoost

## **K En Yakın Komşu**

- Gözlemerin birbirine olan benzerlikleri üzerinden tahmin yapılır.

- Sınıflandırma ya da regresyon problemlerinde kullanılabilen algoritmadır.

- Paranetrik olmayan bir öğrenme türüdür.

Bağımsız değişken değerleri verilen gözlem biriminin bağımlı değişken değeri olan "Y"sini tahmin etmek için ilgili gözlem birimlerinden tablodaki diğer gözlem birimleriyle olan benzerlikleri hesaplanacaktır.

1. Komşu sayısı K belirlenir

2. Bilinmeyen nokta ile diğer tüm noktalar ile arasındaki uzaklıklar hesaplanır

3. Uzaklıkları sırala ve belirlenen k sayısına göre en yakın olan k gözlemini seç

4. Sınıflandırma ise en sık sınıf, regresyon ise ortalama değeri tahmin değeri olarak ver.

## **Modelleme**
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import neighbors
from sklearn.svm import SVR

#Uyarı mesajları ile karşılaşmamak için
from warnings import filterwarnings
filterwarnings('ignore')

"""### **KNN**"""

df = pd.read_csv("/content/Hitters.csv")
df = df.dropna()
dms = pd.get_dummies(df[['League','Division','NewLeague']])
y = df["Salary"]
X_ = df.drop(['Salary','League','Division','NewLeague'], axis = 1).astype('float64')
X = pd.concat([X_, dms[['League_N','Division_W','NewLeague_N']]], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

X_train.head()

"""### Model

"""

knn_model = KNeighborsRegressor().fit(X_train, y_train)

knn_model

knn_model.n_neighbors

knn_model.predict(X_test)[0:5]

y_pred = knn_model.predict(X_test)
#Test setindeki bağımsız değişkenleri kullan ve y bağımlı değişkeni tahmin et.

np.sqrt(mean_squared_error(y_test, y_pred))
#Test hatası

"""### Model Tuning"""

knn_model

RMSE = []

for k in range(10):
  k = k+1
  knn_model = KNeighborsRegressor(n_neighbors = k).fit(X_train, y_train)
  y_pred = knn_model.predict(X_test)
  rmse = np.sqrt(mean_squared_error(y_test, y_pred))
  RMSE.append(rmse)
  print("k =", k, "için RMSE değeri:", rmse)

# GridSearchCV

knn_params = {"n_neighbors": np.arange(1,30,1)}

knn = KNeighborsRegressor()

knn_cv_model = GridSearchCV(knn, knn_params, cv = 10).fit(X_train, y_train)

knn_cv_model.best_params_

#final model
knn_tuned = KNeighborsRegressor(n_neighbors = knn_cv_model.best_params_["n_neighbors"]).fit(X_train, y_train)

y_pred = knn_tuned.predict(X_test)

np.sqrt(mean_squared_error(y_test, y_pred))
