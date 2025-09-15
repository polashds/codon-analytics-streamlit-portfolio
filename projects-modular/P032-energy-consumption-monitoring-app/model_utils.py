
def recommend_movies(df, movie_name, top_n=5):
    target_genre = df[df['movie']==movie_name]['genre'].values[0]
    recommendations = df[df['genre']==target_genre]
    recommendations = recommendations[recommendations['movie']!=movie_name]
    return recommendations.head(top_n)[['movie','rating']]