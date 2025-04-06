import pandas as pd


df = pd.read_excel('titanic.xlsx')
print(df.head(5))

new_df = df.loc[(df['Age'] > 30)]
print(new_df)
female = df['Sex'].value_counts()['female']
male = df['Sex'].value_counts()['male']
print('Female: ', female)
print('Male: ', male)
