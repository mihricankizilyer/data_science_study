# -*- coding: utf-8 -*-
"""3.5 Random Forest

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U44SHJ_ypPAfti9zsSG2GgZUjdY7WaLt

# **RANDOM FOREST**

Topluluk öğrenme yöntemlerinin birden fazla algoritmanın ya da birden fazla ağacın bir araya gelerek toplu bir şekilde öğrenmesi ve tahmin etmeye çalışmasıdır.

**Bagging**: Temeli bootstrap yöntemi ile oluşturulan birden fazla karar ağacının ürettiği tahminlerin bir araya getirilerek değerlendirilmesine dayanır.

**Boosrtap**: Yerine koyma seçme işlemi

- Çalışma prensibinin kilit noktası, boostrap rastgele örnekleme yöntemidir.

- Bootsrap rastgele örnekleme yöntemi gözlem birimlerinin içinden yerine koymak bir şekilde tekrar tekrar örnek çekmek demektir.

> **Baggin Yöntemi**

- Hata kareler ortalamsının karekökü değerini düşürür.

- Doğru sınıflandırma oranını arttırır.

- Varyans düşürür ve ezberlemeye karşı dayanıklıdır.
"""



"""**Random Forest**

- Bagging ile Random Subspace yöntemlerinin birleşimi ile oluşturulmuştur.

- Ağaçlar için gözlemler bootstrap rastgele örnek seçimi yöntemi ile değişkenler random subspace yöntemi ile seçilir.

- Karar ağacının her bir düğümünde en iyi dallara ayırıcı(bilgi kazancı) değişken tüm değişkenler arasından rastgele seçilen daha az sayıdaki değişken arasından seçilir.

- Ağaç oluşturmada veri setinin 2/3'ü kullanılır. Dışarıda kalan veri ağaçların performans değerlendirilmesi ve değişken önermenin belirlenmesi için kullanılır.

- Her düğüm noktasında rastgele değişken seçimi yapılır. (regresyonda p/3, sınıflamada karekök p)

## **Model and Prediction**
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
from sklearn.tree import DecisionTreeRegressor 
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("/Hitters.csv")
df = df.dropna()
dms = pd.get_dummies(df[['League','Division','NewLeague']])
y= df["Salary"]

X_ = df.drop(['Salary','League','Division','NewLeague'], axis = 1).astype('float64')
X = pd.concat([X_, dms[['League_N','Division_W','NewLeague_N']]], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.25, random_state = 42)

rf_model = RandomForestRegressor(random_state = 42).fit(X_train, y_train)
rf_model

"""**max_depth** = Her ağacın derinlik seviyesi ifade edilir.

**max_features** = Bölünmelerde göz önünde bulundurulacak değişkenleri ifade ediyor.

**max_leaf_nodes** = Maksimum yaprak nodlarını ifade ediyor.

**min_samples_split** = Bir node bölünmeden önce bu noddaki minimum gözlem sayısını ifade ediyor. Ör: Bu kadar gözlem varsa bölme işlem,ne devam et denir.

**min_samples_leaf** = Leaf noddaki min gözlem sayısını ifade ediyor.

**n_estimators** = Kullanılacak olan ağaç sayısını ifade ediyor.
"""

# Tahmin edilen değerlere erişme

y_pred = rf_model.predict(X_test)
np.sqrt(mean_squared_error(y_test, y_pred))
#İlkel hata bulundu

"""## **Model Tuning**"""

rf_model = RandomForestRegressor(random_state = 42).fit(X_train, y_train)
rf_model

"""Optimize edilebilecek birçok parametre mevcuttur. Bunların arasında en önemli iki tanesi:

1) Fit edilecek olan ağaç sayısıdır.(n_estimators)

2) Bölünme işlemlerinde göz önünde bulundurulacak olan değişken sayısıdır.

3) min_sample_split ve max_depth

**CART**: Dallanmalara en üst etki eden : min_sample_split
"""

rf_params = {"max_depth": [5,8,10],
             "max_features": [2,5,10],
             "n_estimators": [200,500,1000,2000],
             "min_sample_split":[2,10,80,100]}

rf_cv_model = GridSearchCV(rf_model, rf_params, cv = 10, n_jobs = -1, verbose = 2).fit(X_train, y_train)

rf_cv_model.best_params

random forest model tuning 5:10

rf_model = RandomForestRegressor(random_state = 42, 
                                 max_depth = 8,
                                 max_features = 2,
                                 min_samples_split = 2
                                 n_estimators = 200
                                 )
rf_tuned = rf_model.fit(X_train, y_train)

y_pred = rf_tuned.predict(X_test)
np.sqrt(mean_squared_error(y_test, y_pred))

## Değişken Önem Düzeyi

Importance = pd.DataFrame({'Importance':rf_tuned.feature_importances_*100},
                          index = X_train.coulmns)

Importance.sort_values(by = 'Importance',
                       axis = 0,
                       ascending = True).plot(kind = 'barh',
                                              color = 'r',)
                       
plt.xlabel("Variable Importance")
plt.gca().legend_ = None
