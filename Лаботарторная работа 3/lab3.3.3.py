import pandas as pd

df = pd.read_excel('datasets/Employee_Salary_Dataset.ods', sheet_name='Sheet1', engine='odf')

df.columns = df.columns.str.lower()

print(df.columns)

