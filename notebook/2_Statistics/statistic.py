# -*- coding: utf-8 -*-
"""
# **HİPOTEZ TESTLERİ**

## **Hipotezler ve Türleri**

- H0: m=50   ve  H1: m!=50 

- H0: m<=50  ve  H1: m>50 

- H0: m>=50  ve  H1: m<50

## **Hata Tipleri**
## **p-value**

- p<0.05

p-value değeri 0.05'den küçükse ilgili H0 hipotezini reddedilir.

- Eğer ortaya çıkan p-value değeri çalışmanın başında belirlenmiş olan varsayılan kabul edilebilir hata miktarı olan alfa 0.05'den küçükse H0 reddedilir.

## **Hipotez Testi Adımları**

**Adım1:** Hipotezlerin kurulması ve yönlerinin belirlenmesi

**Adım2:** Anlamlılık düzeyinin ve tablo değerinin belirlenmesi(alfa)

**Adım3:** Test istatistiğinin belirlenmesi ve test istatisliğinin hesaplanması

**Adım4:**  Hesaplanan test istatistiği ile alfaya karşılık gelen tablo değerlerinin karşılaştırılması

Test İstatistiği(Zh) > Tablo Değeri (Zt) ise H0 Red

# **TEK ÖRNEKLEM T TESTİ VE TEK ÖRNEKLEM ORAN TESTİ**

## Tek Örneklem T Testi

Popülasyon ortalaması ile varsayımsal bir değer arasında istatistiksel olarak anlamlı bir farklılık olup olmadığını test etmek için kullanılan parametrik bir testtir.

- H0: m=50   ve  H1: m!=50 

- H0: m<=50  ve  H1: m>50 

- H0: m>=50  ve  H1: m<50

- t = (x - m) / (s / n^1/2)
- z = (x - m) / ( q / n^1/2)

1. Anakütle standart sapması biliniyorsa z istatistiği kullanılır.

2. Anakütle standart sapması bilinmiyorsa ve n > 30 ise z istatistiği kullanılır.

3. Anakütle standart sapması bilinmiyor ve  n < 30 ise t istatistiği kullanılır.

ÖR: Bir ilçenin yaş ortalaması hesaplanırken kullanılır.

Websitede insanların geçirdiği süreyi hesaplamak için kullanılır.

## İş Uygulaması: Ürün Satın Alma Adım Optimizasyonu

**Problem**: Sepete ürün ekleme işlemi sonrasında ödeneme ekranında 5 adım vardır ve bu adımların birisi sorgulanmaktadır.

**Detaylar**:  
- Her adımın 20'şer sn. olması hedefi var. 4.adım sorgulanıyor.

- Bu durumu test etmek için 100 örnek alınıyor.

- Örnek standart sapması 5 saniyedir. Örnek ortalaması ise 19 saniyedir.

**Adım1** : Hipotezlerin kurulması ve yönlerinin belirlenmesi

- H0: m = 20
> H0 hipotezi bilinmeyen anakütle parametresi m yani kişilerin 4.adımda geçirmiş oldukları süre ortalaması 20 demektir.

- H1: m!= 20
> Bilinmeyen anakitle ortalaması yani kişilerin tüm insanların 4.adımda geçirmiş oldukları süre 20 sn farklıdır.

**Adım2** : Anlamlılık düzeyinin ve tablo değerinin belirlenmesi

- a = 0.05    
- a/2 = 0.025

Ztablo tablo olasılık değeri: 0.5-0.025 = 0.475

Ztablo kritik değer = -/+1.96

**Adım3**: Test istatistiğinin belirlenmesi ve test istatistiğinin hesaplanması

z = (x - m) / ( q - n^1/2)

zhesap = (19-20) / (5/100^1/2) = -2

n = 100, std = 5, örnek ort = 19 sn

**Adım4**: Ztablo ve Zhesap karşılatırılması ZhZZt ya da -Zh<-Zt ise H0 Red 

- Zhesap = -2<Ztablo = 1.96 olduğu için H0 reddedilir.

**Adım5**: Yorum

4.adımda geçirilen sürenin 20 saniye oldupunu iddia eden H0 hipotezi reddedilmiştir. Buna göre kullanıcılar istatistiksel olarak yüzde 95 güvenilirlik ile 4. adımda 20 saniyeden farklı zaman geçirmektedir.

## Web Sitesinde Geçirilen Sürenin Testi

**Problem**: Web sitemizde geçirilen ortalama süre gerçekten 170 saniye mi?

**Detaylar**: 

- Yazılımlardan elde edilen web sitesinde geçirilen ort. süreler var.

- Bu veriler incelendiğinde bir yönetici ya da çalışanımız bu değerlerin böyle olmadığında yönelik düşünceler taşıyor ve bu durumu test etmek istiyorlar.

- H0: m = 170
- H1: m!=170
"""

