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
#mean = 170
#sigma = 10
#data = np.random.normal(mean, sigma,250) # 250 random variables from N(170,10)
#print(data)

#fig=px.histogram(data, nbins=50, histnorm="probability density")
#fig.show()

#fig = px.box(data)
#fig.show()
# ------

import statsmodels.api as sm
import pylab as py
#data_std = (data-mean)/sigma    # standardized data
#sm.qqplot(data_std, line ='45')     #qqplot of the standardized data
#py.show()

# -----------------

dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD")) # np.random.randn(6,4) 6x4 matrix of N(0,1) random variables
print(df)
# viewing the data

print(df[df["A"] < -0.5]) # returns only the rows corresponding to the columns of A with elements < -0.5
print(df[df > 0]) # returns the elements > 0 of A, if <0 returns NaN





