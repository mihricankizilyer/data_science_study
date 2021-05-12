# -*- coding: utf-8 -*-
"""3.3 Artificial neural networks

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VvhkP1BGg8jF_3oDj1N2ltBzhoOuP6ro

# **YAPAY SİNİR AĞLARI**

- İnsan beyninin bilgi işleme şeklini referans alan sınıflandırma ve regresyon problemleri için kullanılabilen kuvvetli makine öğrenmesi algoritmalarından birisidir.

- Amaç en küçük hata ile tahmin yapabilecek katsayılara erişmektir.

1. Örnek veri seti toplanır.
2. Ağın topolojik yapısına karar verilir.
3. Ağda bulunan ağırlıklara başlangıç değeri atanır.
4. Örnek veri seti ağa sunulur.
5. İleri hesaplama işlemleri yapılır.
6. Gerçek çıktılar ile tahmin edilen çıktılar karşılaştırılır. Öğrenmenin tamamlanması basamakları gerçekleştirilir.
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
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor

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

"""## Model ve Tahmin"""

# Bu bölümde farklı olarak değişkenlere standartlaştırma işlemleri yapılacak.

scaler = StandardScaler()

scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train) #X_train ölçeklendirilmiştir.

X_test_scaled = scaler.transform(X_test)

mlp_model = MLPRegressor().fit(X_train_scaled, y_train)
#mlp = çok katmanlı algılayıcı
mlp_model

y_pred = mlp_model.predict(X_test_scaled)
#Tahmin edilen değerler
np.sqrt(mean_squared_error(y_test,y_pred))

"""## Model Tuning"""

mlp_params = {"alpha":[0.1, 0.01, 0.02, 0.001, 0.001],
              "hidden_layer_sizes": [(10,2), (10,20), (100,100)]}
#0.001 öğrenmeyi yavaşlatır ama doğruluğu arttırır.
#(10,2) 2 tane gizli katman olduğunu gösterir.

mlp_cv_model = GridSearchCV(mlp_model, mlp_params, cv = 10, verbose = 2, n_jobs = -1).fit(X_train_scaled, y_train)

mlp_cv_model.best_params_

#final
mlp_tuned = MLPRegressor(alpha = 0.02, hidden_layer_sizes = (10,20)).fit(X_train_scaled, y_train)

y_pred = mlp_tuned.predict(X_test)

np.sqrt(mean_squared_error(y_test, y_pred))