import numpy as np

olcumler = np.array([168,169,167,166,171,172,173,166,165,164,174,175])

olcumler[0:10]

#Betimsel İstatistikleri
import scipy.stats as stats

stats.describe(olcumler)

#varsayımlar
#normallik varsayımı

"""## Varsayım Testi

Normallik varsayımı nasıl gerçekleştirilebilir?

1.Grafik yöntemlerle(Histogram, QQPlot)

2.Bazı Testler ile
"""

#histogram
import pandas as pd
pd.DataFrame(olcumler).plot.hist();

#qqplot
import pylab
stats.probplot(olcumler, dist = "norm", plot = pylab);

"""- **Üstteki**: Örnek dağılımı gösterir. Örnek dağılımı elimizdeki ölçümlerdir. 

- **Alttaki**: Teorik dağılımı ifade eder. Teorik dağılım ilgilenmiş olduğumuz normal dağılımdır. 
"""

#Shapiro-Wils Testi

"""**H0**: Örnek dağılımı ile teorik normal dağılımı arasında ist. olarak anlamlı bir farklılık yoktur.

**H1**: ...fark vardır.
"""

from scipy.stats import shapiro

shapiro(olcumler)
#(test istatistiği, p-value)

"""- p-value değerine bakarak değerlendirmelerde bulunabiliyoruz.

- **p-value < 0.05** -> **H0 reddedilir**

H0 reddilemezse örnek dağılım ile teorik normal dağılım arasında istatistiksel olarak anlamlı bir farklılık yoktur. T örneklem testi uygulanabilir.

## Tek Örneklem T Testi Uygulaması
"""

#Hipotez testinin yapılması

stats.ttest_1samp(olcumler, popmean=170)

"""Sonuç Yorum: Elde etmiş olduğumuz p-value değeri çalışmanın başında kabul edilebilir hata mikarı olarak kabul ettiğimiz alfa, yani 0.05 değerinden küçük olduğundan dolayı H0 hipotezi reddedilir.

- H0: Web sitemizde geçirilen ortalama süre 170'tir.

- H1: ... değildir.

Test sonuçları incelendiğinde p-value değeri çalışmanın başında kabul ettiğimiz alfa 0.05 değerinden küçük olduğundan dolayı H0 hipotezi reddedilir. Bu şu anlama gelir web sitemizde geçirilen ortalama süre 170 değildir.

## Nanparametrik Tek Örneklem Testi
"""

from statsmodels.stats.descriptivestats import sign_test
#varsayım sağlanmadığında bu test yapılır.

sign_test(olcumler, 170)
#(test istatistiği, p-value)

