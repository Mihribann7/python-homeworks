import pandas as pd

titanic = pd.read_csv("titanic.csv")
def classify_age(age):
    return 'Child' if age < 18 else 'Adult'

titanic['Age_Group'] = titanic['Age'].apply(classify_age)

print(titanic[['Age', 'Age_Group']].head())

employees = pd.read_csv("employee.csv")

employees['Normalized_Salary'] = employees.groupby('Department')['Salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)

print(employees[['Department', 'Salary', 'Normalized_Salary']].head())

movies = pd.read_csv("movie.csv")

def classify_duration(duration):
    if duration < 60:
        return 'Short'
    elif 60 <= duration <= 120:
        return 'Medium'
    else:
        return 'Long'

movies['Length_Category'] = movies['duration'].apply(classify_duration)

print(movies[['duration', 'Length_Category']].head())
