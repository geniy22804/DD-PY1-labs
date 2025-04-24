import pandas as pd

# Загрузка датасета
df = pd.read_excel('datasets/AmazonBooks.xlsx', sheet_name='Sheet1')

# Вывод последних 10 строк
print(df.tail(10))