# -*- coding: utf-8 -*-
"""Two_Sample_Independent_T_Test_(AB Test)
"""

# DATA TYPE I

import pandas as pd
import numpy as np
A = pd.DataFrame([30,20,22,14,33,24,25,36,28,27,29,21])
B = pd.DataFrame([22,14,23,24,25,26,27,28,29,30,21,22])

A_B = pd.concat([A,B], axis = 1)
A_B.columns = ["A","B"]

A_B.head()

# Data Type II

A = pd.DataFrame([30,20,22,14,33,24,25,36,28,27,29,21])
B = pd.DataFrame([22,14,23,24,25,26,27,28,29,30,21,22])

Group_A = np.arange(len(A))
Group_A = pd.DataFrame(Group_A)
Group_A[:] = "A"
A = pd.concat([A, Group_A], axis = 1)

Group_B = np.arange(len(B))
Group_B = pd.DataFrame(Group_B)
Group_B[:] = "B"
A = pd.concat([B, Group_B], axis = 1)

#Tüm veri
AB = pd.concat([A,B])
AB.columns = ["income","GROUP"]
print(AB.head())
print(AB.tail())

import seaborn as sns
sns.boxplot(x="GROUP", y="income", data=AB);

"""## Assumption Check"""

A_B.head()

AB.head()

#normality conjecture

from scipy.stats import shapiro

shapiro(A_B.A)
# When we write the variable in it, it will show whether it meets the normality or not.

shapiro(A_B.B)
# H0 is irrefutable therefore normality assumption is provided

# assumption of variance homogeneity

# H0: Variances are Homogeneous.
# H1: Variances Are Not Homogeneous.

from scipy import stats
stats.levene(A_B.A, A_B.B)

"""## Hypothesis Testing"""

from scipy import stats
stats.ttest_ind(A_B["A"],A_B["B"], equal_var = True)

test_statistics, pvalue = stats.ttest_ind(A_B["A"],A_B["B"], equal_var = True)
print('Test Statistics = %.4f, p-değeri = %.4f' % (test_statistics, pvalue))

"""## Nonparametric Independent Two-Sample Test"""

# If the results of both tests are negative, nonparametric test is used.

#Nonparametric two-sample testing
stats.mannwhitneyu(A_B["A"],A_B["B"])

test_statistics, pvalue = stats.mannwhitneyu(A_B["A"],A_B["B"])
print('Test Statistics = %.4f, p-değeri = %.4f' % (test_statistics, pvalue))

"""
The p value was greater than 0.05. Both parametric
In two sample tests with both nonparametric approach and
a meaningful result could not be reached.

"""
