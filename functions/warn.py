
from tkinter import messagebox

def warn(title, message):
    messagebox.showwarning(title, message)
    print("!Warning - " + title + " - " + message)