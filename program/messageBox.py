from tkinter import messagebox
import threading

class Popup:
    def __init__(self):
        pass

    def show_popup(self, title, message):
        threading.Thread(target=messagebox.showinfo, args=(str(title), str(message))).start()
