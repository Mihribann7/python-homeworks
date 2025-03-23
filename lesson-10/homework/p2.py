import requests
import random

MOVIE_API_KEY = 'YOUR_TMDB_API_KEY'
base_url = 'https://api.themoviedb.org/3'
genre_url = f"{base_url}/genre/movie/list?api_key={MOVIE_API_KEY}&language=en-US"

response = requests.get(genre_url)
genres_data = response.json()

if 'genres' in genres_data:
    genres = {genre['name'].lower(): genre['id'] for genre in genres_data['genres']}
    user_genre = input("Enter a movie genre: ").strip().lower()

    if user_genre in genres:
        genre_id = genres[user_genre]
        movie_url = f"{base_url}/discover/movie?api_key={MOVIE_API_KEY}&with_genres={genre_id}"
        response = requests.get(movie_url)
        movies_data = response.json()

        if 'results' in movies_data and movies_data['results']:
            movie = random.choice(movies_data['results'])
            print(f"Recommended {user_genre.capitalize()} movie: {movie['title']} (Rating: {movie['vote_average']}/10)")
        else:
            print("No movies found for this genre.")
    else:
        print("Genre not found.")
else:
    print("Failed to retrieve genres.")