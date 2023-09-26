import tkinter as tk
from tkinter import scrolledtext

class TextEditor(tk.Toplevel):
    def __init__(self, parent, square_id):
        super().__init__(parent)
        self.square_id = square_id  # Corrected indentation

        self.title("Text Editor")
        self.geometry("400x300")

        # Create a scrolled text widget
        self.text_widget = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill="both")

    def get_text(self):
        return self.text_widget.get("1.0", tk.END)

    def set_text(self, text):
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", text)
