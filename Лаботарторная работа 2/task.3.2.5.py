import pandas as pd

df = pd.read_excel('datasets/AmazonBooks.xlsx', sheet_name='Sheet1')

df_2011 = df[df['Year'] == 2011]

quantile_75 = df_2011['Reviews'].quantile(0.75)

filtered_books = df_2011[df_2011['Reviews'] > quantile_75]

unique_authors = filtered_books['Author'].dropna().unique().tolist()

print(unique_authors)