"""H0 reddedilemez durumu ortaya çıkar ama bizim değşkenlerimiz doğrusal olduğu için bu durumla ilgilenmiyoruz.

## Tek Örneklem Oran Testi

Oransal bir ifade test edilerek istendildiğinde kullanılır.

p şapka : Örnek üzerinden elde edilen değerdir.

p0 : Sınamak üzere odaklanılan değerdir.

n>30

## İş Uygulaması: Dönüşüm Oran Testi

**Problem:** Bir yazılım ile bir mecrada reklma verilmiş ve bu reklma ilişkin yazılım taradından 0.125 dönüşüm oranu elde edildiği ifade edilmiştir. Fakat b durum kontorl edilmek isteniyor. Çünkü bu yüksek bir oran ve gelirler incelendiğinde örtüşmüyor.

**Detaylar:** 
- 500 kişi dış mecrada reklmalara tıklamış, 40 tanesi sitemize gelip alışveriş yapmış.

- Örnek üzerinden elde edilen dönüşüm oranı: 40/500 = 0.08

- H0: p = 0.125
- H1: p!= 0.125
"""

from statsmodels.stats.proportion import proportions_ztest

#Fonksiyonların bizden beklediği argümanların isimleri
count = 40
#başarı sayısı

nobs = 500 
#gözlem sayısı

value = 0.125
#

proportions_ztest(count,nobs, value)

"""# **BAĞIMSIZ İKİ ÖRNEKLEM T TESTİ(AB Testi)**

p-value değer kabul edilebilir alfa değerinden daha küçük olduğu için reddedilir.

- Normallik

- Varyans Homojenliği

## İş Uygulaması: ML Modelinin Başarı Testi(AB Testi)

**Problem**: Bir ML projesine yatırım yapılmış. Ürettiği tahminler neticesinde oluşan gelir ile eski sistemin ürettiği gelirler karşılaştırılıp anlamlı farklılık olup olmadığı test edilmek isteniyor.

**Detaylar**: 
- Model geliştirilmiş ve web sitesine entegre edilmiş.

- Site kullanıcıların belirli bir kurala göre ikiye bölünmüş olsun.

- A grubu eski B grubu yeni sistem

- Gelir anlamında anlamlı bir iş yapılıp yapılmadığı test edilmek isteniyor.
"""

#VERİ TİPİ I

import pandas as pd
import numpy as np
A = pd.DataFrame([30,20,22,14,33,24,25,36,28,27,29,21])
B = pd.DataFrame([22,14,23,24,25,26,27,28,29,30,21,22])

A_B = pd.concat([A,B], axis = 1)
A_B.columns = ["A","B"]

A_B.head()

# Veri Tipi II

A = pd.DataFrame([30,20,22,14,33,24,25,36,28,27,29,21])
B = pd.DataFrame([22,14,23,24,25,26,27,28,29,30,21,22])

Grup_A = np.arange(len(A))
Grup_A = pd.DataFrame(Grup_A)
Grup_A[:] = "A"
A = pd.concat([A, Grup_A], axis = 1)

Grup_B = np.arange(len(B))
Grup_B = pd.DataFrame(Grup_B)
Grup_B[:] = "B"
A = pd.concat([B, Grup_B], axis = 1)

#Tüm veri
AB = pd.concat([A,B])
AB.columns = ["gelir","GRUP"]
print(AB.head())
print(AB.tail())

import seaborn as sns
sns.boxplot(x="GRUP", y="gelir", data=AB);

"""## Bağımsız İki Örneklem T Testi: Varsayım Kontrolü"""

A_B.head()

AB.head()

#normallik varsayımı

from scipy.stats import shapiro

shapiro(A_B.A)
#İçinde değişkeni yazdığımızda normalliği sağlayıp sağlamadığını vermiş olacak.

shapiro(A_B.B)
#H0 reddedilemez bu sebeple normallik varsayımı sağlanır.

#varyans homojenliği varsayımı

# H0: Varyanslar Homojendir.
# H1: Varyanslar Homojen değildir.

from scipy import stats
stats.levene(A_B.A, A_B.B)

"""## Bağımsız İki Örneklem T Testi Uygulanması: Hipotez Testi"""

from scipy import stats
stats.ttest_ind(A_B["A"],A_B["B"], equal_var = True)

test_istatistiği, pvalue = stats.ttest_ind(A_B["A"],A_B["B"], equal_var = True)
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistiği, pvalue))

"""## Nonparametrik Bağımsız İki Örneklem Testi"""

