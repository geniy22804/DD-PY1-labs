import pandas as pd
import sqlite3

url = 'https://ru.wikipedia.org/wiki/Доходы_населения_России'
tables = pd.read_html(url)

for table in tables:
    if any(col for col in table.columns if 'Субъект' in str(col) and 'руб' in ' '.join(map(str, table.columns))):
        df = table
        break

siberian_regions = [
    'Алтайский край', 'Кемеровская область', 'Красноярский край', 'Иркутская область',
    'Новосибирская область', 'Омская область', 'Томская область',
    'Республика Алтай', 'Республика Хакасия'
]

region_col = [col for col in df.columns if 'Субъект' in str(col)][0]
salary_col = [col for col in df.columns if 'руб' in str(col)][-1]

df = df[[region_col, salary_col]]
df.columns = ['region', 'salary']

df_siberia = df[df['region'].isin(siberian_regions)].copy()

df_siberia['salary'] = df_siberia['salary'].astype(str).str.replace(r'\s+', '', regex=True).str.replace(',', '.').astype(float)

conn = sqlite3.connect('incomes.db')
df_siberia.to_sql('incomes', conn, index=False, if_exists='replace')
conn.close()

print("Таблица 'incomes' успешно сохранена в базе данных incomes.db.")
