import pandas as pd


df = pd.read_excel('datasets/AmazonBooks.xlsx', sheet_name='Sheet1')

df_sorted = df.sort_values(by='Year', ascending=True)
print(df_sorted.head(10))