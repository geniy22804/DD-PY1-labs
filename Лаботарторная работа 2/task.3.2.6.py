import pandas as pd

df = pd.read_excel('datasets/AmazonBooks.xlsx', sheet_name='Sheet1')

df['genre_categories'] = df['Genre'].astype('category')

df['genre_codes'] = df['genre_categories'].cat.codes

print(df[['Genre', 'genre_categories', 'genre_codes']].head())
