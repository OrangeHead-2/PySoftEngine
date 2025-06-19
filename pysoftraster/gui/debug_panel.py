import tkinter as tk
from tkinter import scrolledtext

class DebugPanel(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Debug Log")
        self.text = scrolledtext.ScrolledText(self, state="normal", width=80, height=20)
        self.text.pack(fill="both", expand=True)
        self.protocol("WM_DELETE_WINDOW", self.withdraw)
        self.log("Debug panel created.")

    def log(self, msg):
        self.text.insert(tk.END, msg + "\n")
        self.text.see(tk.END)