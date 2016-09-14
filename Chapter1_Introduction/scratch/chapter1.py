import pymc3 as pm
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

%matplotlib tk

dist = stats.beta

n_trials = [0,1,2,3,4,5,8,15,50,500]
data = stats.bernoulli.rvs(0.5, size = n_trials[-1])
x = np.linspace(0,1,100)



