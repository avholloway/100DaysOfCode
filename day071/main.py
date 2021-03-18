import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format 
df = pd.read_csv("salaries_by_college_major.csv")
df = df.dropna()
spread_col = df['Mid-Career 90th Percentile Salary'] - df['Mid-Career 10th Percentile Salary']
df.insert(1, 'Spread', spread_col)

low_risk = df.sort_values('Spread')
high_risk = df.sort_values("Spread", ascending=False)