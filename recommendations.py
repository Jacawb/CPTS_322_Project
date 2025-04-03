class Recommendations:
    def __init__(self, library_catalog, reading_list):
        self.library_catalog = library_catalog
        self.reading_list = reading_list

    def generate_recommendations(self):
        # Gets the genres from the user's reading list
        genres = {book.genre for book in self.reading_list}

        recommendations = []
        for book in self.library_catalog:
            if book.genre in genres and book not in self.reading_list:
                recommendations.append(book)

        return recommendations