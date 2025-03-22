#ifndef BOOK_H
#define BOOK_H

#include <string>
using namespace std;

class Book 
{
private:
    string title, author, edition, publication;

public:
    Book(string a, string b, string c, string d)
        : title(a), author(b), edition(c), publication(d)
        {

        }

    string getTitle() const 
    { 
        return title; 
    }
    string getAuthor() const 
    { 
        return author; 
    }
    string getEdition() const 
    { 
        return edition; 
    }
    string getPublication() const 
    { 
        return publication; 
    }

    void setTitle(string newTitle) 
    {
         title = newTitle;
    }
    void setAuthor(string newAuthor) 
    { 
        author = newAuthor; 
    }
    void setEdition(string newEdition) 
    { 
        edition = newEdition; 
    }
    void setPublication(string newPublication) 
    { 
        publication = newPublication; 
    }
};

#endif // BOOK_H