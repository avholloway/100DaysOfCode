import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format 
df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", 'POSTS'], header=0)
# df = df.dropna()
df["DATE"] = pd.to_datetime(df["DATE"])
reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
reshaped_df.fillna(0, inplace=True)