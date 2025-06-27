import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv('movies.csv')

# Convert text to vectors using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Recommend movies
def recommend(movie_title):
    if movie_title not in df['title'].values:
        print("❌ Movie not found in database.")
        return

    idx = df[df['title'] == movie_title].index[0]
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_indices = cosine_sim.argsort()[-6:-1][::-1]

    print(f"\nBecause you liked '{movie_title}', you might also like:")
    for i in similar_indices:
        print(f"- {df['title'][i]}")

# Run the system
user_input = input("🎬 Enter a movie you like: ")
recommend(user_input.strip())