#Eğer iki testin sonucu da negatif olursa nonparametrik test kullanılır

#Nonparametrik iki örneklem test
stats.mannwhitneyu(A_B["A"],A_B["B"])

test_istatistiği, pvalue = stats.mannwhitneyu(A_B["A"],A_B["B"])
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistiği, pvalue))

"""p değeri 0.05'den büyük çıkmıştır. Hem parametrik 
yaklaşımla hem nonparametrik yaklaşımla iki örneklem testinde
anlamlı bir sonuca ulaşılamamıştır.

# **BAĞIMLI İKİ ÖRNEKLEM T TESTİ**

Bağımlı iki grup ortalaması arasında karşılaştırma yapılmak istenildiğinde kullanılır.

- Normallik 
- Varyans Homojenliği

## İş Uygulaması: Şirket içi Eğitimin Performans Etkisi Ölçümü

**Problem**: Belirli uğraşlar sonucunda alınan bir eğitimin katma değer sağlayıp sağlamadığı ölçülmek isteniyor.

**Detaylar**: 
- Bir departman bir konuda eğitim talep ediyor.
- Gerekli/gereksiz değerlendirmeler neticesinde eğitim alınıyor.
- Eğitimden önce ve sonra olacak şekilde gerekli ölçümler yapılıyor.
- Eğitim sonrasında eğitimin sağladığı katma değer test edilmek isteniyor.

### Bağımlı İki Örneklem T Testi
"""

oncesi = pd.DataFrame([123,119,119,116,123,123,121,120,117,118,121,121,123,119])
sonrasi = pd.DataFrame([118,127,112,132,129,132,128,130,128,138,140,130,134,134])

oncesi [0:5]

sonrasi[0:5]

#BIRINCI VERI SETI
AYRIK = pd.concat([oncesi,sonrasi], axis = 1)
AYRIK.columns = ["ONCESI","SONRASI"]
print(" 'AYRIK' Veri Seti: \n\n", AYRIK.head(), "\n\n")

#IKINCI VERI SETI
#ONCE FLAG/TAG'INI OLUSTURMA
GRUP_ONCESI = np.arange(len(oncesi))
GRUP_ONCESI = pd.DataFrame(GRUP_ONCESI)
GRUP_ONCESI[:] = "ONCESI"

#FLAG VE ONCESİ DEGERLERİNİ BİR ARAYA GETIRME
A = pd.concat([oncesi, GRUP_ONCESI], axis =1)

#SONRASI FLAG/TAG'INI OLUSTURMA
GRUP_SONRASI = np.arange(len(sonrasi))
GRUP_SONRASI = pd.DataFrame(GRUP_SONRASI)
GRUP_SONRASI[:] = "SONRASI"

#FLAG VE SONRASI DEGERLERINI BIR ARAYA GETIRME
B = pd.concat([sonrasi, GRUP_SONRASI], axis = 1)

# TUM VERIYI BIR ARAYA GETIRME
BIRLIKTE = pd.concat([A,B])
BIRLIKTE

#ISIMLENDIRME
BIRLIKTE.columns = ["PERFORMANS","ONCESI_SONRASI"]
print(" 'BIRLIKTE' Veri Seti: \n\n", BIRLIKTE.head(), "\n")

import seaborn as sns
sns.boxplot(x = "ONCESI_SONRASI", y = "PERFORMANS", data = BIRLIKTE);

"""## Varsayım Kontrolleri"""

from scipy.stats import shapiro

shapiro(AYRIK.SONRASI)

"""Çalışmanın başında kabul edilebilir alfa değeri(0.05)'den küçük olmadığından dolayı H0 reddedilmez."""

import scipy.stats as stats
stats.levene(AYRIK.ONCESI,AYRIK.SONRASI)

