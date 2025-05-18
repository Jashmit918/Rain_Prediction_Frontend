import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("cleaned_data.csv")
# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%y')

df_2008 = df[df['Date'].dt.year == 2008]
print(df_2008.info())

#Extract Month
df_2008["Month"] = df_2008["Date"].dt.month
# Extract Year 
df["Year"] = df["Date"].dt.year


# Calculate the average rainfall for each month
monthly_avg_min = df_2008.groupby(['Month'])['MinTemp'].mean().reset_index()
monthly_avg_max = df_2008.groupby(['Month'])['MaxTemp'].mean().reset_index()

newdf = pd.merge(monthly_avg_min, monthly_avg_max, on='Month')
print(newdf)

# plt.figure(figsize=(10, 6))
# plt.bar(df['Date'], df['Rainfall'])
# plt.xlabel('Date')
# plt.ylabel('Rainfall')
# plt.title('Rainfall over Time')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()