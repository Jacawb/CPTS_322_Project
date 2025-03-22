#ifndef LOGIC_H
#define LOGIC_H

#include <vector>
#include <string>
#include "Book.h"
using namespace std;

void addBook(vector<Book>& library, string title, string author, string edition, string publication);
vector<string> getAllBooks(const vector<Book>& library);

#endif // LOGIC_H