"""p-value 0.05'den küçük olduğu için reddedilir. İkinci varsayım olan varyansların homojenliği varsayımı sağlanmamaktadır.

Bu durumda ne yapılır ?

1) Veri seti üzerinde aykırılıklar varsa düzenleme işlemleri yapılabilir.

2) Bağımlı iki örneklem T testinde varyans homojenliği incelendiğinde bu varsayımın sağlanmaması durumunda bu bir miktar göz ardı edilebilen bir durumdur.

## Hipotez Testi
"""

stats.ttest_rel(AYRIK.ONCESI, AYRIK.SONRASI)

test_istatistiği, pvalue = stats.ttest_rel(AYRIK["ONCESI"],AYRIK["SONRASI"])
print('Test İstatistiği = %.4f, p-değeri = %.4f'% (test_istatistiği, pvalue) )

"""p-value değeri 0.05'den küçük olduğundan dolayı H0 hipotezi reddedilir. Yani eğitim işe yaramıştır.

> Çalışanların performansları göz önünde bulundurulduğunda, öncesi ve sonrası performansları incelendiğinde istatistiki olarak anlamlı bir farklılık yüzde 5 hata payı, yüzde 95 güvenilirlik ile ortaya konmuştur. Eğitim başarılıdır.

## Nonparametrik Bağımlı İki Örneklem Testi
"""

stats.wilcoxon(AYRIK.ONCESI, AYRIK.SONRASI)

test_istatistiği, pvalue = stats.wilcoxon(AYRIK.ONCESI, AYRIK.SONRASI)
print('Test İstatistiği = %.4f, p-değeri = %.4f'% (test_istatistiği, pvalue) )

"""Nonparametrik bağımlı iki örneklem T testi sonucuna göre iki grup arasında istatistiki olarak anlamlı bir farklılık gözlenmektedir. Verilen eğitim performansları olumlu bir şekilde etkilemiştir.

# **İKİ ÖRNEKLEM ORAN TESTİ**
"""

#N1>30 VE N2>30 olduğunda Z'yi kullanarak oran testi yapılır.

## İş Uygulaması: Kullanıcı Arayüzü Deneyi(AB Testi)

- H0: P1 <= P2
- H1: P1 > P2
"""

from statsmodels.stats.proportion import proportions_ztest

import numpy as np
basari_sayisi = np.array([300,250])
gozlem_sayilari = np.array([1000,1100])

proportions_ztest(count = basari_sayisi, nobs = gozlem_sayilari)

"""p-value değeri 0.05'den oldukça küçük olduğundan dolayı H0 hipotezi reddedilir.

# **VARYANS ANALİZİ**

- İki ya da daha fazla grup ortalaması arasında istatistiksel olarak anlamlı farklılık olup olmadığını öğrenilmek istenildiğinde kullanılır.

H0: M1 = M2 = M3

H1: Eşit değillerdir(en az birisi farklıdır)

**Varsayımlar**

- Gözlemlerin birbirinden bağımısız olması(grupların)

- Normal dağılım

- Varyans homojenliği

## İş Uygulaması: Anasayfa İçerik Stratejisi Belirlemek

Problem:

- Anasayfada geçirilen süre arttırılmak isteniyor.

Detaylar:
- Bir web sitesi için başarı kriterleri: ortalama ziyaret süresi, hemen çıkış oranı vb.
- Uzun zaman geçiren kullanıcıların reklamlara daha fazla tıkladığı ve markaya olan bağlılıkları arttığı biliniyor. 
- Buna yönelik olarak benzer haberler farklı resimler ya da farklı formatlarda hazırlanarak oluşturulan test gruplarına gösteriliyor.

> A: Doğal Şekilde

> B: Yönlendirici

> C: İlgi Çekici
"""

A = pd.DataFrame([28,33,30,29,28,29,31,30,32,28,33,25,29,27,31,31,30,31,34,30,32,31,33])
B = pd.DataFrame([31,32,30,30,33,32,34,27,36,30,31,30,38,29,30,34,34,31,35,35,33,30,28])
C = pd.DataFrame([40,33,38,41,42,43,38,35,39,39,36,34,35,40,38,36,39,36,33,35,38,35,40])

dfs = [A,B,C]

ABC = pd.concat(dfs, axis = 1)
ABC.columns = ["GRUP_A","GRUP_B","GRUP_C"]
ABC.head()

"""## Varsayım Analizi & Varsayım Kontrolü"""

