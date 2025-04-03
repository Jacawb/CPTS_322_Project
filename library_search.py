from tkinter import simpledialog, messagebox

class LibrarySearch:
    def __init__(self, library_catalog):
        self.library_catalog = library_catalog #the library dataset

    # This function is used to search for the text in the library
    def search_for_text(self, keyword):
        results = []
        keyword = keyword.lower()

        for book in self.library_catalog:
            if (keyword in book.title.lower() or
                    keyword in book.author.lower() or
                    keyword in book.edition.lower() or
                    keyword in book.publish.lower() or
                    keyword in book.genre.lower()):
            
                info = f"book: {book.title} - {book.author} ({book.edition}, {book.publish}) [Genre: {book.genre}]"
                results.append(info)
        
        return results
    
    def find_in_catalog(self, root):
        """UI for searching in the library catalog."""
        keyword = simpledialog.askstring("Search", "Enter keyword to search:")
        if not keyword:
            return

        results = self.search_for_text(keyword)
        
        if results:
            result_str = "\n".join(results)
            messagebox.showinfo("Search Results", result_str)
        else:
            messagebox.showinfo("No Results", f"No books match: {keyword}")