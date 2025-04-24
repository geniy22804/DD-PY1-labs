import pandas as pd


df = pd.read_excel('datasets/AmazonBooks.xlsx', sheet_name='Sheet1')

book_info = df[['Name', 'User Rating', 'Reviews']]
print(book_info.head())