import pandas as pd

url = 'https://ru.wikipedia.org/wiki/Доходы_населения_России'

tables = pd.read_html(url)

df = tables[-1]

sfo_subjects = [
    'Республика Алтай', 'Алтайский край', 'Республика Тыва', 'Республика Хакасия',
    'Красноярский край', 'Иркутская область', 'Кемеровская область',
    'Новосибирская область', 'Омская область', 'Томская область'
]

df_sfo = df[df['Субъект'] .isin(sfo_subjects)]

print(df_sfo)


