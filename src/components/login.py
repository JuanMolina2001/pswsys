from tkinter import Entry, messagebox, Button, Frame, ttk,Label
from .pswList import PswList
from ..utils import decrypt,getKey
import json
class Login:
    def __init__(self, window: ttk):
        self.window = window
        self.container = Frame(window)
        Label(self.container, text="PSW").pack()
        self.passwordInp = Entry(self.container, show="*")
        self.passwordInp.focus()
        self.passwordInp.pack(pady=10)
        self.passwordInp.bind("<Return>", lambda _: self.submit())
        submitButton = Button(self.container, text="Submit", command=self.submit)
        submitButton.pack(pady=10)
        self.container.pack()
    def submit(self):
        try:
            key = getKey(self.passwordInp.get())
            data = open('data.enc', 'r').read()
            decryptedData = json.loads(decrypt(data, key))
            pswList = PswList(decryptedData, self.window,key)
            def reload():
                pswList.container.destroy()
                self.submit()
            Button(pswList.container, text="reload", command=reload).pack()
            self.container.forget()
        except Exception as e:
            messagebox.showerror("Error", str(e))
