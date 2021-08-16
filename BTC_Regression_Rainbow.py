# Install python packages
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# data processing
df = pd.read_csv("prices.csv")
df = df.iloc[::-1]
df = df[ df['value']>0]
df['date'] = pd.to_datetime(df['date'])

# regression fitting
def funct(x, p1, p2):
    return p1*np.log(x) + p2

xdata = np.array([x+1 for x in range(len(df))])
ydata = np.log(df['value'])

popt, pcov = curve_fit(funct, xdata, ydata, p0=(3.0, -10))

fittedydata = funct(xdata, popt[0], popt[1])

plt.style.use("dark_background")

plt.semilogy(df['date'], df['value'])

for i in range(-3,5):
    #plt.plot(df['date'], np.exp(fittedydata +i))
    plt.fill_between(df['date'], np.exp(fittedydata + i -1), np.exp(fittedydata + i), alpha = 0.4)

plt.plot(df['date'], np.exp(fittedydata))

plt.ylim(bottom = 1)

plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)

plt.show()

print(popt)