import tkinter as tk
from tkinter import filedialog, messagebox
from notes import save_note, load_note
from database import search_notes_by_tag, add_tag
from database import search_notes_by_keyword


class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HIVE-note")
        
        # Title Entry
        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack()
        # Tag input field
        self.tag_label = tk.Label(root, text="Tags (comma-separated):")
        self.tag_label.pack()
        self.tag_entry = tk.Entry(root, width=50)
        self.tag_entry.pack()
        self.tag_button = tk.Button(root, text="Add Tag", command=self.add_tag)
        self.tag_button.pack()
        # Search by Tag
        self.tag_search_label = tk.Label(root, text="Search:")
        self.tag_search_label.pack()
        self.tag_search_entry = tk.Entry(root, width=50)
        self.tag_search_entry.pack()

        self.tag_search_button = tk.Button(root, text="Search by tag", command=self.search_notes_by_tag)
        self.tag_search_button.pack()

        # Text Editor
        self.text_area = tk.Text(root, wrap="word", height=20, width=60)
        self.text_area.pack()

        # Buttons
        self.save_button = tk.Button(root, text="Save Note", command=self.save_note)
        self.save_button.pack()

        self.load_button = tk.Button(root, text="Load Note", command=self.load_note)
        self.load_button.pack()
        
        self.keyword_search_button = tk.Button(root, text="Search by Keyword", command=self.search_notes_by_keyword)
        self.keyword_search_button.pack()

        self.tag_search_button = tk.Button(root, text="Search by Tag", command=self.search_notes_by_tag)
        self.tag_search_button.pack()
        
        # Search Functionality (Fix: Add search entry)
        self.search_label = tk.Label(root, text="Search:")
        self.search_label.pack()
        self.search_entry = tk.Entry(root, width=50)  # <-- This line ensures search_entry exists
        self.search_entry.pack()
        
        self.keyword_search_button = tk.Button(root, text="Search by Keyword", command=self.search_notes_by_keyword)
        self.keyword_search_button.pack()
   
    def search_notes_by_tag (self):
         #Search for notes by tag and display results
        tag = self.search_entry.get().strip()
        results = []
        if tag:
            results = search_notes_by_tag(tag)
        self.display_search_results(results)


    def save_note(self):
        title = self.title_entry.get().strip()
        content = self.text_area.get("1.0", tk.END)
        
        if not title:
            messagebox.showerror("Error", "Title cannot be empty")
            return
        
        save_note(title, content)
        messagebox.showinfo("Success", f"Note '{title}' saved!")

    def load_note(self):
        title = self.title_entry.get().strip()
        if title:
            content = load_note(title)
            if content:
                 self.text_area.delete("1.0", tk.END)
                 self.text_area.insert("1.0", content)
            else:
                messagebox.showerror("Error", "Note not found")


    def search_notes_by_keyword(self):
        keyword = self.search_entry.get().strip()
        results = []
        if keyword:
            results = search_notes_by_keyword(keyword)
            self.display_search_results()
        if results:
            messagebox.showinfo("Search Results", "\n".join(results))
        else:
            messagebox.showinfo("Search Results", "No matching notes found.")


        
    
    def add_tag(self):
    #Adds tags to the currently entered note title.
        title = self.title_entry.get().strip()
        tag = self.tag_entry.get().strip()

        if not title or not tag:
            messagebox.showerror("Error", "Title and tags cannot be empty.")
    
    
        tag_list = [tag.strip() for tag in tag.split(",")]  # Split tags by commas

        if title and tag:
            add_tag(title, tag)
            messagebox.showinfo("Success", f"Tag '{tag}' added to '{title}'")
        else:
            messagebox.showerror("Error", "Title and tag cannot be empty")

    def display_search_results(self, results):
        #Helper function to show search results in a message box.
        if results:
            messagebox.showinfo("Search Results", "\n".join(results))
        else:
            messagebox.showinfo("Search Results", "No matching notes found.")

    # Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
