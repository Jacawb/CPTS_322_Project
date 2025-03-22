/********************************************************************************
** Form generated from reading UI file 'MainWindow.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QLineEdit *titleInput;
    QLineEdit *authorInput;
    QLineEdit *editionInput;
    QLineEdit *publicationInput;
    QPushButton *addButton;
    QPushButton *viewButton;
    QListWidget *bookList;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(500, 400);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        titleInput = new QLineEdit(centralwidget);
        titleInput->setObjectName(QString::fromUtf8("titleInput"));
        titleInput->setGeometry(QRect(150, 30, 200, 30));
        authorInput = new QLineEdit(centralwidget);
        authorInput->setObjectName(QString::fromUtf8("authorInput"));
        authorInput->setGeometry(QRect(150, 70, 200, 30));
        editionInput = new QLineEdit(centralwidget);
        editionInput->setObjectName(QString::fromUtf8("editionInput"));
        editionInput->setGeometry(QRect(150, 110, 200, 30));
        publicationInput = new QLineEdit(centralwidget);
        publicationInput->setObjectName(QString::fromUtf8("publicationInput"));
        publicationInput->setGeometry(QRect(150, 150, 200, 30));
        addButton = new QPushButton(centralwidget);
        addButton->setObjectName(QString::fromUtf8("addButton"));
        addButton->setGeometry(QRect(150, 190, 100, 30));
        viewButton = new QPushButton(centralwidget);
        viewButton->setObjectName(QString::fromUtf8("viewButton"));
        viewButton->setGeometry(QRect(260, 190, 120, 30));
        bookList = new QListWidget(centralwidget);
        bookList->setObjectName(QString::fromUtf8("bookList"));
        bookList->setGeometry(QRect(100, 240, 300, 100));
        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        titleInput->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter Book Title", nullptr));
        authorInput->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter Author", nullptr));
        editionInput->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter Edition", nullptr));
        publicationInput->setPlaceholderText(QCoreApplication::translate("MainWindow", "Enter Publication", nullptr));
        addButton->setText(QCoreApplication::translate("MainWindow", "Add Book", nullptr));
        viewButton->setText(QCoreApplication::translate("MainWindow", "View All Books", nullptr));
        (void)MainWindow;
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
