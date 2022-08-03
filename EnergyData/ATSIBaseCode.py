import pandas as pd
import numpy as np
import sys
import re
from matplotlib import pyplot as plt


'''
Here we read the CSV of hourly locational marginal pricing (LMP) from different energy HUBS in PJM's power grid
'''
lmp = pd.read_csv("20210609-20220718 PJM Day-Ahead Price For Hubs.csv")
#print(lmp['node_name'].unique())
lmp = lmp.loc[lmp['node_name']=='ATSI GEN HUB']
lmp.index = np.arange(0, len(lmp))
#print(lmp)
for k in range(len(lmp)):
    old_date = lmp.iloc[k]['Date']
    new_date = re.split('\s', old_date)[0]
    #print(new_date)
    lmp.iloc[k,0]= new_date

'''
Here we are working with LMP data soley from ATSI power hub  
'''

lmp_dayMean = lmp.groupby('Date').agg('mean')
lmp_dayMean = lmp_dayMean.reset_index()
lmp_dayMean['Date'] = pd.to_datetime(lmp_dayMean['Date'])
lmp_dayMean = lmp_dayMean.sort_values(by='Date')
lmp_dayMean = lmp_dayMean.reset_index()
lmp_dayMean = lmp_dayMean.drop('index', axis=1)
lmp_weekMean = lmp_dayMean.groupby(pd.Grouper(freq = '2W', key = 'Date')).agg('mean').reset_index()
lmp_dayMean = lmp_weekMean
lmp_weekMean = lmp_weekMean[:-1]
#print(lmp_weekMean)
'''
Line graph creation with data points every two weeks
'''

plt.style.use('seaborn')
lmp_chart = lmp_weekMean.plot('Date', 'total_lmp', color = "k", linestyle = '--', linewidth = 3, marker = 'D', markerfacecolor = 'yellow', markeredgecolor = 'yellow')
ax = plt.gca()
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2.5) #change width
    ax.spines[axis].set_color('#8B8989') #change color
plt.xlabel ('Date (Months)')
plt.ylabel('Day-Ahead LMP (Dollars/MWH)')
plt.legend(prop={'size':20})
plt.tight_layout()
plt.title("Two Week Average LMP Rate of ATSI Gen Hub from PJM")



plt.show()