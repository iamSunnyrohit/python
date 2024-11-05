import pandas as pd
import numpy as np

data = pd.read_csv('2024.csv')
data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')

def filter_movies(movie_name=None, genre=None, min_rating=0, max_rating=10, start_year=None, end_year=None, language=None):
    filtered_data = data.copy()

    if movie_name:
        filtered_data = filtered_data[filtered_data['title'].str.contains(movie_name, case=False, na=False)]

    if genre:
        filtered_data = filtered_data[filtered_data['genres'].str.contains(genre, case=False, na=False)]

    if language:
        filtered_data = filtered_data[filtered_data['original_language'].str.contains(language, case=False, na=False)]

    filtered_data = filtered_data[(filtered_data['vote_average'] >= min_rating) & 
                                  (filtered_data['vote_average'] <= max_rating)]

    if start_year is not None:
        filtered_data = filtered_data[filtered_data['release_date'].dt.year >= start_year]
    if end_year is not None:
        filtered_data = filtered_data[filtered_data['release_date'].dt.year <= end_year]
    
    filtered_data['vote_average'] = np.floor(filtered_data['vote_average'] * 10) / 10

    sorted_data = filtered_data.sort_values(by='vote_average', ascending=False)

    return filtered_data[['title', 'vote_average', 'original_language']]