# Varsayım Kontrolü
from scipy.stats import shapiro

shapiro(ABC["GRUP_A"])

shapiro(ABC["GRUP_B"])

shapiro(ABC["GRUP_C"])

"""**Normallik Varsayımı Testi**: H0: örnek dağılımı ile teorik normal dağılım arasında istatistiki olarak anlamlı bir farklılık yoktur.

Her testin p-value değerleri incelendiğinde 0.05'den küçük olmadığından dolayı H0 hipotezi reddedemiyoruz. Üç grup içinde normallik varsayımı sağlanmaktadır.
"""

stats.levene(ABC["GRUP_A"], ABC["GRUP_B"], ABC["GRUP_C"])

"""**Hipotez:** Varyanslar homojendir. p-value değeri incelendiğinde varyans homojendir diyen H0 hipotezinin reddedilemediği görülmektedir. Yani varyanslar homojendir varsayım sağlanmıştır.

## Hipotez Testi Uygulaması
"""

from scipy.stats import f_oneway

f_oneway(ABC["GRUP_A"], ABC["GRUP_B"], ABC["GRUP_C"])

print('{:.5f}'.format(f_oneway(ABC["GRUP_A"], ABC["GRUP_B"], ABC["GRUP_C"])[1]))

"""H0: Bir medya şirketi olarak oluşturmuş olduğum haber portalında 3 farklı haber tarzı deniyorum. Bu haber tarzlarından birisi A, birisi B, diğeri ise C'dir.

- Bunlara ilişkin bir test gerçekleştirdim ve neticesinde 3 grup elde ettim. 
H0: Üç gruba ilişkin websitesinde geçirilen süre ortalamaları arasında istatistiki olarak anlamlı bir farklılık yoktur. 

- Fakat p value değeri incelendiğinde çalışmanın başında kabul edilebilir alfaya göre  daha düşüktür. Bu sebeple H0 hipotezi reddedilir. Gruplar arasında istatistiki olarak anlamlı bir farklılık vardır.
"""

ABC.describe().T

"""GRUP_C istatistiki olaak diğer gruplara göre daha anlamlı katkılar sağlayabileceği gözlenmektedir.

## Nonparametrik Hipotez Testi
"""

from scipy.stats import kruskal
#diğer varsayımlar sağlanmadığında kullanılır

kruskal(ABC["GRUP_A"], ABC["GRUP_B"], ABC["GRUP_C"])

"""H0 hipotezi reddedilir çünkü p-value değeri 0.05'den küçüktür.

# **KORELASYON ANALİZİ**

Değişkenler arasındaki ilişki, bu ilişkinin yönü ve şiddeti ile ilgili bilgiler sağlayan istatistiksel bir yöntemdir.

Korelasyon anlamlılığının testi:
- H0: p=0
- H1: p!=0

**Varsayımlar**:
- İki değişken içinde normallik varsayımı
- Varsayım sağlanıyorsa Pearson Korelasyon Katsayısı
- Varsayım sağlanmıyorsa Spearman Korelasyon Katsayısı

## İş Uygulaması: Bahşiş ile Ödenen Hesap Arasındaki İlişkinin İncelenmesi

> Bahşiş ile ödenen hesap arasında korelasyon var mı?
"""

import seaborn as sns
tips = sns.load_dataset('tips')
df = tips.copy()
df.head()

df["total_bill"] = df["total_bill"] - df["tip"]
#sadece yemeğin masrafı kalmış olur.

df.head()

df.plot.scatter("tip","total_bill");

"""## Varsayım Kontrolü"""

from scipy.stats import shapiro

test_istatistigi, pvalue = shapiro(df["tip"])
print('Test istatistiği = %.4f, p-value = %.4f' % (test_istatistiği, pvalue))

