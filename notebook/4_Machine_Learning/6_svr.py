# -*- coding: utf-8 -*-
"""3.2 SVR

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_656Ljpa0x_uEMZGks_XqW3-WcSHyj4d

# **Support Vector Regression(SVR)**

Güçlü ve esnek modelleme tekniklerinden birisidir. Sınıflandırma ve regresyon için kullanılabilir. Robust(dayanıklı) bir regresyon modelleme tekniğidir.

- Amaç, bir marjin aralığında maksimum noktayı en küçük hata ile alabilecek şekilde doğru ya da eğriyi belirlemektir.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn import model_selection
import matplotlib.pyplot as plt
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

#Veri Seti

df = pd.read_csv("/content/Hitters.csv")

df = df.dropna()
#İçerisindeki eksik değerler atılır

dms = pd.get_dummies(df[['League','Division','NewLeague']])
#Veri seti içerisindeki kategorik değişkenleri dummy değişkenine çevirilir.
#Kategorik değişkenlerin sunduğu bilgiyi daha iyi alabilmek adına
#One hot encoding yapılmış oldu.

y= df["Salary"]
#Bağımlı değişken

X_ = df.drop(['Salary','League','Division','NewLeague'], axis = 1).astype('float64')

X = pd.concat([X_, dms[['League_N','Division_W','NewLeague_N']]], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.25, random_state = 42)

"""## **Model & Tahmin**"""

svr_model = SVR("linear").fit(X_train, y_train)
svr_model

svr_model.predict(X_train)[0:5]

svr_model.predict(X_test)[0:5]

svr_model.intercept_

svr_model.coef_

#test
y_pred = svr_model.predict(X_test)
np.sqrt(mean_squared_error(y_test,y_pred))

"""### **Model Tuning**"""

svr_model = SVR("linear")
svr_model

svr_params = {"C": [0,1, 0.5,1,3]}

svr_cv_model = GridSearchCV(svr_model, svr_params, cv = 5).fit(X_train, y_train)

svr_cv_model.best_params_

svr_cv_model = GridSearchCV(svr_model, svr_params, cv = 5, verbose = 2, n_jobs = -1).fit(X_train, y_train)

"""n_jobs = -1 olursa bilgisayar gücü maksimum işlemci ile çalışır.

> 5 katlı çapraz doğrulama yapılacak ve 20 tane fit etme işlemi gerçekleştirilecektir.
"""

svr_cv_model.best_params_

svr_tuned = SVR("linear", C = 0.5).fit(X_train, y_train)

y_pred = svr_tuned.predict(X_test)

np.sqrt(mean_squared_error(y_test, y_pred))

