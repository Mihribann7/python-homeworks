import pandas as pd

df = pd.read_csv('movie.csv')
print(df.sample(10))

new_df = df[df['duration'] > 120]
print(new_df)
print(df.sort_values('director_facebook_likes', ascending = False))
