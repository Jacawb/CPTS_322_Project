class Recommendations:
    def __init__(self, library_catalog, reading_list):
        self.library_catalog = library_catalog
        self.reading_list = reading_list

    def generate_recommendations(self, limit=None):
        # Collect genres from reading list
        genres = {book.genre for book in self.reading_list if hasattr(book, 'genre') and book.genre}

        # Recommend books in same genre not already in reading list
        recommendations = []
        seen = set(self.reading_list)  # To avoid duplicates

        for book in self.library_catalog:
            if hasattr(book, 'genre') and book.genre in genres and book not in seen:
                recommendations.append(book)
                if limit and len(recommendations) >= limit:
                    break

        return recommendations
