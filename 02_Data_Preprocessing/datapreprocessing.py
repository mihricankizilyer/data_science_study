
"""

# **VERİ ÖN İŞLEME**

- Makine öğrenmesi modelinin amacı genellenebilir yapılar ortaya koymaktır.

- Belirli olaylar gözlendiğinde belirli tahmin sonuçları vermektedir.

> **Veri Temizleme(data cleaning/cleasing)**
- Gürültülü Veri
- Eksik Veri Analizi
- Aykırı Gözlem Analizi

**Gürültülü Veri**: Erkek bireyin veri üzerinde hamile olması. Bebek biberonu fiyatının 1 milyon lira olması.

> **Veri Standardizayonu**
- 0-1 dönüşümü
- z-skoruna dönüştürme
- logaritmik dönüşüm

> **Veri İndirgeme**
- Gözlem sayısının azaltılması
- Değişken sayısının azaltılması

> **Değişken Dönüşümleri**
- Sürekli değişkenlerde dönüşümler
- Kategorik değişkenlerde dönüşümler

# **AYKIRI GÖZLEM ANALİZİ**

Veride genel eğilimin oldukça dışına çıkan ya da diğer gözlemlerden oldukça farklı olan gözlemere aykırı gözlem denir.

- Aykırı Değer Nedir?
> Aykırılığı ifade eden nümerik değere denir.

- Aykırı Gözlem Nedir?
> Aykırı değeri barındıran gözlem birimine aykırı gözlem denir.

Genellenebilirlik kaygısı ile oluşturulan kural setlerini ya da fonksiyonları yanıltır. Yanlılığa sebep olur.

## Kime Göre Neye Göre Aykırı

Veride genel eğilimin oldukça dışına çıkan gözlemler.

Peki veri setinin eğilimin dışına çıkmayı nasıl tanımlarız?

- **1. Sektör Bilgisi**

Örneğin bir ev fiyat tahmin modelinde 1000 metrekarelik evleri modellemeye almamak.

> Eğer kurulan modelin bir genelleme kaygısı varsa: zaten çok seyrek olan senaryolar ve genele uymayan yapılar çalışmanın dışında bırakılmalıdır.

- **2. Standart Sapma Yaklaşımı**

> Bir değişkenin ortalamasının üzerine aynı değişkenin standart sapması hesaplanarak eklenir.
1, 2 ya da 3 standart sapma değeri ortalama üzerine eklenerek ortaya çıkan bu değer eşik değer
olarak düşünülür ve bu değerden yukarı ya da aşağıda olan değerler aykırı değer olaak tanımlanır.

EŞİK DEĞER = ORTALAMA + 1*STANDART SAPMA

EŞİK DEĞER = ORTALAMA + 2*STANDART SAPMA

EŞİK DEĞER = ORTALAMA + 3*STANDART SAPMA

- **3. Z-Skoru Yaklaşımı**

>Standart sapma yöntemine benzer şekilde çalışır. Değişken standart normal dağılıma uyarlar, yani standartlaştırılır.
Sonrasında dağılımın sağından ve solundan -+2.5 değerine göre bir eşik değer konulur ve bu değerin üzerinde ya da altında
olan değerler aykırı değer olarak işaretlenir.

- **4. Boxplot(IQR) Yöntemi**

> En sık kullanılan yöntemlerden birisidir. Değişkenin değerleri küçükten büyüğe sıralanır. Çeyrekliklerine yani Q1Q3 değerlerine karşılık değerler
üzerinden bir eşik değer hesaplanır ve bu eşik değere göre aykırı değer tanımı yapılır.

IQR = 1.5 * (Q3-Q1)

ALT EŞİK DEĞER = Q1 - IQR

ÜST EŞİK DEĞER = Q3 - IQR

## Aykırı Değerleri Yakalamak
"""

import seaborn as sns
df = sns.load_dataset('diamonds')

#sadece içerisindeki sayısal değişkene erişir
df = df.select_dtypes(include = ['float64','int64'])

#veri seti içeriisndeki eksik değerleri siler
df = df.dropna()

df.head()

df_table = df["table"]

df_table.head()

sns.boxplot(x = df_table);

#kutu grafiği
#gözlemlenen değerler aykırıdır

Q1 = df_table.quantile(0.25)
Q3 = df_table.quantile(0.75)
IQR = Q3-Q1

Q1

Q3

IQR

alt_sinir = Q1 - 1.5*IQR
üst_sinir = Q3 + 1.5*IQR

alt_sinir

üst_sinir

(df_table < alt_sinir) | (df_table > üst_sinir)
#ayrık gözlemler = True

aykiri_tf = (df_table < alt_sinir)
aykiri_tf.head()

df_table[aykiri_tf]
#tüm aykırı değerler

df_table[aykiri_tf].index
#aykırı gözlemlerin indexleri

"""## Aykırı Değer Problemi Çözmek"""

df_table[aykiri_tf]

"""### Silme"""

import pandas as pd

type(df_table)

df_table = pd.DataFrame(df_table)

df_table.shape

t_df = df_table[~((df_table < alt_sinir) | (df_table > üst_sinir)).any(axis = 1)] 
#aykırı olmayanları seç
#~: koşulu sağlamayanları al demek
# any(axis = 1) >> sütun bazında işlem yapıldığını söyler

t_df.shape

"""### Ortalama ile Doldurma"""

import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64','int64'])
df = df.dropna()
df.head()

df_table = df["table"]

