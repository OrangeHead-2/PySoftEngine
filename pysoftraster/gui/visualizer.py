import tkinter as tk
from tkinter import ttk

class RasterLabGUI(tk.Tk):
    def __init__(self, engine_callback):
        super().__init__()
        self.title("PySoftEngine RasterLab")
        self.engine_callback = engine_callback
        self._build_gui()

    def _build_gui(self):
        self.canvas = tk.Canvas(self, width=512, height=512, bg="black")
        self.canvas.grid(row=0, column=0, columnspan=4)
        self.mode = tk.StringVar(value="shaded")
        ttk.Radiobutton(self, text="Wireframe", variable=self.mode, value="wireframe", command=self.update).grid(row=1, column=0)
        ttk.Radiobutton(self, text="Shaded", variable=self.mode, value="shaded", command=self.update).grid(row=1, column=1)
        ttk.Radiobutton(self, text="Depth", variable=self.mode, value="depth", command=self.update).grid(row=1, column=2)
        ttk.Button(self, text="Update", command=self.update).grid(row=1, column=3)
        self.debug = tk.Label(self, text="Ready", anchor="w")
        self.debug.grid(row=2, column=0, columnspan=4, sticky="we")
        self.update()

    def update(self):
        mode = self.mode.get()
        img, info = self.engine_callback(mode)
        self.tkimg = tk.PhotoImage(width=img.width, height=img.height, data=img.to_base64())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tkimg)
        self.debug.config(text=info)