import pandas as pd
import numpy as np
import datetime as dt
##from Miso_Pricing_Driver import *  


##time.sleep(60)

'''
Here we fetch the csv file that was generated from the driver
start_date is the date data collection starts, derived from variable days_ago_start
end_date is the date data collection ends, derived from variable days_ago_end
Change days_ago_start and days_ago_end in the driver if a new day range is desired
'''


##str_start_date = start_date.strftime("%Y%m%d")
##str_end_date = end_date.strftime("%Y%m%d")
##csv_MINN_file_name = str_start_date + "-" + str_end_date + " MISO Day-Ahead Energy Price.csv"
csv_MINN_file_name = "20210801" + "-" + "20220731" + " MISO Day-Ahead Energy Price.csv"

lmp_above_total = 80.00 # in MGW/h pricing


'''
Here we read the CSV of hourly locational marginal pricing (LMP) from different energy HUBS in MISO's power grid 
We alter the data frame to show only entries from "Minn.HUB" that have an LMP above varaible "lmp_above"
'''

Minn_df = pd.read_csv("/Users/cartercribbs/Downloads/" + csv_MINN_file_name)
Minn_df = Minn_df.loc[Minn_df['node']=='MINN.HUB']
Minn_df.index = np.arange(0, len(Minn_df))
Minn_df=Minn_df.sort_values(
    by="lmp",
    ascending = False)
Minn_df=Minn_df.reset_index()
Total_Minn_df = Minn_df[(Minn_df.lmp>=lmp_above_total)]
#Six_Minn_df = Minn_df[(Minn_df.lmp>=60.00) & (Minn_df.lmp<70.00)]
#Seven_Minn_df = Minn_df[(Minn_df.lmp>=70.00) & (Minn_df.lmp<80.00)]
#Eight_Minn_df = Minn_df[(Minn_df.lmp>=80.00) & (Minn_df.lmp<90.00)]
#Nine_Minn_df = Minn_df[(Minn_df.lmp>=90.00) & (Minn_df.lmp<100.00)]
#OneHundred_Minn_df = Minn_df[(Minn_df.lmp>=100.00) & (Minn_df.lmp<110.00)]
#OneTen_Minn_df = Minn_df[(Minn_df.lmp>=110.00) & (Minn_df.lmp<120.00)]
#OneTwenty_Minn_df = Minn_df[(Minn_df.lmp>=120.00) & (Minn_df.lmp<130.00)]
#Max_Minn_df = Minn_df[(Minn_df.lmp>=130.00)]

#OneThirty_Minn_df = Minn_df[(Minn_df.lmp>=130.00) & (Minn_df.lmp<140.00)]
#OneForty_Minn_df = Minn_df[(Minn_df.lmp>=140.00) & (Minn_df.lmp<150.00)]
#OneFifty_Minn_df = Minn_df[(Minn_df.lmp>=150.00) & (Minn_df.lmp<160.00)]
#Max_Minn_df = Minn_df[(Minn_df.lmp>=160.00)]




#print(Total_Minn_df)


#print(len(Total_Minn_df))
#print(len(Six_Minn_df))
#rint(len(Seven_Minn_df))
#print(len(Eight_Minn_df))
#print(len(Nine_Minn_df))
#print(len(OneHundred_Minn_df))
#print(len(OneTen_Minn_df))
#print(len(OneTwenty_Minn_df))
#print(len(OneThirty_Minn_df))
#print(len(OneForty_Minn_df))
#print(len(OneFifty_Minn_df))
#print(len(Max_Minn_df))

# print(len(Total_Minn_df)/5)

#print("The total entires above 7.00 cents = " + len(Minn_df))



#surveys_df[(surveys_df.year >= 1980) & (surveys_df.year <= 1985)]



# Hours above a range
SevenAbove_Minn_df = Minn_df[(Minn_df.lmp>=70.00)]
EightAbove_Minn_df = Minn_df[(Minn_df.lmp>=80.00)]
TenAbove_Minn_df = Minn_df[(Minn_df.lmp>=100.00)]
FifteenAbove_Minn_df = Minn_df[(Minn_df.lmp>=150.00)]
TwentyAbove_Minn_df = Minn_df[(Minn_df.lmp>=200.00)]

print(len(SevenAbove_Minn_df))
print(len(EightAbove_Minn_df))
print(len(TenAbove_Minn_df))
print(len(FifteenAbove_Minn_df))
print(len(TwentyAbove_Minn_df))

