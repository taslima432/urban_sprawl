
import numpy as np
from numpy import loadtxt,sum,where
import matplotlib.pyplot as plt
dow = loadtxt('dow.csv', delimiter=',')
#Q1. Create a "mask" array that indicates which rows have a volume greater than 5.5 billion.
volume =dow[:,4]
mask = volume>5500000000
dow[mask]
#Q2. How many are there?  (hint: use sum).
total_days =np.sum(mask)
total_days
#Q3.Find the index of every row (or day) where the volume is greater than 5.5 billion. hint: look at the where() command.
mask_index = np.where(mask)
mask_index
#Plot the adjusted close for *every* day in 2008.
dates= np.arange(len(dow))
adjusted_close = dow[:,5]
plt.plot(dates, adjusted_close)
# Now over-plot this plot with a 'red dot' marker for every day where the volume was greater than 5.5 billion.
plt.scatter(mask_index,adjusted_close[mask_index],color= "red")
plt.show()
