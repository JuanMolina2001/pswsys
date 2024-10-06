from tkinter import Toplevel, Label, Entry, Button, messagebox
from ..utils import auth
class PasswordMg:
    def copy(self):
        Label(self.modal, text="Write the user password").pack()
        password = Entry(self.modal, show="*")
        password.pack()
        password.bind("<Return>", lambda event: self.verify(password))
    def verify(self,password):
        if auth(password.get()):
            value = self.data["values"][-1]
            self.window.clipboard_clear()
            self.window.clipboard_append(value)
            self.modal.destroy()
        else:
            messagebox.showerror("Error", "Invalid password")
    def __init__(self ,data,window):
        self.data = data
        self.window = window
        self.modal = Toplevel(self.window)
        self.modal.title("User Password")
        self.modal.resizable(False, False)
        Button(self.modal, text="copy", command=self.copy).pack()
