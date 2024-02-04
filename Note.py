import tkinter as tk
from tkinter import messagebox

class Noteapplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes")

        self.notiz_text = tk.Text(self.root, height=10, width=50)
        self.notiz_text.pack(pady=10)

        save_button = tk.Button(self.root, text="Save Note", command=self.note_save)
        save_button.pack()

    def note_save(self):
        notiz_text = self.notiz_text.get("1.0", "end-1c")

        if notiz_text:
            messagebox.showinfo("Note Saved", "Note was saved successfully.")
        else:
            messagebox.showwarning("Blank note", "Please enter a note before saving.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Noteapplication(root)
    root.mainloop()
