print("hello")
import numpy as np
from IPython.core.pylabtools import figsize

import matplotlib
matplotlib.rc('font', family='Malgum Gothic')

figsize(11, 9)

import scipy.stats as stats

dist = stats.beta
n_trials = [0, 1, 2, 3, 4, 5, 8, 15, 50, 500]
data = stats.bernou.rvs(0.5, size=n_trials[-1])
x=np.linspace(0, 1, 100)

for k, N in enumerate