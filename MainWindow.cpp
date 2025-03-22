#include "MainWindow.h"
#include "ui_MainWindow.h"
#include "logic.h"
#include <QString>
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow) 
{
    ui->setupUi(this);  
}

MainWindow::~MainWindow() 
{
    delete ui;
}

void MainWindow::on_addButton_clicked() 
{
    string title = ui->titleInput->text().toStdString();
    string author = ui->authorInput->text().toStdString();
    string edition = ui->editionInput->text().toStdString();
    string publication = ui->publicationInput->text().toStdString();

    if (title.empty() || author.empty()) 
    {
        QMessageBox::warning(this, "error", "title and author cannot be empty！");
        return;
    }

    addBook(library, title, author, edition, publication);
    QMessageBox::information(this, "*Nice*", "you add a book！");
}

void MainWindow::on_viewButton_clicked() 
{
    ui->bookList->clear();
    vector<string> books = getAllBooks(library);
    for (const string& b : books)
        ui->bookList->addItem(QString::fromStdString(b));
}
