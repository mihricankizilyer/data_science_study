# -*- coding: utf-8 -*-
"""

##  User Interface Experiment (AB Test)

- H0: P1 <= P2
- H1: P1 > P2
"""

from statsmodels.stats.proportion import proportions_ztest

import numpy as np
sucess_rate = np.array([300,250])
observation_counts = np.array([1000,1100])

proportions_ztest(count = sucess_rate, nobs = observation_counts)

"""The H0 hypothesis is rejected because the p-value is significantly smaller than 0.05."""

