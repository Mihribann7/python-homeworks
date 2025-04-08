import pandas as pd

titanic = pd.read_csv("titanic.csv")
grouped_titanic = titanic.groupby('Pclass').agg(
    avg_age=('Age', 'mean'),
    total_fare=('Fare', 'sum'),
    passenger_count=('PassengerId', 'count')
).reset_index()

print(grouped_titanic)

movies = pd.read_csv("movie.csv")

grouped_movies = movies.groupby(['color', 'director_name']).agg(
    total_reviews=('num_critic_for_reviews', 'sum'),
    avg_duration=('duration', 'mean')
).reset_index()

print(grouped_movies.head())

flights = pd.read_csv("flights.csv")

grouped_flights = flights.groupby(['Year', 'Month']).agg(
    total_flights=('FlightNum', 'count'),
    avg_arr_delay=('ArrDelay', 'mean'),
    max_dep_delay=('DepDelay', 'max')
).reset_index()

print(grouped_flights.head())
