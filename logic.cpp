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

//This method goes through the library catalog and returns the text that was searched for using a keyword.
//This uses getAllBooks function as a base function. Just adds the ability to search using a keyword
vector<string> searchForText(vector<Book>& library, string& keyWord)
{
    //string::npos is used when finding substrings
    vector<string> results;
    for(const auto& text : library)
    {
        if (text.getTitle().find(keyWord) != string::npos || 
        text.getAuthor().find(keyWord) != string::npos || 
        text.getEdition().find(keyWord) != string::npos || 
        text.getPublication().find(keyWord) != string::npos)
        {
            string info = "book: " + text.getTitle() + " - " + text.getAuthor() + " (" + text.getEdition() + ", " + text.getPublication() + ")";

            results.push_back(info);
        }
    }
    return results;
}