test_istatistigi, pvalue = shapiro(df["total_bill"])
print('Test istatistiği = %.4f, p-value = %.4f' % (test_istatistiği, pvalue))

"""İki değişken içinde normallik varsayımının sağlanmadığını gözlemiyoruz. p-value değerleri 0.05'den küçük çıkmıştır. Yani H0 reddedilmiştir. Normallik varsayımı için H0 hipotezi örnek dağılımı ile teorik normal dağılım arasında istatistiki olarak anlamlı bir farklılık yoktur. p-value değeri H0' reddeddiğinden dolayı örnek dağılımı ile teorik normal dağılım arasında istatistiki olarak anlamlı bir farklılık vardır demiş oluyoruz. Fark var dediğimizde dağılımlar birbirine benzemiyor demiş oluruz. Örnek dağılım ile teorik normal dağılım birbirine benzemiyor demiş oluruz. Bu sebeple normallik varsayımı sağlanmamaktadır.

## Hipotez Testi

**Korelasyon Katsayısı**
"""

df["tip"].corr(df["total_bill"])

df["tip"].corr(df["total_bill"], method = "spearman")
#spearman korelasyon katsayısı

"""Corr fonksiyonu ön tanımlı olara pearson katsayısını bize verir.Person korelasyon katsayısı ancak değişkenler için normallik katsayısı sağlandığında hesaplanabilir.

Yorum: Değişkenlerin arasında pozitif yönlü bir ilişki vardır. İlişkinin yönü orta şiddetlidir. 0.60 civarındadır.

**Korelasyonun Anlamlılığının Testi**
"""

from scipy.stats.stats import pearsonr

test_istatistigi, pvalue = pearsonr(df["tip"], df["total_bill"])
print('Korelasyon Katsayısı = %.4f, p-value = %.4f' % (test_istatistiği, pvalue))

"""Yorum: Değişkenler arasında anlamlı bir ilişki yoktur diyen H0 hipotezini reddeder. Yani değişkenler arasında anlamlı bir ilişki korelasyon vardır denir.

## Nanparametrik Korelasyon Hipotez Testi
"""

stats.spearmanr(df["tip"],df["total_bill"])

"""Yorum: Test sonucu incelendiğinde p-value değeri olduca küçük çıkmaktadır ve değişkenler arasında ilişki yoktur diyen H0 hipotezi reddedilir. Yani değişkenlerin arasında ilişki vardır bu orta şiddetli bir ilişkidir. Bu ilşiki anlamlıdır. """

test_istatistigi, pvalue = stats.spearmanr(df["tip"], df["total_bill"])
print('Korelasyon Katsayısı = %.4f, p-value = %.4f' % (test_istatistiği, pvalue))

"""İki değişken arasında ilişki olup olmadığını, ilişkinin anlamlı olup olmadığını,bu ilişkinin yönünü ve şiddeti merak edilmektedir. Buna yönelik olarak iki değişkenin arasındaki ilişkiyi korelasyon testleri ile test etmeye karar verildi. Fakat öncesinde varsayımları incelendi varsayım sağlanıyorsa person , varsayım sağlanmıyorsa pearman korelasyon katsayısını kullanacağımızı ifade ettik. buna yönelik olarak ilgili korelasyon katsayını elde ettiğimizde bu korelasyon katsayısına ilişkin hipotez testini gerçekleştirdiğimizde H0 değişkenlerin arasında anlamlı bir korelasyon yoktur hipotezi pvalue  değeri çalışmanın başında kabul ettiğimiz kabul edilebilir hata miktarı olan alfa oldukça küçük olduğundan dolayı reddedilir. Yani değişkenlerin arasında istatistiki olarak anlamlı bir vardır. Bu ilişki pozitif yönlüdür ve orta şiddete sahiptir."""

test_istatistigi, pvalue = stats.kendalltau(df["tip"], df["total_bill"])
print('Korelasyon Katsayısı = %.4f, p-value = %.4f' % (test_istatistiği, pvalue))

