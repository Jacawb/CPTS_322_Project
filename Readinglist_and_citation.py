import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
#This function is used to do the initialization
#There are four main info we need to make a reading list
class BookInfo:
    def __init__(self, title, author, edition="", publish=""):
        self.title = title
        self.author = author
        self.edition = edition
        self.publish = publish

    def __str__(self):
        return f"{self.title} - {self.author} ({self.edition}, {self.publish})"
#This function is used to initialize the CitationTool
#We will have MLA and APA
class CitationTool:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def apa(self):
        return f"{self.author}. ({self.year}). \"{self.title}\". {self.publisher}."

    def mla(self):
        return f"{self.author}. \"{self.title}\". {self.publisher}, {self.year}."
#Design the UI
class ReadingListManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library")
        self.root.geometry("800x450")

        self.book_list = []

        self.setup_tabs()  

    def setup_tabs(self):
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True)
        self.book_tab()
        self.citation_tab()

    #It will be the framework for our E-lib reading list
    def book_tab(self):
        self.book_frame = tk.Frame(self.tabs)
        self.tabs.add(self.book_frame, text="My Books")

        labels = ["Title", "Author", "Edition", "Publisher"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(self.book_frame, text=text).grid(row=i, column=0, sticky="e")
            entry = tk.Entry(self.book_frame, width=40)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entries[text.lower()] = entry
    #The functionality for our reading list
        buttons = [
            ("Add", self.add),
            ("Edit", self.edit),
            ("Delete", self.remove),
            ("Search", self.find),
            ("Clear", self.clear)
        ]

        for i, (label, cmd) in enumerate(buttons):
            tk.Button(self.book_frame, text=label, width=10, command=cmd).grid(row=5, column=i, padx=5, pady=10, sticky="w")

        self.listbox = tk.Listbox(self.book_frame, width=80, height=10)
        self.listbox.grid(row=6, column=0, columnspan=5, pady=10)

    def citation_tab(self):
    # It will be used to create the Citation Tool tab
        self.cite_frame = tk.Frame(self.tabs)
        self.tabs.add(self.cite_frame, text="Citation Tool")

        labels = ["Title", "Author", "Publisher", "Year"]
        self.cite_entries = {}

        for i, text in enumerate(labels):
            tk.Label(self.cite_frame, text=text).grid(row=i, column=0, sticky="e")
            entry = tk.Entry(self.cite_frame, width=60)
            entry.grid(row=i, column=1)
            self.cite_entries[text.lower()] = entry
     # We need a button so that the users are able to generate the citation
        tk.Button(self.cite_frame, text="Generate", command=self.make_citation).grid(row=4, column=0, columnspan=2, pady=10)

        self.apa_out = tk.StringVar()
        self.mla_out = tk.StringVar()
    # Display APA citation
        tk.Label(self.cite_frame, text="APA:").grid(row=5, column=0, sticky="e")
        tk.Entry(self.cite_frame, textvariable=self.apa_out, width=80, state="readonly").grid(row=5, column=1)
    # Display MLA citation
        tk.Label(self.cite_frame, text="MLA:").grid(row=6, column=0, sticky="e")
        tk.Entry(self.cite_frame, textvariable=self.mla_out, width=80, state="readonly").grid(row=6, column=1)
# Get all the input values from the fields
    def add(self):
        t = self.entries["title"].get().strip()
        a = self.entries["author"].get().strip()
        e = self.entries["edition"].get().strip()
        p = self.entries["publisher"].get().strip()
    #Most of the books will have the name of the book and the name of author 
        if t and a == "":
            messagebox.showerror("Input Error", "Title and Author cannot be empty.")
            return

        self.book_list.append(BookInfo(t, a, e, p))
        self.refresh()
        self.clear()

    def remove(self):
        # The user will get selected item in the list
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        # If the user is not interested in the book any more then it will be removed from the list
        self.book_list.pop(idx)
        self.refresh()

    def edit(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        book = self.book_list[idx]
        # User can edit the fields one by one
        new_author = simpledialog.askstring("Author", "Edit author:", initialvalue=book.author)
        new_edition = simpledialog.askstring("Edition", "Edit edition:", initialvalue=book.edition)
        new_publish = simpledialog.askstring("Publisher", "Edit publisher:", initialvalue=book.pub)

        if new_author is not None:
            book.author = new_author
        if new_edition is not None:
            book.edition = new_edition
        if new_publish is not None:
            book.publish = new_publish

        self.refresh()
# User can use title to search the book
    def find(self):
        title = simpledialog.askstring("Search", "Enter book title:")
        if not title:
            return
    # Look for the book in the list
        for b in self.book_list:
            if b.title.lower() == title.lower():
                messagebox.showinfo("Found", str(b))
                return
    # If the book cannot be found in the list, let the user know
        messagebox.showinfo("Not found", f"No match for: {title}")

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for b in self.book_list:
            self.listbox.insert(tk.END, str(b))

# Clear all the fields
    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
 # Get the input values for citation
    def make_citation(self):
        t = self.cite_entries["title"].get().strip()
        a = self.cite_entries["author"].get().strip()
        p = self.cite_entries["publisher"].get().strip()
        y = self.cite_entries["year"].get().strip()
        #Most of the citation need at least title and author name 
        #That's why I didn't write something like if not t,a,p,y
        if not t or not a:
            messagebox.showwarning("Missing Info", "Title and Author are required.")
            return
        #Year will be an integer 
        if y and not y.isdigit():
            messagebox.showerror("Error Info", "Year must be a number.")
            return
        
        cite = CitationTool(t, a, p, y)
        self.apa_out.set(cite.apa())
        self.mla_out.set(cite.mla())


if __name__ == "__main__":
    root = tk.Tk()
    app = ReadingListManagement(root)
    root.mainloop()
