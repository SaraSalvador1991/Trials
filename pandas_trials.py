import pandas as pd
import plotly.express as px
# import data
#data_cars = pd.read_csv("//Users//sarasalvador//Downloads//cars.csv")
#print(data_cars)

#print(data_cars["hp"])

#print(data_cars.columns)

#fig = px.box(data_cars["hp"])
#fig.show()

# ---------------

import numpy as np

import norm
mean = 170
sigma = 10
data = np.random.normal(mean, sigma,250) # 250 random variables from N(170,10)
print(data)

fig=px.histogram(data, nbins=50, histnorm="probability density")
fig.show()

fig = px.box(data)
fig.show()
# ------

import statsmodels.api as sm
import pylab as py
data_std = (data-mean)/sigma    # standardized data
sm.qqplot(data_std, line ='45')     #qqplot of the standardized data
py.show()

# -----------------



