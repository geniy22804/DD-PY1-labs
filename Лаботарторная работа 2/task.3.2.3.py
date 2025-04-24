import pandas as pd


df = pd.read_excel('datasets/AmazonBooks.xlsx', sheet_name='Sheet1')

expensive_books = df[df['Price'] > 20]
print(expensive_books.head())