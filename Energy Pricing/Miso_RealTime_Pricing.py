import pandas as pd
import numpy as np
import datetime as dt

csv_MINN_file_name = "20210801" + "-" + "20220731" + " MISO Actual Energy Price.csv"

curtailment_hour_amount = 550

Minn_df = pd.read_csv("/Users/cartercribbs/Downloads/" + csv_MINN_file_name)
Minn_df = Minn_df.loc[Minn_df['HUB']=='MINN.HUB']
Minn_df.index = np.arange(0, len(Minn_df))
#print(Minn_df)
Minn_df=Minn_df.sort_values(
     by="LMP",
     ascending = False)
Minn_df=Minn_df.reset_index()
Curtailment_Minn_df = Minn_df[0:curtailment_hour_amount]
#print(Curtailment_Minn_df)
Curtailment_Minn_df.to_excel("curtailment500.xlsx")


Total = Curtailment_Minn_df['LMP'].sum()

print(Total)

