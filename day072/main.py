import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.2f}'.format 
df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", 'POSTS'], header=0)
df["DATE"] = pd.to_datetime(df["DATE"])

reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
reshaped_df.fillna(0, inplace=True)

roll_df = reshaped_df.rolling(window=12).mean()

plt.figure(figsize=(12,8)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=column)
plt.legend(fontsize=16)
plt.show()