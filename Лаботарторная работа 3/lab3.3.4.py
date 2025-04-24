import pandas as pd

df = pd.read_excel('datasets/Employee_Salary_Dataset.ods', sheet_name='Sheet1', engine='odf')

df.columns = df.columns.str.lower()

q1 = df['salary'].quantile(0.25)
q3 = df['salary'].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 3 * iqr
upper_bound = q3 + 3 * iqr

df_no_outliers = df[(df['salary'] >= lower_bound) & (df['salary'] <= upper_bound)]

print(f'До удаления выбросов: {df.shape}')
print(f'После удаления выбросов: {df_no_outliers.shape}')


