import pandas as pd
import numpy as np
import re
import datetime as dt
from matplotlib import pyplot as plt
from MinnHubDriver import *  


time.sleep(60)

'''
Here we fetch the csv file that was generated from the driver
start_date is the date data collection starts, derived from variable days_ago_start
end_date is the date data collection ends, derived from variable days_ago_end
Change days_ago_start and days_ago_end in the driver if a new day range is desired
'''


str_start_date = start_date.strftime("%Y%m%d")
str_end_date = end_date.strftime("%Y%m%d")
csv_MINN_file_name = str_start_date + "-" + str_end_date + " MISO Day-Ahead Energy Price.csv"
##csv_MINN_file_name = str_start_date + "-" + "20220729" + " MISO Day-Ahead Energy Price.csv"


'''
Here we read the CSV of hourly locational marginal pricing (LMP) from different energy HUBS in MISO's power grid
'''

lmp = pd.read_csv("/Users/cartercribbs/Downloads/" + csv_MINN_file_name)
lmp = lmp.loc[lmp['node']=='MINN.HUB']
lmp.index = np.arange(0, len(lmp))
for k in range(len(lmp)):
    old_date = lmp.iloc[k]['Date']
    new_date = re.split('\s', old_date)[0]
    #Here we format all dates to datetime object format
    if(new_date[1]=="/"):
        new_date = "0" + new_date
    if(new_date[4]=="/"):
        new_date = new_date[0:3] + "0" + new_date[3:]  
    format_str = "%m/%d/%Y"
    date_time = dt.datetime.strptime(new_date, format_str)
    lmp.iloc[k,0]= date_time
    
    

'''
Here we are working with LMP data soley from Minn.Hub
We average over a 24 hour period to get a single LMP per day
'''

lmp_dayMean = lmp.groupby('Date').agg('mean')
lmp_dayMean = lmp_dayMean.reset_index()
lmp_dayMean['Date'] = pd.to_datetime(lmp_dayMean['Date'])
lmp_dayMean = lmp_dayMean.sort_values(by='Date')
lmp_dayMean = lmp_dayMean.reset_index()
lmp_dayMean = lmp_dayMean.drop('index', axis=1)


'''
Generate line graph for desired LMP day range
'''

today_date = dt.date.today() 
str_today = today_date.strftime("%m/%d/%Y")
plt.style.use('seaborn')
lmp_chart = lmp_dayMean.plot('Date', 'lmp', color = "k", linestyle = '-', linewidth = 1.8)
ax = plt.gca()
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2.5) #change width
    ax.spines[axis].set_color('#8B8989') #change color
plt.xlabel ('Date')
plt.ylabel('Day-Ahead LMP (Dollars/MWH)')
plt.legend(prop={'size':20})
plt.title("Daily Average LMP Rate of Minn Hub from MISO Over One Year")

plt.savefig("Minn Hub Data.png")

#plt.show()