aykiri_tf.head()

df_table[aykiri_tf] 
#alt sınırdaki aykırı değerler

df_table.mean()

df_table[aykiri_tf] = df_table.mean()
#yakalanan tüm değerlerin yerine ortalamayı atar.

df_table[aykiri_tf]

"""### Baskılama Yöntemi"""

import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64','int64'])
df = df.dropna()
df.head()

df_table = df["table"]

alt_sinir

df_table[aykiri_tf] = alt_sinir

df_table[aykiri_tf]

"""## Çok Değişkenli Aykırı Gözlem

**LOCAL OUTLIER FACTOR**

Gözlemleri bulundukları konumda yoğunluk tabanlı skorlayarak buna göre aykırı değer olabilecek tanımlayabilmemize imkan sağlar.

Bir noktanın local yoğunluğu bu noktanın komşuları ile karşılaştırılıyor. 
Eğer bir nokta komşularının yoğunluğundan anlamlı bir şekilde düşükse bu nokta komşularından daha seyrek bir noktada bulunuyordur.
"""

import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64','int64'])
df = df.dropna()
df.head()

import numpy as np
from sklearn.neighbors import LocalOutlierFactor

clf = LocalOutlierFactor(n_neighbors = 20, contamination = 0.1)
#contamination = yoğunluk

clf.fit_predict(df)

df_scores = clf.negative_outlier_factor_

df_scores[0:10]

np.sort(df_scores)[0:20]
#sıralama yapılmıştır.

esik_deger = np.sort(df_scores)[13]

"""Silme Yöntemi"""

aykiri_tf = df_scores > esik_deger

aykiri_tf

yeni_df = df[df_scores >esik_deger]

yeni_df
#aykırı olmayan değerler

df[df_scores < esik_deger]
#aykırı gözlemler

"""Baskılama Yöntemi"""

df[df_scores == esik_deger]

baski_deger = df[df_scores == esik_deger]

aykirilar = df[~aykiri_tf]

res = aykirilar.to_records(index = False)

res[:] = baski_deger.to_records(index = False)

res

df[~aykiri_tf]

import pandas as pd
df[~aykiri_tf] = pd.DataFrame(res, index = df[~aykiri_tf].index)

df[~aykiri_tf]

"""# **EKSİK GÖZLEM ANALİZİ**

1. Veri setindeki eksikliğin yapısal bir eksiklik olup olmadığı bilinmesi gerekir.

2. NA her zaman eksiklik anlamına gelmez

3. Bilgi kaybı

- **Tümüyle Raslantısal Kayıp**: Diğer değişkenlerden ya da yapısal bir porblemden kaynaklanmayan tamamen rastgele oluşan gözlemler.

- **Rastlantısal Kayıp**: Diğer değişkenlere bağlı olarak oluşabilen eksiklik türü.

- **Rastlantısal Olmayan Kayıp**: Göz ardı edilemeyecek olan ve yapısal problemler ile ortaya çıkan eksiklik türü.

Eksik Veri Rassalılığının Testi

- Görsel Teknikler
- Bağımsız İki Örneklem T Testi
- Korelasyon Testi
- Little'nin MCAR Testi

Eksik Veri Problemi Nasıl Giderilir ? 

> Silme Yöntemleri
- Gözlem ya da değişken silem yöntemi
- Liste bazında silme yöntemi(Listwise Method)
- Çiftler bazında silme yöntemi(Pairwise Method)

> Değer Atama Yöntemleri
- Ortanca, ortalama,medyan
- En benzer birime atama (hot deck)
- Dış kaynaklı atama

> Tahmine Dayalı Yöntemler
- Makine Öğrenmesi
- EM
- Çoklu Atama Yöntemi

## Eksik Veri Hızlı Çözüm
"""

import numpy as np
import pandas as pd
V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])
df = pd.DataFrame(
    {"V1": V1,
    "V2": V2,
    "V3": V3}
)
df

df.isnull().sum()
#değişkendeki eksik değerler
#her bir değişkendeki eksik değer sayısı

df.notnull().sum()
#tam olan gözlemlerin sayıları

df.isnull().sum().sum()
# veri setindeki toplam eksik değer sayısı

df.isnull()

df[df.isnull().any(axis=1)]
#any(axis=1) = en az bir tane eksik değer varsa seç

df[df.notnull().all(axis=1)]
#all(axis=1) 
#tüm değerleri tam olan gözlemler

df[df["V1"].notnull() & df["V2"].notnull() & df["V3"].notnull()]

# Eksik değerlerin silinmesi

df.dropna()
#df.dropna(inplace = True) #kalıcı olarak silme işlemi
#veri setindeki tüm eskiklikler silinir

df

#basit değer atama

df["V1"]

df["V1"].mean()

df["V1"].fillna(df["V1"].mean())
#fillna = doldur
#kendi ortalaması ile doldur

df["V2"].fillna(0)

import numpy as np
import pandas as pd
V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])
df = pd.DataFrame(
    {"V1": V1,
    "V2": V2,
    "V3": V3}
)
df

df.apply(lambda x: x.fillna(x.mean(), axis = 0))

"""## Eksik Veri Yapısının Görselleştirilmesi"""

!pip install missingno

import missingno as msno

msno.bar(df);

# v1 = 7 tam gözlem
# v2 = 6 tam gözlem
# v3 = 7 tam gözlem
# sağ = elimizideki gözlem sayısı
# sol = eksikliklerin yüzdesi
