"""
## Business Practice: Product Purchase Step Optimization

Problem : After adding a product to the cart, there are 5 steps on the payment screen and one of these steps is queried.
Detail:
- Each step is 20 seconds. It has a goal to be. Step 4 is being questioned.
- 100 samples are taken to test this situation.
- Sample standard deviation is 5 seconds. The sample average is 19 seconds.

Step1 : Establishing hypotheses and determining their directions
- H0: m = 20
> H0 hypothesis means the unknown population parameter m, that is, the average time people spent in step 4 is 20.
- H1: m! = 20
> Average with unknown population, ie the time that all people spent in step 4 is 20 seconds different.

Step2 : Determining the significance level and table value
a = 0.05
a / 2 = 0.025
Ztable table probability value: 0.5-0.025 = 0.475
Ztable critical value = - / + 1.96

Step3 : Determination of test statistics and calculation of test statistics
z = (x - m) / (q - n ^ 1/2)
zaccount = (19-20) / (5/100 ^ 1/2) = -2
n = 100, std = 5, sample mean = 19 sec

Step4 : Ztablo and Zhaccount comparison H0 Red if Zh> Zt or -Zh <-Zt
H0 is rejected because Ztable = -2 <Ztable = 1.96.

Step5:
Comment: The H0 hypothesis claiming that the time spent in step 4 was 20 seconds was rejected. Accordingly, users spend time different than 20 seconds in step 4 with a statistical reliability of 95 percent.

## Testing the Time Spent on the Website
Problem : Is the average time spent on our website really 170 seconds?

Detail:
Average passed on the website obtained from the software. there are periods.
When these data are examined, a manager or employee has thoughts about the absence of these values and they want to test this situation.
H0: m = 170
H1: m! = 170
"""

import numpy as np

measurements = np.array([168,169,167,166,171,172,173,166,165,164,174,175])

measurements[0:10]

#Descriptive Statistics
import scipy.stats as stats

stats.describe(measurements)

# assumptions
#normality conjecture

"""
## Assumption Testing
How can the assumption of normality be realized?
1. Graphical methods (Histogram, QQPlot)
2. With Some Tests
"""

#histogram
import pandas as pd
pd.DataFrame(measurements).plot.hist();

#qqplot
import pylab
stats.probplot(measurements, dist = "norm", plot = pylab);

"""-
Above: Shows the sample distribution. The sample distribution is the measurements we have.
Below: Refers to the theoretical distribution. The theoretical distribution is the normal distribution we are interested in.
"""

#Shapiro-Wils Testi

"""
H0: Between the sample distribution and the theoretical normal distribution statistics as there is no significant difference.
H1: ... there is a difference.
"""

from scipy.stats import shapiro

shapiro(measurements)
#(test statistics, p-value)

"""
We can make evaluations by looking at the p-value value.
p-value <0.05  ->  H0 rejected
If H0 cannot be rejected, there is no statistically significant difference between the sample distribution and the theoretical normal distribution. T sample test can be applied.
## One Sample T Test ##
"""

#Hypothesis testing

stats.ttest_1samp(measurements, popmean=170)

"""## Nanparametrik Tek Örneklem Testi"""

from statsmodels.stats.descriptivestats import sign_test
#This test is done when the assumption is not provided.

sign_test(measurements, 170)
#(test statistics, p-value)

"""## One Sample Proportion Test
p ^: The value obtained through the sample.
p0: It is the value focused on testing.
n> 30

## Conversion Rate Test
Problem:An advertisement was placed on a medium with a software and it was stated that a conversion rate of 0.125 was achieved by the software related to this advertisement. But this situation is wanted to be controlled. Because this is a high rate and does not match when the incomes are examined.

Detail: 500 people clicked on advertisements on the outside, 40 of them came to our site and made shopping.
- Conversion rate obtained through the sample: 40/500 = 0.08
- H0: p = 0.125
- H1: p! = 0.125
"""

from statsmodels.stats.proportion import proportions_ztest

#The names of the arguments that functions expect from us
count = 40
#number of success

nobs = 500 
# number of observations

value = 0.125

proportions_ztest(count,nobs, value)
