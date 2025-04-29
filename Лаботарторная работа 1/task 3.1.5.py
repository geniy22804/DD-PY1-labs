import pandas as pd

df = pd.read_excel('datasets/AmazonBooks.xlsx', sheet_name='Sheet1')

print(df.tail(10))