import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ✅ Always find the correct path to movies.csv
base_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_path, "movies.csv")

# ✅ Load the dataset
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    print("❌ 'movies.csv' file not found. Make sure it's in the same folder as code.py.")
    exit()

# ✅ Convert movie descriptions into vectors using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

# ✅ Compute similarity scores between all movies
similarity = cosine_similarity(tfidf_matrix)

# ✅ Recommend movies function
def recommend(movie_title):
    if movie_title not in df['title'].values:
        print("❌ Movie not found. Please enter an exact title from the dataset.")
        return

    index = df[df['title'] == movie_title].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\n🎯 Because you liked **{movie_title}**, you might also enjoy:\n")
    for i in scores[1:6]:
        print("🎬", df.iloc[i[0]]['title'])

# ✅ Start the program
if __name__ == "__main__":
    print("📽️ Welcome to the Movie Recommendation System!")
    movie = input("🎬 Enter a movie you like: ").strip()
    recommend(movie)
