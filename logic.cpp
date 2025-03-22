#include "logic.h"

void addBook(vector<Book>& library, string title, string author, string edition, string publication) 
{
    library.push_back(Book(title, author, edition, publication));
}

vector<string> getAllBooks(const vector<Book>& library) 
{
    vector<string> result;
    for (const auto& book : library) 
    {
        string info = "book: " + book.getTitle() + " - " + book.getAuthor() +
                      " (" + book.getEdition() + ", " + book.getPublication() + ")";
        result.push_back(info);
    }
    return result;
}