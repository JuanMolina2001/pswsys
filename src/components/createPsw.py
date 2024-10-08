from tkinter import Entry, filedialog, messagebox, Button, Frame, ttk,Label
from ..utils import encrypt,getKey
import json
from .login import Login
class CreatePassword:
    def __init__(self, window: ttk):
        self.window = window
        self.container = Frame(window)
        Label(self.container, text="Create a password").pack()
        password = Entry(self.container, show="*")
        rPassword = Entry(self.container, show="*")
        password.pack()
        rPassword.pack()
        submitButton = Button(
            self.container, text="Submit", command=lambda: self.submit(password, rPassword)
        )
        submitButton.pack()
        self.container.pack()
    def savePassword(self,key):
        filename = filedialog.asksaveasfilename(
            title="Select a folder to save the password",
            filetypes=(("Key File", "*.key"), ("All Files", "*.*")),
            defaultextension=".key",
        )
        if filename:
            with open(filename, "wb") as f:
                f.write(key)
        with open('data.enc', 'wb') as f:
            data = json.dumps(json.loads('[{"source":"steam","user":"juanm","password":"123456789"}]')).encode()
            f.write(encrypt(data, key))
        self.container.destroy()
        Login(self.window)
    def submit(self, psw1, psw2):
        try:
            if psw1.get() != psw2.get() :
                messagebox.showerror("Error", "Passwords do not match")
            elif psw1.get() == "":
                messagebox.showerror("Error", "Password cannot be empty")
            else:
                password = psw1.get()
                key = getKey(password)
                self.savePassword(key)
                messagebox.showinfo("Success", "Password saved successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))
