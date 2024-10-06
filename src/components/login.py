from tkinter import Entry, messagebox, Button, Frame, ttk,Label
import hashlib
from .pswList import PswList
import base64
from ..utils import decrypt
import json
class Login:
    def __init__(self, window: ttk):
        self.window = window
        self.container = Frame(window)
        Label(self.container, text="PSW").pack()
        self.passwordInp = Entry(self.container, show="*")
        self.passwordInp.focus()
        self.passwordInp.pack(pady=10)
        submitButton = Button(self.container, text="Submit", command=self.submit)
        submitButton.pack(pady=10)
        self.container.pack()
    def submit(self):
        try:
            password = self.passwordInp.get()
            hashedPassword = hashlib.sha256(password.encode()).digest() 
            key = base64.urlsafe_b64encode(hashedPassword[:32])
            print('key')
            print('encryptedData')
            data = open('data.enc', 'r').read()
            decryptedData = json.loads(decrypt(data, key))
            print(decryptedData)
            pswList = PswList(decryptedData, self.window)
            def reload():
                pswList.container.destroy()
                self.submit()
            Button(pswList.container, text="reload", command=reload).pack()
            self.container.forget()
        except Exception as e:
            messagebox.showerror("Error", str(e))
