from collections import defaultdict

class MovieRecommender:
    def __init__(self):
        self.movies = {}
        self.genre_movies = defaultdict(set)
        self.genre_counts = defaultdict(int)

    def add_movie(self, movie_id, title, genres):
        self.movies[movie_id] = {'title': title, 'genres': set(genres)}
        for genre in genres:
            self.genre_movies[genre].add(movie_id)
            self.genre_counts[genre] += 1

    def jaccard_similarity(self, movie1, movie2):
        genres1 = self.movies[movie1]['genres']
        genres2 = self.movies[movie2]['genres']
        intersection = len(genres1.intersection(genres2))
        union = len(genres1.union(genres2))
        return intersection / union if union > 0 else 0

    def get_recommendations(self, movie_id, n=5):
        if movie_id not in self.movies:
            return []

        similarities = []
        for other_id in self.movies:
            if other_id != movie_id:
                similarity = self.jaccard_similarity(movie_id, other_id)
                similarities.append((other_id, similarity))

        similarities.sort(key=lambda x: x[1], reverse=True)
        top_n = similarities[:n]

        recommendations = []
        for other_id, score in top_n:
            recommendations.append((self.movies[other_id]['title'], score))

        return recommendations

def main():
    recommender = MovieRecommender()

    while True:
        print("\n--- Movie Recommendation System ---")
        print("1. Add a movie")
        print("2. View all movies")
        print("3. Get recommendations")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
             movie_id = int(input("Enter movie ID: "))
             title = input("Enter movie title: ")
             genres = input("Enter genres (comma-separated): ").split(',')
             genres = [genre.strip() for genre in genres]
             recommender.add_movie(movie_id, title, genres)
             print(f"Movie '{title}' added successfully.")

        elif choice == '2':
            if not recommender.movies:
                print("No movies in the system yet.")
            else:
                print("\nAll Movies:")
                for movie_id, movie in recommender.movies.items():
                    print(f"{movie_id}: {movie['title']} - Genres: {', '.join(movie['genres'])}")

        elif choice == '3':
            if not recommender.movies:
                print("No movies in the system yet. Please add some movies first.")
            else:
                movie_id = int(input("Enter the ID of the movie you want recommendations for: "))
                if movie_id not in recommender.movies:
                    print("Movie not found.")
                else:
                    recommendations = recommender.get_recommendations(movie_id)
                    print(f"\nRecommendations for '{recommender.movies[movie_id]['title']}':")
                    if recommendations:
                        for title, score in recommendations:
                            print(f"- {title} (Similarity: {score:.2f})")
                    else:
                        print("No recommendations found.")

        elif choice == '4':
            print("Thank you for using the Movie Recommendation System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()